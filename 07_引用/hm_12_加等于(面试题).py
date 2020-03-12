#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_12_加等于(面试题).py
    @Description    :  
    @CreateTime     :  2020/3/4 7:58 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


def demo(num, num_list):

    print("函数开始")

    # num = num +num
    num += num

    # 列表变量使用 + 不会做相加再赋值的操作
    # num_list = num_list + num_list
    # 本质上是在调用列表的 extend 方法
    num_list += num_list
    # num_list.extend(num_list)

    print(num)
    print(num_list)

    print("函数完成")


gl_num = 9
gl_list = [1, 2, 3]

demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
