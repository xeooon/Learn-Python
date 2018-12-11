# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
import socket
import subprocess  # 远程执行模块
import struct
import json

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

            # 1.获取执行命令返回的结果,计算结果的总大小
            ret = obj.stdout.read()
            ret1 = obj.stderr.read()
            total_size = len(ret + ret1)

            # 2.构建header字典
            head_dict = {'filename': '二狗',
                         'md5': 'asdfasd12345654',
                         'total_size': total_size}

            # 3.将字典转换成json格式
            dict_json = json.dumps(head_dict)

            # 4.将字典转换成bytes，只能通过bytes类型进行网络传输
            dict_bytes = dict_json.encode('utf-8')

            # 5.计算字典bytes类型的大小
            dict_len = len(dict_bytes)

            # 6.将bytes类型的 字典的长度，转化成固定长度的bytes
            head_dict_len = struct.pack('i', dict_len)

            # 7.发送字典的总大小
            conn.send(head_dict_len)

            # 8.发送bytes类型的字典
            conn.send(dict_bytes)

            # 9.发送数据部分
            conn.send(ret)
            conn.send(ret1)

        except Exception:
            break
conn.close()
phone.close()
