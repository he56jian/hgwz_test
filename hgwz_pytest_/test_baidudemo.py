import allure
import pytest
from selenium import webdriver
import time


# 参数化，把allreu/pytest/unittest三个参数分成三个变量，传递给测试用例的test_data参数；
@allure.feature('百度搜索')
@pytest.mark.parametrize('test_data', ['allrue', 'pytest', 'unittest'])
def test_steps_demo(test_data):
    with allure.step('打开百度首页'):
        driver = webdriver.Chrome()
        driver.get('http://www.baidu.com')
    with allure.step('搜索关键字'):
        driver.find_element_by_id('kw').send_keys(test_data)
        time.sleep(2)
        driver.find_element_by_id('su').click()
        time.sleep(2)
    with allure.step("截图，并生成截图报告"):
        driver.save_screenshot(f'./result/{test_data}.png')
        allure.attach.file('./result/b.png', attachment_type=allure.attachment_type.PNG)  # 把截图生成报告，类型为PNg
        allure.attach('<head></head><body>测试</body>', 'attach with html type', allure.attachment_type.HTML)
    driver.quit()
#后面要使用pytest test_baidudemo.py --alluredir=./result/demotest    生成测试数据
#使用allure serve alluredir=./result/demotest把测试数据转换成测试报告