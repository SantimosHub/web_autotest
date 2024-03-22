import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

ids = dict()
with open("./locators.yaml") as f:
    locators = yaml.safe_load(f)
for locator in locators["xpath"].keys():
    ids[locator] = (By.XPATH, locators["xpath"][locator])
for locator in locators["css"].keys():
    ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])



class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send '{word}' to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operate with {locator}")
            return False
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def enter_login(self, word):
        self.enter_text_into_field(ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def click_login_button(self):
        self.click_button(ids["LOCATOR_LOGIN_BTN"], description="login")

    def login(self, login, passwd):
        self.enter_login(login)
        self.enter_pass(passwd)
        self.click_login_button()

    def get_error_text(self):
        return self.get_text_from_element(ids["LOCATOR_ERROR_FIELD"], description="error label")

    def create_post_btn(self):
        self.click_button(ids["LOCATOR_CREATE_POST_BTN"], description="new post")

    def enter_title(self, title):
        self.enter_text_into_field(ids["LOCATOR_TITLE_INPUT"], title, description="title")

    def enter_description(self, description):
        self.enter_text_into_field(ids["LOCATOR_DESCRIPTION_INPUT"], description, description="description")

    def enter_content(self, content):
        self.enter_text_into_field(ids["LOCATOR_CONTENT_INPUT"], content, description="content")

    def save_post(self):
        self.click_button(ids["LOCATOR_SAVE_POST_BTN"], description="save")

    def contact_btn(self):
        self.click_button(ids["LOCATOR_CONTACT_BTN"], description="contact")

    def attach_image(self, path):
        self.find_element(ids["LOCATOR_ATTACH_IMAGE"]).send_keys(path)

    def input_name(self, name):
        self.enter_text_into_field(ids["LOCATOR_CONTACT_NAME_INPUT"], name, description="contact_name")

    def input_email(self, email):
        self.enter_text_into_field(ids["LOCATOR_CONTACT_EMAIL_INPUT"], email, description="contact_email")

    def input_content(self, content):
        self.enter_text_into_field(ids["LOCATOR_CONTACT_CONTENT_INPUT"], content, description="contact_content")

    def submit_form(self):
        self.click_button(ids["LOCATOR_CONTACT_SUBMIT_BTN"], description="contact")


