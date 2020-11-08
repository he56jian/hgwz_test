from appium.webdriver.common.mobileby import MobileBy

from hgwz_test.hgwz_appium.企业微信作业二.page.basepage import BasePage


class AddressPage(BasePage):
    _add_address = (MobileBy.ID, 'com.tencent.wework:id/iz')

    def add_address(self, address_value):
        # address_name = "//*[contains(@resource-id,'com.tencent.wework:id/iz')]"
        # self.driver.find_element(MobileBy.XPATH, address_name).send_keys(address_value)
        self.find_and_send(self._add_address, address_value)
        return self

    _click_ok = (MobileBy.ID, 'com.tencent.wework:id/i6k')

    def click_ok(self):
        from hgwz_test.hgwz_appium.企业微信作业二.page.contackaddpage import ContackAddPage
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'com.tencent.wework:id/i6k')]").click()
        self.find_and_click(self._click_ok)
        return ContackAddPage(self.driver)
