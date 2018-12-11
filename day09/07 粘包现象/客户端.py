# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# import socket
#
# phone = socket.socket()
#
# phone.connect(('127.0.0.1', 8080))
# while 1:
#     msg = input('>>>').strip()
#     if msg.upper() == 'Q': break
#     elif not msg: continue  # 解决的是输入为空程序会夯住的问题。
#     phone.send(msg.encode('utf-8'))
#     server_data = phone.recv(1024)
#     print(server_data.decode('gbk'))
# phone.close()


# 例子2
# 解决方式一 让连续数据变成不连续，不能这么做。
# import socket
# import time
# phone = socket.socket()
#
# phone.connect(('127.0.0.1', 8888))
#
# phone.send(b'hello')
# time.sleep(0.1)
# phone.send(b'world')
#
# print(phone.recv(1024).decode('utf-8'))
# phone.close()


# 解决方式2  限定获取的字节数等于发送的字节数，不行，写死了。
# import socket
# import time
# phone = socket.socket()
#
# phone.connect(('127.0.0.1', 8888))
#
# phone.send(b'hellohellohellohello')
# # phone.send(b'world')
#
# print(phone.recv(1024).decode('utf-8'))
# phone.close()