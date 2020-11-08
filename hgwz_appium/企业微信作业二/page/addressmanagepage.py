from appium.webdriver.common.mobileby import MobileBy

from hgwz_test.hgwz_appium.企业微信作业二.page.basepage import BasePage
from hgwz_test.hgwz_appium.企业微信作业二.page.revmessagepage import RevMessagePage


class AddressManagePage(BasePage):
    def goto_revmessage(self, name_value):
        _rev = (MobileBy.XPATH, f'//*[@text="{name_value}"]')
        # 进入成员修改信息页面
        # self._driver.find_element(MobileBy.XPATH, f'//*[@text="{name_value}"]').click()
        self.find_and_click(_rev)
        return RevMessagePage(self.driver)

    def get_list(self):
        name_xpath = "//*[contains(@resource-id,'com.tencent.wework:id/icn')]/*[@class='android.widget.TextView']"
        names = [value.text for value in self.driver.find_elements(MobileBy.XPATH, name_xpath)]
        return names
