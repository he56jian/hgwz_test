from hgwz_test.hgwz_appium.练习.test_framwork import log
from hgwz_test.hgwz_appium.练习.test_framwork.base_page import BasePage


class CommonPage(BasePage):

    def __getattr__(self, item):
        # 当一个方法找不到时，会自动调用该方法；
        # 如果没有找到LoginPage方法，则会使用return方法代替没有找到的那个方法；方法代理
        log.debug(item)
        self._method_name = item
        return self._po_method

    def _po_method(self, **kwargs):
        log.debug(f"_po_method:{kwargs}")
        self.po_run(self._method_name, **kwargs)
    # def login_by_password(self,username,password):
    #     self.po_run('login_by_password',username=username,password=password)
