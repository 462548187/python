#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  09_使用同一个套接字收发数据.py
    @Description    :  
    @CreateTime     :  2020-03-19 10:55
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
import socket


def send_msg(udp_socket):
    """ 发送消息 """

    # 获取对方的ip/port
    dest_ip = input("请输入对方的ip：")
    dest_port = int(input("请输入对方的port："))

    # 从键盘获取数据
    send_data = input("请输入要发送的数据:")

    # 可以使用套接字收发数据
    # udp_socket.sendto("哈哈", 对方的ip以及port)
    # udp_socket.sendto(send_data.encode("utf-8"), ("10.67.12.66", 8080))
    udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))  # Windows 使用gbk编码


def recv_msg(udp_socket):
    """ 接收数据 """

    # 接收回送过来的数据
    recv_data = udp_socket.recvfrom(1024)

    # 套接字是一个可以同时 收发数据
    print("%s:%s" % (recv_data[1], recv_data[0].decode("gbk")))


def main():

    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定信息
    udp_socket.bind(("", 7788))

    while True:
        print("----- XXX 聊天工具-----")
        print("1：发送消息")
        print("2：接收消息")
        print("0：退出消息")
        op = input("请输入功能：")

        if op == "1":
            send_msg(udp_socket)
        elif op == "2":
            recv_msg(udp_socket)
        elif op == "0":
            break
        else:
            print("输入有误，请重新输入")

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':

    main()


