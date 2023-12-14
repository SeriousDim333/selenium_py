import time
from testpage import OperationsHelper
import logging
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

def test_step1(browser):
    logging.info("Test1 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test2 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("Petrr")
    testpage.enter_pass("fa258a35d9")
    testpage.click_login_button()
    assert testpage.get_head_blog() == "Blog"
    testpage.logout()
    time.sleep(3)


def test_step3(browser):
    logging.info("Test3 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("Petrr")
    testpage.enter_pass("fa258a35d9")
    testpage.click_login_button()
    time.sleep(3)
    testpage.click_create_new_post()
    time.sleep(3)
    testpage.enter_title("test title")
    testpage.enter_description("test description")
    testpage.enter_content("test content")
    testpage.click_save_post_btn()
    time.sleep(3)
    assert testpage.get_head_new_post() == "test title"
    testpage.logout()
    time.sleep(3)


def test_step4(browser):
    logging.info("Test4 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("Petrr")
    testpage.enter_pass("fa258a35d9")
    testpage.click_login_button()
    time.sleep(3)
    testpage.click_to_contact()
    testpage.enter_name_to_contact_us("petr")
    testpage.enter_email_to_contact_us("petr@petr.com")
    testpage.enter_content_to_contact_us("petr content")
    testpage.click_to_contact_us()
    time.sleep(3)
    assert testpage.get_alert_text() == "Form successfully submitted"
    
def test_step5(browser, token):
    logging.info("Test5 starting")
    testpage = OperationsHelper(browser)
    assert testdata["check_id"] in testpage.get_post_id(token)

def test_step6(browser, token, send_email):
    logging.info("Test6 starting")
    testpage = OperationsHelper(browser)
    assert "testtt" in testpage.create_post(token, 'title', 'testtt', 'content')
