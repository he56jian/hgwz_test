from time import sleep

from selenium.webdriver.common.by import By

from hgwz_test.hgwz_selenium.作业二.page.base_page import BasePage


class DepartmentPage(BasePage):
    def add_department(self, departmentName):
        self._driver.find_element(By.XPATH, "//input[@name='name']").send_keys(departmentName)
        self._driver.find_element(By.XPATH, "//a[@d_ck='submit']").click()
        print(departmentName)
        sleep(1)
        name = self._driver.find_element(By.XPATH, "//span[@id='party_name']").text
        assert departmentName == name
