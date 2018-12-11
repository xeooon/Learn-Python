# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
import socket
import struct

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 买电话

phone.connect(('127.0.0.1', 8080))  # 拨号

while 1:
    msg = input('>>>').strip()
    if not msg : continue
    if msg.upper() == 'Q': break
    phone.send(msg.encode('utf-8'))

    # 1.接收报头
    header_bytes = phone.recv(4)

    # 2.反解报头
    total_size = struct.unpack('i', header_bytes)[0]  # int

    # 3.接收数据部分
    data_size = 0
    res = b''
    while data_size < total_size:
        data = phone.recv(1024)
        res = res + data
        data_size = data_size + len(data)

    print(res.decode('utf-8'))

phone.close()
