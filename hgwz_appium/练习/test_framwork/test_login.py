import pytest

from hgwz_test.hgwz_appium.练习.test_framwork.demo_page import DemoPage


class TestLogin:
    def setup_class(self):
        self.demo = DemoPage()
        self.demo.start_app()

    # todo:测试数据的数据驱动
    @pytest.mark.parametrize('username,password', [
        ('user1', 'password1'),
        ('user2', 'password2')
    ])
    def test_login(self, username, password):
        # todo: 测试步骤的数据驱动
        self.demo.login(username, password)
        assert 1 == 1

    @pytest.mark.parametrize('keyword', [
        'alibaba',
        'baidu'
    ])
    def test_search(self, keyword):
        self.demo.search(keyword)
