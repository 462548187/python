#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_10_多继承的使用注意事项.py
    @Description    :  
    @CreateTime     :  2020/3/14 12:55 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


class A:

    def test(self):
        print("A---test 方法")

    def demo(self):
        print("A---demo 方法")


class B:

    def test(self):
        print("B---test 方法")

    def demo(self):
        print("B---demo 方法")


class C(A, B):
    """ 多继承可以让子类对象，同时具有多个父类 的属性和方法 """
    pass

# 创建子对象
c = C()

c.test()
c.demo()

# 确认 C 类对象调用方法的顺序
print(C.__mro__)
