from appium.webdriver.common.mobileby import MobileBy

from hgwz_test.hgwz_appium.企业微信作业二.page.basepage import BasePage


class RevMessagePage(BasePage):
    _del_mess = (MobileBy.XPATH, '//*[@text="删除成员"]')

    def del_mess(self):
        # self._driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        self.find_and_click(self._del_mess)
        return self

    _del_ok = (MobileBy.ID, 'com.tencent.wework:id/blx')

    def click_ok(self):
        from hgwz_test.hgwz_appium.企业微信作业二.page.addressmanagepage import AddressManagePage
        # self._driver.find_element(MobileBy.ID, 'com.tencent.wework:id/blx').click()
        self.find_and_click(self._del_ok)
        return AddressManagePage(self.driver)
