#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-03-12 11:54
# @Author  : Sandy
# @Site    : 
# @File    : hm_01_第一个面向对象.py
# @Software: PyCharm


class Cat:
    """ 这是一个猫的类 """
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()

tom.eat()
tom.drink()

print(tom)

addr = id(tom)
print("%X" % addr)
