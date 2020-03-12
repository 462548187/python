#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-03-12 16:43
# @Author  : Sandy
# @Site    : 
# @File    : hm_07_del方法.py
# @Software: PyCharm


class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)