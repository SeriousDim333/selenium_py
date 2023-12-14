import pytest
import yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from send_email import sendemail

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def browser():
    if testdata["browser"] == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def token():
    result = requests.post(
        url=testdata["url_aut"],
        data={"username": testdata["login"], "password": testdata["password"]},
    )
    token = result.json()["token"]
    return token


@pytest.fixture(scope="session")
def send_email():
    yield
    sendemail()
