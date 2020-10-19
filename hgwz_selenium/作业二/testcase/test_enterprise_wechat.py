from hgwz_test.hgwz_selenium.作业二.page.login_page import LoginPage


class TestWechat:
    def setup_method(self):
        self.login = LoginPage()
        print('开始')

    def teardown_method(self):
        print('结束')

    def test_demo(self):
        self.login.do_login().to_address().to_department().add_department('新部门')
