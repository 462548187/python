#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_06_from_import注意事项.py
    @Description    :  
    @CreateTime     :  2020/3/15 4:16 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


# from hm_01_测试模块1 import say_hello
from hm_02_测试模块2 import say_hello as module2_say_hello
from hm_01_测试模块1 import say_hello

say_hello()
module2_say_hello()