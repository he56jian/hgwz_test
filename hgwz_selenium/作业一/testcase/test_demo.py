import os
from os import path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo1():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()
        print('结束')

    def test_demo1(self):
        # my_cookies = self.driver.get_cookies()
        my_cookies = [{'domain': '.work.weixin.qq.com',
                       'httpOnly': False, 'name': 'wwrtx.vid',
                       'path': '/', 'secure': False, 'value': '1688851958785557'},
                      {'domain': '.work.weixin.qq.com', 'httpOnly': True,
                       'name': 'wwrtx.vst', 'path': '/', 'secure': False,
                       'value': '6wg0UflbBKT9QTomCSMVeb4qAdJ2J68KRyh1kq6Yi9Z1mRDECCKxaiGLSGjEPB3FY0DtvrznsZ4yO4XrOMjiILWp-59tQG3V8Rc24aPeIn2tTS9S-4BwNa90c0so9rOraNPDY_ryiHDfOBLfkDNzjjwNZEU_ylXemkOHjaSX0M_5XSNGoBd9kRyY6J9UQdC27ffzij-YkwEpGDKKcr4h9uuSb-DN4r2eUHiZiaW8Ccpkp9GFZu4OJACN9467cEDIDmjZuh-u0JrZDrucMGXtkw'},
                      {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/',
                       'secure': False, 'value': '1688851958785557'},
                      {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
                       'secure': False, 'value': '1970324959169482'},
                      {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/',
                       'secure': False, 'value': '18UTDisqMEapV4CfwWcRBXMe5azWL3Wks4rmJ1bdTNtTq64Xp9ozRHkwwWGQKUS6'},
                      {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/',
                       'secure': False, 'value': 'a6149106'},
                      {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/',
                       'secure': False, 'value': '2499504241256865'},
                      {'domain': 'work.weixin.qq.com', 'expiry': 1602631161, 'httpOnly': True, 'name': 'ww_rtkey',
                       'path': '/', 'secure': False, 'value': '85dmk7r'},
                      {'domain': '.qq.com', 'expiry': 1602686600, 'httpOnly': False, 'name': '_gid', 'path': '/',
                       'secure': False, 'value': 'GA1.2.40392520.1602599626'},
                      {'domain': '.qq.com', 'expiry': 1665672200, 'httpOnly': False, 'name': '_ga', 'path': '/',
                       'secure': False, 'value': 'GA1.2.1109791638.1602599626'},
                      {'domain': '.work.weixin.qq.com', 'expiry': 1634135625, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
                       'path': '/', 'secure': False, 'value': '0'},
                      {'domain': '.qq.com', 'expiry': 1906212317, 'httpOnly': False, 'name': 'tvfe_boss_uuid',
                       'path': '/', 'secure': False, 'value': '873597962a20538b'},
                      {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
                       'secure': False, 'value': '4078916608'},
                      {'domain': '.qq.com', 'expiry': 1905262701, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
                       'secure': False, 'value': '0_5ec3fd6c93313'},
                      {'domain': '.qq.com', 'expiry': 2147483652, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
                       'secure': False, 'value': '7419cc8458c465c321c368d687567d533fc898905ae9ac7340f4f0e688f83add'},
                      {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/',
                       'secure': False, 'value': 'NeRsxlJsaW'},
                      {'domain': '.work.weixin.qq.com', 'expiry': 1605192203, 'httpOnly': False,
                       'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'},
                      {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/',
                       'secure': False, 'value': '1'},
                      {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/',
                       'secure': False, 'value': 'direct'},
                      {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
                       'secure': False, 'value': '5154665268'}]
        # print(my_cookies)
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        for cookies in my_cookies:
            print(cookies)
            self.driver.add_cookie(cookies)
        #
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')

        self.driver.find_element(By.LINK_TEXT, '导入通讯录').click()
        inputs = self.driver.find_element(By.XPATH, '//input[@type="file"]')
        pathnew = os.path.abspath(os.path.join(os.getcwd(), "../test_num.xlsx"))
        inputs.send_keys(pathnew)
        assert "test_num.xlsx" == self.driver.find_element(By.XPATH,
                                                           '//div[@class="ww_fileImporter_fileContainer_fileNames"]').text
        sleep(5)

# if __name__ == '__main__':
#     print('当前路径',os.path.abspath(os.path.join(os.getcwd(), "../test_num.xlsx")))
