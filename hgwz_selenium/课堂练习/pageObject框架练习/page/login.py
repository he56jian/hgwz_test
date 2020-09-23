from selenium.webdriver.common.by import By

from hgwz_test.hgwz_selenium.课堂练习.pageObject框架练习.page.bast_page import BasePage
from hgwz_test.hgwz_selenium.课堂练习.pageObject框架练习.page.register import Register


class Login(BasePage):
    def scan(self):
        pass

    def goto_register(self):
        self.find(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return Register(self._driver)
