#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  02_多任务-线程-demo.py
    @Description    :  
    @CreateTime     :  2020-03-20 11:17
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
import time
import threading


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

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
