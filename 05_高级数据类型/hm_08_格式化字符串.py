#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_08_格式化字符串.py
    @Description    :  
    @CreateTime     :  2020/3/1 5:10 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

info_tuple = ("小明", 18, 1.75)
# 格式化字符串后面的 '()' 本质上就是元组
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple

print(info_str)
