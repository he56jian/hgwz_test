import pytest


class Test_calc:
    @pytest.mark.run(order=1)
    def test_add(self, get_addData, message_test):
        """
        测试相加
        :return:
        """
        a, b, expect = get_addData
        result = message_test.add(a, b)
        assert expect == result

    @pytest.mark.run(order=4)
    def test_div(self, get_divData, message_test):
        """
        测试相除
        :return:
        """
        a, b, expect = get_divData
        if b == 0:
            result = 'error'
        else:
            result = round(message_test.div(a, b), 2)
        assert expect == result

    @pytest.mark.run(order=2)
    def test_sub(self, get_subData, message_test):
        """
        测试相减
        :return:
        """
        a, b, expect = get_subData
        result = message_test.sub(a, b)
        assert expect == result

    @pytest.mark.run(order=3)
    def test_nul(self, get_nulData, message_test):
        """
        测试相乘
        :return:
        """
        a, b, expect = get_nulData
        result = message_test.mul(a, b)
        assert expect == result
