#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_16_多只参数.py
    @Description    :  
    @CreateTime     :  2020/3/7 8:09 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


def demo(num, *nums, **person):

    print(num)
    print(nums)
    print(person)


demo(1)

demo(1, 2, 3, 4, 5, name="小明", age=18)
