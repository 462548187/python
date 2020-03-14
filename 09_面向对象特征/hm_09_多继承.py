#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_09_多继承.py
    @Description    :  
    @CreateTime     :  2020/3/14 12:45 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


class A:

    def test(self):
        print("test 方法")


class B:

    def demo(self):
        print("demo 方法")


class C(A, B):
    """ 多继承可以让子类对象，同时具有多个父类 的属性和方法 """
    pass

# 创建子对象
c = C()

c.test()
c.demo()
