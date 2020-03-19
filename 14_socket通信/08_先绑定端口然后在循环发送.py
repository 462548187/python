#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  08_先绑定端口然后在循环发送.py
    @Description    :  
    @CreateTime     :  2020-03-19 10:26
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


import socket


def main():

    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    udp_socket.bind(("", 2425))

    while True:
        # 从键盘获取数据
        send_data = input("请输入要发送的数据:")

        # 退出功能
        if send_data == "exit":
            break

        # 可以使用套接字收发数据
        # udp_socket.sendto("哈哈", 对方的ip以及port)
        # udp_socket.sendto(send_data.encode("utf-8"), ("10.67.12.66", 8080))
        udp_socket.sendto(send_data.encode("gbk"), ("10.67.12.66", 8080))  # Windows 使用gbk编码

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':

    main()

