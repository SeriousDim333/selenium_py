from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open(r"D:\обучение\selenium_py\task\locators.yaml") as f:
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
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exeption while operation with {locator}")
            return False
        return True

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

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"we find text {text} in field {element_name}")
        return text

    # enter text
    def enter_login(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"],
            word,
            description="login field",
        )

    def enter_pass(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="pass field"
        )

    def enter_title(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_FIELD_TITLE"],
            word,
            description="title field",
        )

    def enter_description(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_FIELD_DESCRIPTION"],
            word,
            description="description field",
        )

    def enter_content(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_FIELD_CONTENT"],
            word,
            description="content field",
        )

    def enter_name_to_contact_us(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_FIELD_YOURNAME_CONTACTUS"],
            word,
            description="name to contact us field",
        )

    def enter_email_to_contact_us(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_FIELD_YOUREMAIL_CONTACTUS"],
            word,
            description="email to contact us field",
        )

    def enter_content_to_contact_us(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_FIELD_CONTENT_CONTACTUS"],
            word,
            description="content to contact us field",
        )

    # click
    def click_login_button(self):
        self.click_button(
            TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login"
        )

    def click_to_contact_us(self):
        self.click_button(
            TestSearchLocators.ids["LOCATOR_CONTACTUS_BTN"], description="contact us"
        )

    def click_to_contact(self):
        self.click_button(
            TestSearchLocators.ids["LOCATOR_CONTACT"], description="contact"
        )

    def click_save_post_btn(self):
        self.click_button(
            TestSearchLocators.ids["LOCATOR_SAVE_POST_BTN"], description="save post"
        )

    def click_create_new_post(self):
        self.click_button(
            TestSearchLocators.ids["LOCATOR_CREATE_NEW_POST_BTN"],
            description="create new post",
        )

    # get text

    def get_head_new_post(self):
        return self.get_text_from_element(
            TestSearchLocators.ids["LOCATOR_CHECK_NEW_POST"], description="post name"
        )

    def get_error_text(self):
        return self.get_text_from_element(
            TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="error text"
        )

    def get_head_blog(self):
        return self.get_text_from_element(
            TestSearchLocators.ids["LOCATOR_CHECK_LOGIN"], description="head blog text"
        )

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text

    def logout(self):
        logging.info("logout")
        self.find_element(TestSearchLocators.ids["LOCATOR_PROF"]).click()
        self.find_element(TestSearchLocators.ids["LOCATOR_LOGOUT"]).click()

    def get_post_id(self, token):
        post_id = self.post_id(token)
        return post_id

    def get_create_post(self, token, title, description, content):
        result = self.create_post(token, title, description, content)
        return result
