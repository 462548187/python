#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  01_socket的基本使用.py
    @Description    :  
    @CreateTime     :  2020-03-18 17:46
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

import socket


def main():

    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 可以使用套接字收发数据
    # udp_socket.sendto("哈哈", 对方的ip以及port)
    udp_socket.sendto(b"hahaha", ("10.67.12.66", 8080))

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':

    main()
