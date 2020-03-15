#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_03_写入文件.py
    @Description    :  
    @CreateTime     :  2020/3/15 7:53 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


# 1. 打开
file = open("README", "a")

# 2. 写入文件
file.write("Hello123")

# 3. 关闭
file.close()