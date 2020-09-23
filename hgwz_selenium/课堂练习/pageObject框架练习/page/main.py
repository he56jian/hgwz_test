from selenium.webdriver.common.by import By

from hgwz_test.hgwz_selenium.课堂练习.pageObject框架练习.page.bast_page import BasePage
from hgwz_test.hgwz_selenium.课堂练习.pageObject框架练习.page.login import Login
from hgwz_test.hgwz_selenium.课堂练习.pageObject框架练习.page.register import Register


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com'

    def goto_register(self):
        self.find(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self._driver)
