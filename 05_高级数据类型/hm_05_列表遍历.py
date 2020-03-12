#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_05_列表遍历.py
    @Description    :  
    @CreateTime     :  2020/3/1 3:40 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

name_list = ["张三", "李四", "王五", "王小二"]

# 使用迭代遍历列表
"""
顺序的从列表中依次获取数据，每一次循环过程中，数据都会保存在
my_name 这个变量中，在循环体内部可以访问到当前这一次获取的数据

for my_name in name_list:
    print("我的名字叫 %s " % my_name)

"""
for my_name in name_list:
    print("我的名字叫 %s " % my_name)
