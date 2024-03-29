import pytest
import yaml
import requests
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


@pytest.fixture(scope="function")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


S = requests.Session()


@pytest.fixture()
def user_login():
    try:
        result = S.post(url=testdata['url'], data={'username': testdata['email'], 'password': testdata['password']})
        response_json = result.json()
        token = response_json.get('token')
    except:
        logging.exception("Get token exception")
        token = None
    logging.debug(f"Return token success")
    return token
