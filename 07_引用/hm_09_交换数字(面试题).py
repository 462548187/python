#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_09_交换数字(面试题).py
    @Description    :  
    @CreateTime     :  2020/3/4 6:45 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

a = 6
b = 100

# 解法1： - 使用其他变量
# c = a
# a = b
# b = c

# 解法2：- 不使用其他变量
# a = a + b
# b = a - b
# a = a - b

# 解法3： - Python 专有
# a, b = (b, a)
# 提示：等号右边是一个元组，只是把小括号省略了
a, b = b, a

print(a)
print(b)
