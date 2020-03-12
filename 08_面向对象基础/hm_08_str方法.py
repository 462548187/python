#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_08_str方法.py
    @Description    :  
    @CreateTime     :  2020/3/12 9:31 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 我去了" % self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "我是小猫[%s]" % self.name


# tom 是一个全局变量
tom = Cat("Tom")
print(tom)
