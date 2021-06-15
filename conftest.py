# -*- coding: utf-8 -*-
import pytest
import methods

# 用例执行时调用
@pytest.fixture(scope='class')
def get_chushi():
    print("开始计算")
    # 实例化计算方法
    jis = methods.jisuan()
    yield jis
    print("计算结束")


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        # 测试用例的名字转译,先utd-8，再解码为unicode
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # 测试用例的路转译
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
    items.reverse()