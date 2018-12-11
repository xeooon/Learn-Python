# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
import socket
import struct
import json

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 买电话

phone.connect(('127.0.0.1', 8080))  # 拨号

while 1:
    msg = input('>>>').strip()
    if not msg : continue
    if msg.upper() == 'Q': break
    phone.send(msg.encode('utf-8'))

    # 1.接收字典的大小
    dict_size =  struct.unpack('i', phone.recv(4))[0]

    # 2.获取报头字典的json格式
    header_dict_json = phone.recv(dict_size).decode('utf-8')

    # 3.通过json反解成字典
    header_dict = json.loads(header_dict_json)

    # 4.接收数据部分
    data_size = 0
    res = b''
    while data_size < header_dict['total_size']:
        data = phone.recv(1024)
        res = res + data
        data_size = data_size + len(data)

    print(res.decode('utf-8'))

phone.close()
