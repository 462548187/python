#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_06_复制大文件.py
    @Description    :  
    @CreateTime     :  2020/3/15 8:12 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

# 1. 打开
file_read = open("README")
file_write = open("README[复制]", "w")

# 2. 读、写
while True:
    # 读取一行内容
    text = file_read.readline()

    # 判断是否读取到内容
    if not text:
        break

    file_write.write(text)

# 3. 关闭
file_read.close()
file_write.close()

