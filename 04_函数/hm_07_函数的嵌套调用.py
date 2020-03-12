#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_07_函数的嵌套调用.py
    @Description    :  
    @CreateTime     :  2020/2/29 8:49 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


def test1():

    print("*" * 50)


def test2():

    print("-" * 50)

    # 函数嵌套调用
    test1()

    print("+" * 50)


test2()
