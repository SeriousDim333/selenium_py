from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.XPATH, """//*[@id="login"]/div[3]/button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_CHECK_LOGIN = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CREATE_NEW_POST_BTN = (
        By.XPATH,
        """//*[@id="app"]/main/div/div[2]/div[1]""",
    )
    LOCATOR_FIELD_TITLE = (
        By.XPATH,
        """//*[@id="create-item"]/div/div/div[1]/div/label/input""",
    )
    LOCATOR_FIELD_DESCRIPTION = (
        By.XPATH,
        """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""",
    )
    LOCATOR_FIELD_CONTENT = (
        By.XPATH,
        """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""",
    )
    LOCATOR_SAVE_POST_BTN = (
        By.XPATH,
        """//*[@id="create-item"]/div/div/div[7]/div/button""",
    )
    LOCATOR_CHECK_NEW_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_PROF = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_LOGOUT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/div/ul/li[3]""")
    LOCATOR_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]""")
    LOCATOR_FIELD_YOURNAME_CONTACTUS = (
        By.XPATH,
        """//*[@id="contact"]/div[1]/label/input""",
    )
    LOCATOR_FIELD_YOUREMAIL_CONTACTUS = (
        By.XPATH,
        """//*[@id="contact"]/div[2]/label/input""",
    )
    LOCATOR_FIELD_CONTENT_CONTACTUS = (
        By.XPATH,
        """//*[@id="contact"]/div[3]/label/span/textarea""",
    )
    LOCATOR_CONTACTUS_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(
            f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}"
        )
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(
            f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}"
        )
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(
            f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}"
        )
        return text

    def get_head_blog(self):
        blog_field = self.find_element(TestSearchLocators.LOCATOR_CHECK_LOGIN, time=3)
        text = blog_field.text
        logging.info(
            f"we find text {text} in blog field {TestSearchLocators.LOCATOR_CHECK_LOGIN[1]}"
        )
        return text

    def click_create_new_post(self):
        logging.info("Click create new post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_NEW_POST_BTN).click()

    def enter_title(self, word):
        logging.info(
            f"Send {word} to element {TestSearchLocators.LOCATOR_FIELD_TITLE[1]}"
        )
        login_field = self.find_element(TestSearchLocators.LOCATOR_FIELD_TITLE)
        login_field.clear()
        login_field.send_keys(word)

    def enter_description(self, word):
        logging.info(
            f"Send {word} to element {TestSearchLocators.LOCATOR_FIELD_DESCRIPTION[1]}"
        )
        login_field = self.find_element(TestSearchLocators.LOCATOR_FIELD_DESCRIPTION)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content(self, word):
        logging.info(
            f"Send {word} to element {TestSearchLocators.LOCATOR_FIELD_CONTENT[1]}"
        )
        login_field = self.find_element(TestSearchLocators.LOCATOR_FIELD_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

    def click_save_post_btn(self):
        logging.info("Click save new post button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def get_head_new_post(self):
        new_post_field = self.find_element(
            TestSearchLocators.LOCATOR_CHECK_NEW_POST, time=3
        )
        text = new_post_field.text
        logging.info(
            f"we find text {text} in new post field {TestSearchLocators.LOCATOR_CHECK_NEW_POST[1]}"
        )
        return text

    def logout(self):
        logging.info("logout")
        self.find_element(TestSearchLocators.LOCATOR_PROF).click()
        self.find_element(TestSearchLocators.LOCATOR_LOGOUT).click()

    def click_to_contact(self):
        logging.info("click to contact")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT).click()

    def enter_name_to_contact_us(self, word):
        logging.info(f"enter name {word} to contact us")
        login_field = self.find_element(
            TestSearchLocators.LOCATOR_FIELD_YOURNAME_CONTACTUS
        )
        login_field.clear()
        login_field.send_keys(word)

    def enter_email_to_contact_us(self, word):
        logging.info(f"enter email {word} to contact us")
        login_field = self.find_element(
            TestSearchLocators.LOCATOR_FIELD_YOUREMAIL_CONTACTUS
        )
        login_field.clear()
        login_field.send_keys(word)

    def enter_content_to_contact_us(self, word):
        logging.info(f"enter content {word} to contact us")
        login_field = self.find_element(
            TestSearchLocators.LOCATOR_FIELD_CONTENT_CONTACTUS
        )
        login_field.clear()
        login_field.send_keys(word)

    def click_to_contact_us(self):
        logging.info("click to contact us")
        self.find_element(TestSearchLocators.LOCATOR_CONTACTUS_BTN).click()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        return text
