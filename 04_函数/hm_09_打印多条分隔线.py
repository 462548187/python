#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_09_打印多条分隔线.py
    @Description    :  
    @CreateTime     :  2020/2/29 9:09 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


def print_line(char, times):
    """打印多行分隔线

    :param char: 分隔字符
    :param times: 重复次数
    """
    print(char * times)


def print_lines(char, times):
    """ 打印多行分割线

    :param char: 分隔线使用的分隔字符
    :param times: 分隔线重复的次数
    """

    row = 0

    while row < 5:

        print_line(char, times)

        row += 1


print_lines("-", 20)
