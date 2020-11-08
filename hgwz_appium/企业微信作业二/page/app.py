"""
app常用的方法：启动应用，关闭应用，重启应用，进入首页
"""
from appium import webdriver

from hgwz_test.hgwz_appium.企业微信作业二.page.basepage import BasePage
from hgwz_test.hgwz_appium.企业微信作业二.page.mainpage import MainPage


class App(BasePage):
    def start(self):
        """
        启动应用，如果driver已经被实例化，就服用driver,否则就创建一个driver

        :return:
        """
        if self.driver is None:
            _package = 'com.tencent.wework'
            _activity = '.launch.LaunchSplashActivity'
            caps = {'platformName': 'android', 'deviceName': 'hogworts', 'appPackage': _package,
                    'appActivity': _activity,
                    'autoGrantPermissions': True, 'noReset': True}
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
            self.driver.implicitly_wait(3)
        else:
            # 启动caps设置的app
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
