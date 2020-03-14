#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_05_异常的传递.py
    @Description    :  
    @CreateTime     :  2020/3/14 10:41 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


def demo1():
    return int(input("输入整数："))


def demo2():
    return demo1()


# 利用异常的传递性，在主程序捕获异常
try:
    print(demo2())

except Exception as result:
    print("未知错误 %s" % result)

