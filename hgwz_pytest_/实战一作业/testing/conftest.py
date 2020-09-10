def pytest_collection_modifyitems(items):
    """
    测试用例收集完成之后，将收集的item进行处理;将收集到的item的name和nodeid的中文显示在控制台
    :param items:
    :return:
    """
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')
