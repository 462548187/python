#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_01_读取文件.py
    @Description    :  
    @CreateTime     :  2020/3/15 7:41 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

# 1. 打开文件
file = open("README")

# 2. 读取文件内容
text = file.read()
print(text)

# 3. 关闭文件
file.close()
