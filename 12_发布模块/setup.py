#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  setup.py
    @Description    :  
    @CreateTime     :  2020/3/15 6:05 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

from distutils.core import setup

setup(name="hm_message",  # 包名
      version="1.0",  # 版本
      description="sandy's 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="sandy",  # 作者
      author_email="462548187@qq.com",  # 作者邮箱
      url="www.baidu.com",  # 主页
      py_modules=["hm_message.send_message",
                  "hm_message.receive_message"])
