#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_05_修改全局变量.py
    @Description    :  
    @CreateTime     :  2020/3/4 5:16 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
# 全局变量
num = 10


def demo1():

    # 希望修改全局变量的值 - 使用 global 声明一下变量即可
    # global 关键字会告诉解释器后面的变量是一个全局变量
    # 在使用赋值语句时，就不会创建局部变量
    global num
    num = 99

    print("demo1 ==> %d" % num)


def demo2():
    print("demo2 ==> %d" % num)


demo1()
demo2()

