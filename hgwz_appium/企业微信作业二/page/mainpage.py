from appium.webdriver.common.mobileby import MobileBy

from hgwz_test.hgwz_appium.企业微信作业二.page.addresslistpage import AddressListPage
from hgwz_test.hgwz_appium.企业微信作业二.page.basepage import BasePage


class MainPage(BasePage):
    _addresslist = (MobileBy.XPATH, '//*[@text="通讯录"]')

    def goto_addresslist(self):
        self.find_and_click(self._addresslist)
        return AddressListPage(self.driver)
