#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  05_绑定端口用来接收数据.py
    @Description    :  
    @CreateTime     :  2020-03-18 21:20
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
import socket


def main():

    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定一个本地信息
    local_addr = ("", 7788)
    udp_socket.bind(local_addr)

    # 3. 接收数据
    recv_data = udp_socket.recvfrom(1024)

    # 4. 打印接收到的数据

    # 5. 关闭套接字


if __name__ == '__main__':

    main()
