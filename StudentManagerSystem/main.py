#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  main.py.py
    @Description    :  
    @CreateTime     :  2020/4/5 1:12 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
# 1. 导入管理系统模块
from mangerSystem import *

# 2. 启动管理系统
# 保证是当前文件运行才启动管理系统：if -- 创建对象并调用run方法
if __name__ == '__main__':
    student_manager = StudentManager()
    student_manager.run()
