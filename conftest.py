import pytest 
from selenium import webdriver

from Utilities.BaseClass import BaseClass

@pytest.fixture(scope="class")
def setup(request): 
    global driver 
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

    request.cls.driver = driver

    yield 
    driver.close()
