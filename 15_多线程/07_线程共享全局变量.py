#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  07_线程共享全局变量.py
    @Description    :  
    @CreateTime     :  2020-03-20 16:24
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
import threading
import time

g_num = 100


def test1():
    global g_num
    g_num += 1
    print("------in test1 g_num = %d" % g_num)


def test2():
    print("------in test2 g_num = %d" % g_num)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("---- in main Thread g_num = %d" % g_num)


if __name__ == '__main__':
    main()
