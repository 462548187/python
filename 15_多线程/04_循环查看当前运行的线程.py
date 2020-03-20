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

    # 如果创建Thread时执行的函数，运行结束那么意味着，这个子线程结束了...


def test2():
    for i in range(10):
        print("----- test2 ----- %d" % i)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()

    while True:
        print(threading.enumerate())

        if len(threading.enumerate()) <=1:
            break
        time.sleep(1)


if __name__ == '__main__':
    main()
