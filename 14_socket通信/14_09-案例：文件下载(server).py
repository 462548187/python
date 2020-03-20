#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  14_09-案例：文件下载(server).py
    @Description    :  
    @CreateTime     :  2020-03-19 23:17
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
import socket


def send_file_2_client(new_client_socket, client_addr):
    # 1. 接收客户端 需要下载的文件名
    # 接收客户端发送过来的 需要下载的文件名
    file_name = new_client_socket.recv(1024).decode("gbk")
    print("客户端（%s）需要下载文件是：%s" % (str(client_addr), file_name))

    # 2. 打开这个文件，读取数据
    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件(%s)" % file_name)

    # 3. 发送文件的数据给客户端
    if file_content:
        # new_client_socket.send("success".encode("gbk"))
        new_client_socket.send(file_content)


def main():
    # 1. 创建套接字 socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定本地信息 bind
    tcp_server_socket.bind(("", 7890))

    # 3. 让默认的套接字由主动变为被动 listen
    tcp_server_socket.listen(128)
    while True:
        # 4. 等待客户端的链接 accept
        new_client_socket, client_addr = tcp_server_socket.accept()

        # 5. 调用发送文件函数，完成为客户端服务
        send_file_2_client(new_client_socket, client_addr)

        # 6. 关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()




if __name__ == '__main__':
    main()
