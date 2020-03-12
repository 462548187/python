#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_10_不可变和可变的参数.py
    @Description    :  
    @CreateTime     :  2020/3/4 6:55 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


def demo(num, num_list):

    print("函数内部的代码")

    # 在函数内部，针对参数使用赋值语句，不会修改到外部的实参变量
    num = 100
    num_list = [1, 2, 3]

    print(num)
    print(num_list)

    print("函数执行完成")


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
