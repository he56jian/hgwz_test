from time import sleep

import pytest
import yaml

from hgwz_test.hgwz_appium.企业微信作业二.page.app import App


def get_contack():
    with open('../data/contack.yaml', 'rb') as f:
        datas = yaml.safe_load(f)
    return datas


class TestWexin:

    def setup(self):
        """启动APP"""
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize('name,phone,address', get_contack(), ids=['新姓名1'])
    def test_addcontack(self, name, phone, address):
        mypage = self.main.goto_addresslist().add_member() \
            .addmember_menual().edit_name(name).edit_phone(phone) \
            .click_address().add_address(address).click_ok().click_save()
        mytoast = mypage.get_toast()
        assert mytoast == '添加成功'

    @pytest.mark.parametrize('name,phone,address', get_contack(), ids=['新姓名1'])
    def test_delcontack(self, name, phone, address):
        mypage = self.main.goto_addresslist().goto_address_manage().goto_revmessage(name) \
            .del_mess().click_ok()
        sleep(1)
        mylist = mypage.get_list()
        assert name not in mylist
