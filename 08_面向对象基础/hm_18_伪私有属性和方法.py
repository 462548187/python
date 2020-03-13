#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_18_伪私有属性和方法.py
    @Description    :  
    @CreateTime     :  2020/3/13 8:19 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")

# 伪私有属性，在外界是不能被直接访问的
print(xiaofang._Women__age)

# 伪私有方法，同样不允许在外界直接访问
xiaofang._Women__secret()
