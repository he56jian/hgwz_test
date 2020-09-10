import pytest
import yaml
import sys

from hgwz_test.hgwz_pytest_.实战一作业.pythoncode.calculator import Calculator


def get_detas():
    with open('./datas/calc.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        add_datas = mydatas['add']['datas']
        add_ids = mydatas['add']['myids']
        sub_datas = mydatas['sub']['datas']
        sub_ids = mydatas['sub']['myids']
        nul_datas = mydatas['nul']['datas']
        nul_ids = mydatas['nul']['myids']
        div_datas = mydatas['div']['datas']
        div_ids = mydatas['div']['myids']
    return {'add': [add_datas, add_ids], "sub": [sub_datas, sub_ids], "nul": [nul_datas, nul_ids],
            "div": [div_datas, div_ids]}


class Test_calc:

    def setup_class(self):
        print('测试类开始')
        self.calc = Calculator()

    def teardown_class(self):
        print('测试类结束')

    def setup(self):
        print('开始计算')

    def teardown(self):
        print('结束计算')

    @pytest.mark.parametrize('a,b,expect', get_detas()['add'][0], ids=get_detas()['add'][1])
    def test_add(self, a, b, expect):
        """
        测试相加
        :return:
        """
        result = self.calc.add(a, b)
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', get_detas()['sub'][0], ids=get_detas()['sub'][1])
    def test_sub(self, a, b, expect):
        """
        测试相减
        :return:
        """
        result = self.calc.sub(a, b)
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', get_detas()['nul'][0], ids=get_detas()['nul'][1])
    def test_nul(self, a, b, expect):
        """
        测试相乘
        :return:
        """
        result = self.calc.mul(a, b)
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', get_detas()['div'][0], ids=get_detas()['div'][1])
    def test_div(self, a, b, expect):
        """
        测试相除
        :return:
        """
        if b == 0:
            result = 'error'
        else:
            result = round(self.calc.div(a, b), 2)
        assert expect == result
