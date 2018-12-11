# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

'''
基于网络传输数据只能通过bytes类型
'''

import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 买电话，默认是网络传输，TCP协议
phone.bind(('127.0.0.1', 8080))  # 买电话卡

phone.listen(5)  # 同一时刻只能监听5个请求

conn, addr = phone.accept()  # 等待电话，阻塞状态
print('这是:', addr)

client_data = conn.recv(1024)  # 限制的是每次最大接收字节数
print(client_data)
conn.send(client_data.upper())

conn.close()
phone.close()
