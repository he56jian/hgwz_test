from appium.webdriver.common.mobileby import MobileBy

from hgwz_test.hgwz_appium.企业微信作业二.page.addressmanagepage import AddressManagePage
from hgwz_test.hgwz_appium.企业微信作业二.page.basepage import BasePage
from hgwz_test.hgwz_appium.企业微信作业二.page.memberinvitepage import MemberInvitePage


class AddressListPage(BasePage):
    _addmember = (MobileBy.XPATH, '//*[@text="添加成员"]')

    def add_member(self):
        """
        添加成员
        :return:
        """
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self.find_and_click(self._addmember)
        return MemberInvitePage(self.driver)

    _address_manage = (MobileBy.ID, 'com.tencent.wework:id/i6i')

    def goto_address_manage(self):
        # self._driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'com.tencent.wework:id/i6i')]").click()
        self.find_and_click(self._address_manage)
        return AddressManagePage(self.driver)
