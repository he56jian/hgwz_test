from appium.webdriver.common.mobileby import MobileBy

from hgwz_test.hgwz_appium.企业微信作业二.page.addresspage import AddressPage
from hgwz_test.hgwz_appium.企业微信作业二.page.basepage import BasePage


class ContackAddPage(BasePage):
    _edit_name = (MobileBy.XPATH, '//*[@text="必填"]')
    _address_page = "//*[contains(@resource-id,'com.tencent.wework:id/iy')]//*[contains(@resource-id," \
                    "'com.tencent.wework:id/b5n')] "
    _address_click = (MobileBy.XPATH, _address_page)
    _edit_phone = (MobileBy.XPATH, '//*[@text="手机号"]')

    def edit_name(self, name):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="必填"]').send_keys(name)
        self.find_and_send(self._edit_name, name)
        return self

    def click_address(self):
        # address_page = "//*[contains(@resource-id,'com.tencent.wework:id/iy')]//*[contains(@resource-id," \
        #                "'com.tencent.wework:id/b5n')] "
        # self.driver.find_element(MobileBy.XPATH, address_page).click()
        self.find_and_click(self._address_click)
        return AddressPage(self.driver)

    def edit_phone(self, phone):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys(phone)
        self.find_and_send(self._edit_phone, phone)
        return self

    _save_click = (MobileBy.ID, 'com.tencent.wework:id/i6r')

    def click_save(self):
        from hgwz_test.hgwz_appium.企业微信作业二.page.memberinvitepage import MemberInvitePage
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'com.tencent.wework:id/i6r')]").click()
        self.find_and_click(self._save_click)
        return MemberInvitePage(self.driver)
