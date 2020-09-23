from selenium.webdriver.common.by import By

from hgwz_test.hgwz_selenium.课堂练习.pageObject框架练习.page.bast_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.CSS_SELECTOR, '#corp_name').send_keys('hello')
        self.find(By.ID, 'manager_name').send_keys('hello2')
        return True
