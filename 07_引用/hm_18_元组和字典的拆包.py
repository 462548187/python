#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_18_元组和字典的拆包.py
    @Description    :  
    @CreateTime     :  2020/3/7 8:43 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}


# demo(gl_nums, gl_dict)

# 拆包语法，简化元组变量/字典变量的传递
demo(*gl_nums, **gl_dict)

demo(1, 2, 3, name="小明", age=18)