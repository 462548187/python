#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  01_没有多任务的程序.py
    @Description    :  
    @CreateTime     :  2020-03-20 11:17
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
import time


def sing():
    """ 唱歌 5 秒钟 """
    for i in range(5):

        print("--- 正在唱：菊花台 ---")
        time.sleep(1)


def dance():
    """ 跳舞 5 秒钟 """
    for i in range(5):

        print("--- 正在跳舞 ---")
        time.sleep(1)


def main():

    sing()
    dance()


if __name__ == '__main__':
    main()
