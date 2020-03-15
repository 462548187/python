#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_02_读取文件后文件指针会改变.py
    @Description    :  
    @CreateTime     :  2020/3/15 7:49 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

# 1. 打开文件
file = open("README")

# 2. 读取文件内容
text = file.read()
print(text)
print(len(text))

print("-" * 50)

text = file.read()
print(text)
print(len(text))

# 3. 关闭文件
file.close()
