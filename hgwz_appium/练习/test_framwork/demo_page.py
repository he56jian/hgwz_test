from selenium.webdriver.common.by import By

from hgwz_test.hgwz_appium.练习.test_framwork.base_page import BasePage


class DemoPage(BasePage):
    _search_button = (By.ID, 'home_search')

    # todo: po的数据驱动
    def login(self):
        pass

    def forget_password(self):
        pass

    def search(self, keyword):
        self.po_run('search', keyword=keyword)
        # self.find(self._search_button).click()
        return self

    def back(self):
        self.po_run('back')
        return self
