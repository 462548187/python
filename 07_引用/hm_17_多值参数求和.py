#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_17_多值参数求和.py
    @Description    :  
    @CreateTime     :  2020/3/7 8:16 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


def sum_numbers(*args):

    num = 0

    print(args)
    # 循环遍历
    for n in args:
        num += n
    return num


result = sum_numbers(1, 2, 3, 4, 5)
print(result)
