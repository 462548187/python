#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_05_函数的参数.py
    @Description    :  
    @CreateTime     :  2020/2/29 8:11 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     :
"""


def sum_2_num(num1, num2):
    """ 对两个数字的求和 """

    # num1 = 10
    # num2 = 20

    result = num1 + num2

    print("%d + %d = %d" % (num1, num2, result))


sum_2_num(1, 2)
