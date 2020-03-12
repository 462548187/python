#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_16_字符串判断方法.py
    @Description    :  
    @CreateTime     :  2020/3/2 11:26 上午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

# 1. 判断空白字符
space_str = " \t\n\r"

print(space_str.isspace())


# 2. 判断字符串中是否包含数字

# 1> 都不能判断小数
# num_str = "1.2"

# 2> unicode 字符串
# num_str = "\u00b2"

# 3> 中文数字
num_str = "一千零一"

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
