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