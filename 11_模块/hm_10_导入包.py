#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_10_导入包.py
    @Description    :  
    @CreateTime     :  2020/3/15 5:57 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

import hm_message

hm_message.send_message.send("hello")
text = hm_message.receive_message.receive()
print(text)
