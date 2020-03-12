#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_17_字符串的查找和替换.py
    @Description    :  
    @CreateTime     :  2020/3/2 12:10 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

hello_str = "hello word"

# 1. 判断是否以指定字符串开始
print(hello_str.startswith("hello"))


# 2. 判断是否以指定字符串结束
print(hello_str.endswith("word"))


# 3. 查找指定字符串
# index 同样可以查找指定的字符串在大字符串中的索引
print(hello_str.find("llo"))
print(hello_str.index("llo"))

# index 如果指定的字符串不存在，会报错
# find 如果指定的字符串不存在，会返回 -1
print(hello_str.find("abc"))
# print(hello_str.index("abc"))


# 4. 替换字符串
# replace 方法执行完成之后，会返回一个新的字符串
# 注意： 不会修改原有字符串的内容
print(hello_str.replace("word", "Python"))

print(hello_str)
