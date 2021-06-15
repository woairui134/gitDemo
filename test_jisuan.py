# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pytest
import time
import allure
import methods
import yaml
import logging
from methods import jisuan

# 定义日志的级别
log = logging.getLogger()

# 取数据
with open('./shuju.yml') as f:
    #datas代表add整体字典
    datas= yaml.safe_load(f)['add']
    # aa是取值add里面的aa字典数据
    aa = datas['aa']
    print(aa)
    # bb是取值add里面的bb字典数据
    bb = datas['bb']
    print(bb)
    # cc是取值add里面的cc字典数据
    cc = datas['cc']
    print(cc)
    # bb是取值add里面的bb字典数据
    dd = datas['dd']
    print(dd)

@allure.feature("计算器")
class Test_jisuanqi():

    @allure.title("加法计算")
    # yaml中的数据aa，给变量a,b,expect赋值
    @pytest.mark.parametrize(
        "a,b,expect",
        aa,ids=bb
    )
    # 设置失败重跑，最大次数2，间隔时间为1s
    @pytest.mark.flaky(reruns=2, reruns_delay=1)

    # 设置用例执行的顺序
    @pytest.mark.run(order=1)

    # 设置加法为主题，除法依赖加法，加法失败，除法不执行
    @pytest.mark.dependency()

    def test_add(self,get_chushi,a,b,expect):

        # 判断a是不是整数和小数数据类型
        if isinstance(a,(int,float)):

            #调用jisu里面的add方法
            aaa = get_chushi.add(a,b)
            # 判断实际值是否是小数，如果是小数则取小数点后2位
            if isinstance(aaa,float):
                aaa = round(aaa,2)

            # 判断实际结果和预期是否一致,根据结果输出对应日志报告
            if pytest.assume(aaa == expect):
                log.info(f"加法结果：{a}+{b}={aaa}")
            # 判断计算错误
            else:
                log.error(f"执行错误：{a}+{b}={aaa}")
        else:
            log.info(f"加法错误：{expect}")


    @allure.title("除法计算")
    # yaml中的数据aa，给变量c,d,expect赋值
    @pytest.mark.parametrize(
        ("c,d,expect"),
        cc,ids=dd
    )
    # 设置运行顺序为2
    @pytest.mark.run(order=2)

    # 设置失败重跑
    @pytest.mark.flaky(rerun=2,reruns_delay=1)

    # 设置除法依赖加法
    # @pytest.mark.dependency(depends = ['test.add'])
    def test_division(self,get_chushi,c,d,expect):

        # 判断a是不是整数和小数数据类型
        if isinstance(c,(int,float)):
            #调用jisu里面的division方法
            cc = get_chushi.division(c,d)
            # 判断实际值是否是小数，如果是小数则取小数点后2位
            if isinstance(cc,float):
                ccc = round(cc,2)
                pytest.assume(ccc == expect)
                log.info(f"除法结果：{c}÷{d}={ccc}")
            # 非小数点判断，或者小数点计算错误判断
            elif pytest.assume(cc == expect):
                log.info(f"除法结果：{c}÷{d}={cc}")
            else:
                log.error(f"执行错误：{c}÷{d}={cc}")

        else:
            print(f"除法错误：{expect}")

if __name__ == '__main__':
    pytest.main()