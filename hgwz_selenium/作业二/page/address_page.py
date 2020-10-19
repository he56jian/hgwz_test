from time import sleep

from selenium.webdriver.common.by import By

from hgwz_test.hgwz_selenium.作业二.page.base_page import BasePage
from hgwz_test.hgwz_selenium.作业二.page.department_page import DepartmentPage


class AddressPage(BasePage):
    def to_main(self):
        pass

    def to_department(self):
        print('到这里了')
        # 点击添加部门进入添加部门页面
        sleep(1)
        # self._driver.find_element_by_class_name('js_add_sub_party').click()
        self._driver.find_element(By.XPATH, "//a[@class='js_add_sub_party']").click()
        return DepartmentPage(self._driver)
