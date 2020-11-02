import pytest

from hgwz_test.hgwz_appium.练习.test_framwork.base_page import BasePage
from hgwz_test.hgwz_appium.练习.test_framwork.demo_page import DemoPage
from hgwz_test.hgwz_appium.练习.test_framwork.common_page import CommonPage
from hgwz_test.hgwz_appium.练习.test_framwork.utils import Utils


class TestLogin:
    testcase_file = 'test_search.yaml'
    po_file = 'page_demo.yaml'
    data = Utils.from_file(testcase_file)

    def setup_class(self):
        self.app = BasePage()
        self.app.start_app()

        # self.demo.start_app()

    def setup(self):
        pass

    def teardown(self):
        pass

    # todo:测试数据的数据驱动
    @pytest.mark.parametrize('username,password', [
        ('user1', 'password1'),
        ('user2', 'password2')
    ])
    def test_login(self, username, password):
        # todo: 测试步骤的数据驱动
        self.demo = DemoPage(self.po_file)
        self.demo.login(username, password)
        assert 1 == 1

    # @pytest.mark.parametrize('keyword', [
    #     'alibaba',
    #     'baidu'
    # ])
    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search(self, keyword):
        self.demo = DemoPage(self.po_file)
        self.demo.search(keyword)
        self.demo.back()

    #  用commonpage
    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search_common(self, keyword):
        demo = CommonPage(self.po_file)
        demo.search(keyword=keyword)
        demo.back()


    def test_login(self):
        po_file = 'page_login.yaml'
        login = CommonPage(po_file)
        # login.start_app()     #因为在之前把start变成了类方法，执行了一次之后，driver就会变成类变量，就不用重复获取
        # login.login_by_password('12315645612','123456')
        login.login_by_password(username='12315645612', password='123456')
