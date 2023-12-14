from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import requests
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru/"

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator),
                message=f"Cant find element by locator {locator}",
            )
        except:
            logging.exception("Find element exception")
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(
                f"Property {property} not found in element with locator {locator}"
            )
            return None

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open site")
            start_browsing = None
        return start_browsing

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception("Exception with alert")
            return None

    def post_id(self, token):
        try:
            res_get = requests.get(
                url=testdata["url"],
                headers={"X-Auth-Token": token},
                params={"owner": "notMe"},
            )
        except:
            logging.exception("exception with post id")
            return None
        list_id = [i["id"] for i in res_get.json()["data"]]
        return list_id

    def create_post(self, token, title, description, content):
        try:
            requests.post(
                url=testdata["url_create_post"],
                headers={"X-Auth-Token": token},
                params={"title": title, "description": description, "content": content},
            )
        except:
            logging.exception("exception with create post")
            return None
        try:
            res_get = requests.get(url=testdata["url"], headers={"X-Auth-Token": token})
        except:
            logging.exception("exception with description post")
        list_description = [i["description"] for i in res_get.json()["data"]]
        return list_description
