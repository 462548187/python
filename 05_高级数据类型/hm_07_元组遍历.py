#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_07_元组遍历.py
    @Description    :  
    @CreateTime     :  2020/3/1 5:02 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
info_tuple = ("zhangsan", 18, 1.75)

# 使用迭代遍历元组

for my_info in info_tuple:

    # 使用格式字符串拼接 my_info 这个变量不方便！
    # 因为元组中通常保存的数据类型是不同的
    print(my_info)
