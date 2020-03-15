#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_05_复制文件.py
    @Description    :  
    @CreateTime     :  2020/3/15 8:07 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

# 1. 打开
file_read = open("README")
file_write = open("README[复制]", "w")

# 2. 读、写
text = file_read.read()
file_write.write(text)

# 3. 关闭
file_read.close()
file_write.close()

