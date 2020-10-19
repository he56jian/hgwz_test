from hgwz_test.hgwz_selenium.作业二.page.base_page import BasePage
from hgwz_test.hgwz_selenium.作业二.page.main_page import MainPage
from hgwz_test.hgwz_selenium.作业二.page.register_page import RegisterPage


class LoginPage(BasePage):
    def do_login(self):
        # print(self._driver.get_cookies())
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851958785557'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851958785557'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a5199740'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'sites'},
            {'domain': '.qq.com', 'expiry': 1603134734, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '18UTDisqMEapV4CfwWcRBW_0AmE8Xim3fF-vIGlc18lXocT6uYNnkcb62-5HZYTH'},
            {'domain': '.qq.com', 'expiry': 1603221097, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.573628306.1603127110'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1605726700, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1666206697, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1099558400.1603127110'},
            {'domain': '.qq.com', 'expiry': 1904020056, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': '96cbb94eb945f95b'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1634663107, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1610122119, 'httpOnly': False, 'name': 'psrf_qqaccess_token', 'path': '/',
             'secure': False, 'value': '303CF370DBAEFFA0ADF480E2C5A3102D'},
            {'domain': '.qq.com', 'expiry': 1620208068, 'httpOnly': False, 'name': 'LW_uid', 'path': '/',
             'secure': False, 'value': '61R5X8w8s6Z7i2Y0T6B8U8J6n7'},
            {'domain': '.qq.com', 'expiry': 1610122119, 'httpOnly': False, 'name': 'psrf_qqunionid', 'path': '/',
             'secure': False, 'value': ''},
            {'domain': '.qq.com', 'expiry': 1610122119, 'httpOnly': False, 'name': 'euin', 'path': '/', 'secure': False,
             'value': '7eCzoKo5oKck'},
            {'domain': '.qq.com', 'expiry': 1610122119, 'httpOnly': False, 'name': 'psrf_access_token_expiresAt',
             'path': '/', 'secure': False, 'value': '1610122149'},
            {'domain': '.qq.com', 'expiry': 2147483644, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'QXQk1nJna0'},
            {'domain': '.qq.com', 'expiry': 1610122119, 'httpOnly': False, 'name': 'psrf_qqrefresh_token', 'path': '/',
             'secure': False, 'value': '7B040307B88E37A06900BFC2495AF86D'},
            {'domain': '.qq.com', 'expiry': 1620207896, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
             'secure': False, 'value': 'o1Q5a8u8E6n7m1N8a9F6n0r0J2'},
            {'domain': '.qq.com', 'expiry': 1610122119, 'httpOnly': False, 'name': 'uin', 'path': '/', 'secure': False,
             'value': '460131185'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603158643, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '3us0n9m'},
            {'domain': '.qq.com', 'expiry': 1610122119, 'httpOnly': False, 'name': 'psrf_qqopenid', 'path': '/',
             'secure': False, 'value': '1A625D38FAB377DB2F3821BF2C4F5C4A'},
            {'domain': '.qq.com', 'expiry': 1610122119, 'httpOnly': False, 'name': 'tmeLoginType', 'path': '/',
             'secure': False, 'value': '2'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'yqfSsYoDSW_RLnwiebZQKYsfrtCVDdtFfxXwRTVbG1WXPpJgQQTYPbgOQgX7zC7SOvfvDBdUEPxhFgZYG7SJNax5WzQba3hqSdfQPP0aFxYAeENKqJcV19w7f7UCvZtGOeAah9XtfRYRNwaR5mtm1rtL561apiCf8ipRnXEeSOxtO_UWknnXieX7lkc7rMB54nCld4dm-0nYCYsed9kC_-wksxIP4NIdfdY9ap3eg-B8gyWjzss_ZL6yWiVX3pwR64RmEurbmvCOJXscC0x4pg'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1634663108, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603127109'},
            {'domain': '.qq.com', 'expiry': 1911630310, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_5f2526e66530b'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '885488503693491'},
            {'domain': '.qq.com', 'expiry': 1624704480, 'httpOnly': True, 'name': 'ied_qq', 'path': '/',
             'secure': False, 'value': 'o0178889750'},
            {'domain': '.qq.com', 'expiry': 1620208142, 'httpOnly': False, 'name': 'LW_sid', 'path': '/',
             'secure': False, 'value': '1125d8P866U7G2I1X422v4e6O8'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324959169482'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '7983864832'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '8975883231'},
            {'domain': '.qq.com', 'expiry': 2147483618, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'dac51f9fbf22ebfb5d43b52c69a74eab756dea3ad6f14610ceb902f88a858ffe'}]

        self._driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame')
        return MainPage(self._driver)

    def to_register(self):
        return RegisterPage(self._driver)
