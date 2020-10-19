from selenium.webdriver.common.by import By

from hgwz_test.hgwz_selenium.作业二.page.addmember_page import AddMemberPage
from hgwz_test.hgwz_selenium.作业二.page.address_page import AddressPage
from hgwz_test.hgwz_selenium.作业二.page.base_page import BasePage
from hgwz_test.hgwz_selenium.作业二.page.import_address_page import ImportAddressPage


class MainPage(BasePage):
    def to_address(self):
        # 点击通讯录按钮，跳转到通讯录界面
        self._driver.find_element(By.XPATH, "//a[@id='menu_contacts']/span[@class='frame_nav_item_title']").click()
        return AddressPage(self._driver)

    def to_add_member(self):
        # 点击添加成员按钮，跳转到添加成员界面
        return AddMemberPage(self._driver)

    def to_import_address(self):
        # 点击导入通讯按钮，跳转到导入通讯录界面
        return ImportAddressPage(self._driver)
