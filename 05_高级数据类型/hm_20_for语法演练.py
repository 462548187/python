#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_20_for语法演练.py
    @Description    :  
    @CreateTime     :  2020/3/2 2:47 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
for num in [1, 2, 3]:

    print(num)

    if num == 2:
        break

else:
    # 如果循环体内部使用 break 退出了循环
    # else 下方的代码就不会被执行
    print("会执行吗？")

print("循环结束")

