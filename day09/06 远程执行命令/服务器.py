# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
import socket
import subprocess  # 远程执行模块

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 使用socker网络通信，默认使用TCP
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)  # 避免出现OSError
phone.bind(('127.0.0.1', 8080))  # 定义服务器的IP及端口
phone.listen(5)  # 并发5个
print('server is start')

while 1:  # 链接循环
    conn, addr = phone.accept()  # 等待阻塞状态
    print('这是:', addr)

    while 1:  # 通讯循环
        try:
            client_data = conn.recv(1024)  # 接收客户端输入的命令
            obj = subprocess.Popen(client_data.decode('utf-8'),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            ret = obj.stdout.read()
            ret1 = obj.stderr.read()

            conn.send(ret + ret1)
        except Exception:
            break
    conn.close()

phone.close()
