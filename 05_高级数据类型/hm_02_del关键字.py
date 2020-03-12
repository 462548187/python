#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_02_del关键字.py
    @Description    :  
    @CreateTime     :  2020/3/1 2:28 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

name_list = ["张三", "李四", "王五"]

# (知道) 使用 del 关键词（delete）删除列表元素
# 提示： 在日常开发中，要从列表删除数据，建议使用列表提供的方法
del name_list[1]

# del 关键字本质上是用来将一个变量从内存中删除的
name = "小明"

del name

# 注意：如果使用 del 关键字将变量从内存中删除
# 后续的代码就不能再使用这个变量了
# print(name)

print(name_list)
