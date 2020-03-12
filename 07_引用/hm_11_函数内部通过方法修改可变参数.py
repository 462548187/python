#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_11_函数内部通过方法修改可变参数.py
    @Description    :  
    @CreateTime     :  2020/3/4 7:35 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


def demo(num_list):

    print("函数内部的代码")

    num_list.append(9)

    print(num_list)

    print("函数执行完成")


gl_list = [1, 2, 3]
demo(gl_list)
print(gl_list)
