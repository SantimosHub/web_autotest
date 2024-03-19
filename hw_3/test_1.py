import yaml
import time
import logging
import os
from testpage import OperationsHelper, ContactPage, TestSearchLocators

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'img.jpeg')

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_unsuccessful_login(browser):
    logging.info("Test1 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login("test")
    test_page.enter_pass("test")
    test_page.click_login_button()
    assert test_page.get_error_text() == "401"


def test_successful_login(browser):
    logging.info("Test2 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata['email'])
    test_page.enter_pass(testdata['password'])
    test_page.click_login_button()
    hello_text = test_page.find_element(TestSearchLocators.LOCATOR_HELLO_TEXT).text
    assert f"Hello, {testdata['email']}" == hello_text


def test_user_can_create_post(browser):
    logging.info("Test3 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata['email'])
    test_page.enter_pass(testdata['password'])
    test_page.click_login_button()
    test_page.create_post_btn()
    test_page.enter_title(testdata['title'])
    test_page.enter_description(testdata['description'])
    test_page.enter_content(testdata['content'])
    test_page.attach_image(file_path)
    test_page.save_post()
    test_page.find_element(TestSearchLocators.LOCATOR_POST_IMAGE)
    post_title = test_page.find_element(TestSearchLocators.LOCATOR_POST_TITLE).text
    logging.info(f"We found text {post_title} on the page of the post")
    assert post_title == testdata['title']


def test_check_contact_us(browser):
    login_page = OperationsHelper(browser)
    login_page.go_to_site()
    login_page.login(testdata['email'], testdata['password'])
    login_page.contact_btn()
    contact_page = ContactPage(browser, browser.current_url)
    contact_page.input_name(testdata['contact_name'])
    contact_page.input_email(testdata['contact_email'])
    contact_page.input_content(testdata['contact_content'])
    contact_page.submit_form()
    time.sleep(2)
    text = contact_page.get_text_from_alert()
    assert text == 'Form successfully submitted'
