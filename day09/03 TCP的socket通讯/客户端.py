# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

'''
基于网络传输数据只能通过bytes类型
'''

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 买电话

phone.connect(('127.0.0.1', 8080))  # 拨号

msg = input('>>>').strip()

phone.send(msg.encode('utf-8'))
server_data = phone.recv(1024)  # 限制的是每次最大接收字节数
print(server_data.decode('utf-8'))

phone.close()
