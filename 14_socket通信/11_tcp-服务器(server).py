#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  11_tcp-服务器(server).py
    @Description    :  
    @CreateTime     :  2020-03-19 16:54
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
import socket


def main():

    # 1. 买个手机（创建套接字 socket）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 插入手机卡（绑定本地信息 bind）
    tcp_server_socket.bind(("", 7788))
    # 3. 将手机设置为正常的 响铃模式（让默认的套接字由主动变为被动 listen）
    tcp_server_socket.listen(128)

    while True:
        print("等待一个新的客户端的到来...")
        # 4. 等待别人的电话到来 (等待客户端的链接 accept)
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("一个新的客户端已经到来 %s" % str(client_addr))

        # 接收客户端发送的请求
        recv_data = new_client_socket.recv(1024)
        print("客户端发送的请求是 %s " % recv_data.decode("gbk"))

        # 回送一部分数据给客户端
        new_client_socket.send("---ok---".encode("gbk"))

        # 关闭套接字
        # 关闭 accept 返回的套接字，意味着，不会在为这个客户端服务
        new_client_socket.close()
        print("已经服务完毕...")

    # 如果将监听套接字 关闭了，那么会导致不能再次等待新客户端到来，即 XXX.accept 就会失败
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
