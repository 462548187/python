#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-03-11 11:27
# @Author  : Sandy
# @Site    : 
# @File    : hm_20_递归求和.py
# @Software: PyCharm


# 定义一个函数 sum_numbers
# 能够接受一个 num 的整数参数
# 计算 1 + 2 + ... num 的结果

def sum_numbers(num):

    # 1. 出口
    if num == 1:
        return 1

    # 2. 数字的累加 num + （1 ... num - 1）
    # 假设 sum_numbers 能够正确的处理 1 ... num - 1
    temp = sum_numbers(num - 1)

    # 两个数累加
    return num + temp

result = sum_numbers(2)
print(result)
