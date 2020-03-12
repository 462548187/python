#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_04_函数不能直接修改全局变量.py
    @Description    :  
    @CreateTime     :  2020/3/4 5:14 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
# 全局变量
num = 10


def demo1():

    # 希望修改全局变量的值
    # 在 python 中，是不允许直线修改全局变量的值
    # 如果使用赋值语句，会在函数 内部，定义一个局部变量
    num = 99

    print("demo1 ==> %d" % num)


def demo2():
    print("demo2 ==> %d" % num)


demo1()
demo2()

