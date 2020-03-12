#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_04_列表排序.py
    @Description    :  
    @CreateTime     :  2020/3/1 3:16 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
num_list = [6, 8, 4, 1, 10]

# 升序
# num_list.sort()
# name_list.sort()

# 降序
# name_list.sort(reverse=True)
# num_list.sort(reverse=True)

# 逆序（反转）
name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)
