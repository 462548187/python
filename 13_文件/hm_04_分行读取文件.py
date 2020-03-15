#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_04_分行读取文件.py
    @Description    :  
    @CreateTime     :  2020/3/15 8:02 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

file = open("README")

while True:
    text = file.readline()

    # 判断是否读取到内容
    if not text:
        break

    print(text, end="")


file.close()
