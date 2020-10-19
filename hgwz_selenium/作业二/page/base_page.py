from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            # option = Options()
            # option.debugger_address='localhost:9222'
            # self._driver = webdriver.Chrome(options=option)
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
