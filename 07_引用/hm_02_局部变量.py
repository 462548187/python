#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_02_局部变量.py
    @Description    :  
    @CreateTime     :  2020/3/4 3:31 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


def demo1():

    # 定义一个局部变量
    # 1> 出生：执行了下方的代码之后，才会被创建
    # 2> 死亡：函数执行完成之后
    num = 10

    print("在demo1 函数内部的变量是 %d" % num)


def demo2():

    # print("%d" % num)
    pass

# 在函数内部定义的变量，不能再其他位置使用
# print("%d" % num)


demo1()

demo2()
