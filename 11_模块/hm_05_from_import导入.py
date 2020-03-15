#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_05_from_import导入.py
    @Description    :  
    @CreateTime     :  2020/3/15 4:10 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


from hm_01_测试模块1 import Dog
from hm_02_测试模块2 import say_hello

say_hello()

wangcai = Dog()
print(wangcai)
