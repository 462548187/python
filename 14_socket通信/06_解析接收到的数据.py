#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  06_解析接收到的数据.py
    @Description    :  
    @CreateTime     :  2020-03-18 21:38
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

import socket


def main():

    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定一个本地信息
    local_addr = ("", 7788)  # 必须绑定自己电脑的ip以及port，其他的不行
    udp_socket.bind(local_addr)

    # 3. 接收数据
    recv_data = udp_socket.recvfrom(1024)

    # recv_data 这个变量中存储的是一个元组（接收到说的数据，（发送方的iP，port））
    recv_msg = recv_data[0]  # 存储接收到的数据
    send_addr = recv_data[1]  # 存储发送方的地址信息

    # 4. 打印接收到的数据
    # print("%s:%s" % (str(send_addr), recv_msg.decode("utf-8")))
    print("%s:%s" % (str(send_addr), recv_msg.decode("gbk")))  # windows 系统

    # 5. 关闭套接字
    udp_socket.close()


if __name__ == '__main__':

    main()
