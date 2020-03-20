#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  06_线程共享全局变量.py
    @Description    :  
    @CreateTime     :  2020-03-20 16:21
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


num = 100
nums = [11, 22]


def test():
    global num
    num += 100


def test2():
    nums.append(33)


print(num)
print(nums)

test()
test2()

print(num)
print(nums)
