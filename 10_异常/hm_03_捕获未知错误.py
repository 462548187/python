#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_03_捕获未知错误.py
    @Description    :  
    @CreateTime     :  2020/3/14 9:56 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

try:
    # 提示用户输入一个整数
    num = int(input("输入一个整数："))

    # 使用 8 除以用户输入的整数并且输出
    result = 8 / num

    print(result)

except ValueError:
    print("请输入正确的整数")

except Exception as result:
    print("未知错误 %s" % result)
