#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_15_字符串统计操作.py
    @Description    :  
    @CreateTime     :  2020/3/1 8:06 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
hello_str = "hello hello"

# 1. 统计字符串长度
print(len(hello_str))


# 2. 统计某一个小 (子) 字符串出现的次数
print(hello_str.count("hello"))
print(hello_str.count("abc"))

# 3. 某一个子字符串出现的位置
print(hello_str.index("llo"))
# 注意：如果使用index 方法传递的子字符串不存在，程序会报错！
# print(hello_str.index("abc"))
