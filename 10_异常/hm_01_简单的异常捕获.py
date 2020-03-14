#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_01_简单的异常捕获.py
    @Description    :  
    @CreateTime     :  2020/3/14 9:33 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


try:
    # 不能确定正确的执行的代码
    num = int(input("请输入一个整数："))

except:
    # 错误的处理代码
    print("请输入正确的整数")

print("-" * 50)
