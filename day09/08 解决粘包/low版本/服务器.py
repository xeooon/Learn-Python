# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
import socket
import subprocess  # 远程执行模块
import struct

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

            # 1.获取执行命令返回的结果
            ret = obj.stdout.read()
            ret1 = obj.stderr.read()

            # 2.计算head（总数据）大小
            total_size = len(ret + ret1)
            print(total_size)

            # 3.将head转换成固定长度的bytes
            head = struct.pack('i', total_size)

            # 4.发送head
            conn.send(head)

            # 5.发送数据部分
            conn.send(ret)
            conn.send(ret1)

        except Exception:
            break
    conn.close()

phone.close()
