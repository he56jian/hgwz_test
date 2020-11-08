from appium.webdriver.common.mobileby import MobileBy

from hgwz_test.hgwz_appium.企业微信作业二.page.basepage import BasePage
from hgwz_test.hgwz_appium.企业微信作业二.page.contackaddpage import ContackAddPage


class MemberInvitePage(BasePage):
    _addmember = (MobileBy.XPATH, '//*[@text="手动输入添加"]')

    def addmember_menual(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.find_and_click(self._addmember)
        return ContackAddPage(self.driver)

    def get_toast(self):
        value = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return value
