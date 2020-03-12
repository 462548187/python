#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-03-12 16:35
# @Author  : Sandy
# @Site    : 
# @File    : hm_06_利用参数设置属性初始值.py
# @Software: PyCharm


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-03-12 16:04
# @Author  : Sandy
# @Site    :
# @File    : hm_05_初始化方法.py
# @Software: PyCharm


class Cat:
    """ 这是一个猫类 """

    def __init__(self, new_name):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
tom = Cat("Tom")
tom.eat()

print(tom.name)

lazy_cat = Cat("大懒猫")
lazy_cat.eat()
