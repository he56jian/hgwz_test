# def pytest_collection_modifyitems(items):
#     """
#     测试用例收集完成之后，将收集的item进行处理;将收集到的item的name和nodeid的中文显示在控制台
#     :param items:
#     :return:
#     """
#     for item in items:
#         item.name = item.name.encode('utf-8').decode('unicode_escape')
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')
from typing import List

import pytest
import yaml

from pythoncode.calculator import Calculator


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.fixture(scope='module')
def message_test():
    print('开始计算')
    calc = Calculator()
    yield calc
    print('结束计算')


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


@pytest.fixture(params=get_detas()['add'][0], ids=get_detas()['add'][1])
def get_addData(request):
    return request.param


@pytest.fixture(params=get_detas()['sub'][0], ids=get_detas()['sub'][1])
def get_subData(request):
    return request.param


@pytest.fixture(params=get_detas()['nul'][0], ids=get_detas()['nul'][1])
def get_nulData(request):
    return request.param


@pytest.fixture(params=get_detas()['div'][0], ids=get_detas()['div'][1])
def get_divData(request):
    return request.param
