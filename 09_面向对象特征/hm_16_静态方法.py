#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_16_静态方法.py
    @Description    :  
    @CreateTime     :  2020/3/14 6:09 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


class Dog(object):

    @staticmethod
    def run():

        # 不访问实例属性/类属性
        print("小狗要跑...")


# 通过 类名.调用静态方法 - 不需要创建对象
Dog.run()
