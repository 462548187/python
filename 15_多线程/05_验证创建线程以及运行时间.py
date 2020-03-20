#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  03_查看线程数-让某些线程先执行.py
    @Description    :  
    @CreateTime     :  2020-03-20 12:10
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
import threading
import time


def test1():
    for i in range(5):
        print("----- test1 ----- %d" % i)
        time.sleep(1)


def main():
    # 在调用Thread之前先打印当前线程信息
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)

    # 在调用Thread之后打印
    print(threading.enumerate())

    t1.start()

    # 在调用start之后打印
    print(threading.enumerate())


if __name__ == '__main__':
    main()
