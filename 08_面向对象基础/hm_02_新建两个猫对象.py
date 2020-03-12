#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-03-12 14:34
# @Author  : Sandy
# @Site    : 
# @File    : hm_02_新建两个猫对象.py
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

# 在创建一个猫对象
lazy_cat = Cat()

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)
