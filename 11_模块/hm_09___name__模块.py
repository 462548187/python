#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_09___name__模块.py
    @Description    :  
    @CreateTime     :  2020/3/15 5:19 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

# 全局变量、函数、类，注意：直接执行的代码不是向外界提供的工具


def say_hello():
    print("您好您好，我是 say hello")


# 如果直接执行模块， __main__
if __name__ == "__main__":
    print(__name__)

    # 文件被导入时，能够直接执行的代码不需要被执行
    print("小明开发的模块")
    say_hello()
