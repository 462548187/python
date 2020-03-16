#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_07_python2字符串.py
    @Description    :  
    @CreateTime     :  2020-03-16 15:55
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

# 引号前面的 u 告诉解释器，这个是一个utf8编码格式的字符串
hello_str = u"hello世界"

print(hello_str)

for c in hello_str:
    print(c)
