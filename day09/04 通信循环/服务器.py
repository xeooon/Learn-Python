# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 买电话

phone.bind(('127.0.0.1', 8080))  # 买电话卡
phone.listen(5)  # 并发5个

while 1:  # 链接循环
    conn, addr = phone.accept()  # 等待电话，阻塞状态
    print('这是:', addr)

    while 1:  # 通讯循环
        try:
            client_data = conn.recv(1024)  # 限制的是每次最大接收字节数
            conn.send(client_data + b'SB')
        except Exception:
            break
    conn.close()

phone.close()
