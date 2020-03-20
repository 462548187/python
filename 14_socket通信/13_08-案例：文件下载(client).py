#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  13_08-案例：文件下载(client).py
    @Description    :  
    @CreateTime     :  2020-03-19 22:55
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
import socket


def main():

    # 1. 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 获取服务器ip port
    dest_ip = input("请输入下载服务器的ip：")
    dest_port = int(input("请输入下载服务器的port："))

    # 3. 链接服务器
    tcp_socket.connect((dest_ip, dest_port))

    # 4. 获取下载文件名字
    download_file_name = input("请输入要下载的文件名字：")

    # 5. 将文件名字发送给服务器
    tcp_socket.send(download_file_name.encode("gbk"))

    # 6. 接收文件中的数据
    recv_data = tcp_socket.recv(1024)

    if recv_data:
        # 7. 保存接收的数据到一个文件中
        with open("[新]" + download_file_name, "wb") as f:
            f.write(recv_data)

    # 8. 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
