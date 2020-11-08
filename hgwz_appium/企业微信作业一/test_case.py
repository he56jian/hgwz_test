from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestCase:
    new_name = '新的姓名'

    def setup(self):
        # com.tencent.wework/.launch.LaunchSplashActivity
        _package = 'com.tencent.wework'
        _activity = '.launch.LaunchSplashActivity'
        caps = {'platformName': 'android', 'deviceName': 'hogworts', 'appPackage': _package, 'appActivity': _activity,
                'autoGrantPermissions': True, 'noReset': True}
        self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self._driver.implicitly_wait(3)
        # 直接启动app
        # self._driver.start_activity(_package, _activity)

    def teardown(self):
        self._driver.quit()
        # pass

    def test_add(self):
        """
        # 点击通讯录
          点击添加成员；点击手动输入添加；
          选择必填选项，输入名字，
          选择手机号选项，输入名字，
          点击地址，进入新页面，输入地址；点击确定;
          点击保存；
        :return:
        """

        self._driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self._driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self._driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()

        self._driver.find_element(MobileBy.XPATH, '//*[@text="必填"]').send_keys(self.new_name)
        self._driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys('123456789123')

        # 地址 = //*[contains(@resource-id,'com.tencent.wework:id/iy')]//*[contains(@resource-id,'com.tencent.wework:id/b5n')]
        address = "//*[contains(@resource-id,'com.tencent.wework:id/iy')]//*[contains(@resource-id,'com.tencent.wework:id/b5n')]"
        self._driver.find_element(MobileBy.XPATH, address).click()
        address_name = "//*[contains(@resource-id,'com.tencent.wework:id/iz')]"
        self._driver.find_element(MobileBy.XPATH, address_name).send_keys('新地址')
        sleep(1)
        self._driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'com.tencent.wework:id/i6k')]").click()
        sleep(3)
        self._driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'com.tencent.wework:id/i6r')]").click()
        sleep(3)
        self._driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'com.tencent.wework:id/i63')]").click()
        #
        name = "//*[contains(@resource-id,'com.tencent.wework:id/icn')]/*[@class='android.widget.TextView']"
        names = [value.text for value in self._driver.find_elements(MobileBy.XPATH, name)]
        assert self.new_name in names

    def test_del(self):
        self._driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self._driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'com.tencent.wework:id/i6i')]").click()
        self._driver.find_element(MobileBy.XPATH, f'//*[@text="{self.new_name}"]').click()
        self._driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        sleep(1)
        self._driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'com.tencent.wework:id/blx')]").click()
        sleep(1)
        name_xpath = "//*[contains(@resource-id,'com.tencent.wework:id/icn')]/*[@class='android.widget.TextView']"
        names = [value.text for value in self._driver.find_elements(MobileBy.XPATH, name_xpath)]
        assert self.new_name not in names
