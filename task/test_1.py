import yaml
from module import Site
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(site, log_xpath, pass_xpath, btn_xpath, result_xpath):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys("test")
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys("test")
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    err_lable = site.find_element("xpath", result_xpath)
    assert err_lable.text == "401"


def test_step2(site, log_xpath, pass_xpath, btn_xpath, result_login):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    login = site.find_element("xpath", result_login)
    assert login.text == "Blog"


def test_step3(site, log_xpath, pass_xpath, btn_xpath, create_new_post, title, description, content, save_post_btn, name_post):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    time.sleep(testdata["sleep_time"])
    input3 = site.find_element("xpath", create_new_post)
    input3.click()
    time.sleep(testdata["sleep_time"])
    input4 = site.find_element("xpath", title)
    input4.send_keys(testdata["text_test"])
    input5 = site.find_element("xpath", description)
    input5.send_keys(testdata["text_test"])
    input6 = site.find_element("xpath", content)
    input6.send_keys(testdata["text_test"])
    input7 = site.find_element("xpath", save_post_btn)
    input7.click()
    time.sleep(testdata["sleep_time"])
    check = site.find_element("xpath", name_post)
    assert check.text == testdata["text_test"]