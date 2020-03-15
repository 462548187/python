#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_04_import同时指定别名.py
    @Description    :  
    @CreateTime     :  2020/3/15 4:02 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


import hm_01_测试模块1 as DogModule
import hm_02_测试模块2 as CatModule

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
print(dog)

cat = CatModule.Cat()
print(cat)
