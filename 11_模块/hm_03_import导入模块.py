#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_03_import导入模块.py
    @Description    :  
    @CreateTime     :  2020/3/14 11:13 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

import hm_01_测试模块1
import hm_02_测试模块2

hm_01_测试模块1.say_hello()
hm_02_测试模块2.say_hello()

dog = hm_01_测试模块1.Dog()
print(dog)

cat = hm_02_测试模块2.Cat()
print(cat)
