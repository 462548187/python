#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  02_发送任意数据给Windows中调试助手.py
    @Description    :  
    @CreateTime     :  2020-03-18 18:32
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

import socket


def main():

    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 从键盘获取数据
    send_data = input("请输入要发送的数据:")

    # 可以使用套接字收发数据
    # udp_socket.sendto("哈哈", 对方的ip以及port)
    udp_socket.sendto(send_data.encode("utf-8"), ("10.67.12.66", 8080))

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':

    main()
