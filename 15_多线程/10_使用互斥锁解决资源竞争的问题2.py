#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  10_使用互斥锁解决资源竞争的问题.py
    @Description    :  
    @CreateTime     :  2020-03-20 16:24
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
import threading
import time

g_num = 0


def test1(num):
    global g_num
    # 上锁，如果之前没有被上锁，那么此时 上锁成功
    # 如果上锁之前 已经被上锁了，那么此时会堵塞在这里，知道这个锁被解开为止

    for i in range(num):
        mutex.acquire()
        g_num += 1
        # 解锁
        mutex.release()
    print("------in test1 g_num = %d" % g_num)


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("------in test2 g_num = %d" % g_num)


# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test1, args=(10000000,))
    t2 = threading.Thread(target=test2, args=(10000000,))

    t1.start()
    t2.start()

    # 等待上面两个线程执行完毕
    time.sleep(2)

    print("---- in main Thread g_num = %d" % g_num)


if __name__ == '__main__':
    main()
