# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# import socket
# import subprocess
#
# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
# phone.bind(('127.0.0.1', 8080))
#
# phone.listen(5)
# conn, addr = phone.accept()
# while 1:
#     try:
#         cmd = conn.recv(1024)
#         obj = subprocess.Popen(cmd.decode('utf-8'),
#                                shell=True,
#                                stdout=subprocess.PIPE,
#                                stderr=subprocess.PIPE,
#                                )
#
#         ret = obj.stdout.read()
#         ret1 = obj.stderr.read()
#
#         total_size = len(ret+ret1)
#         print(total_size)
#         conn.send(ret + ret1)
#     except Exception:
#         break
#
# conn.close()
# phone.close()



'''
# 1，流式协议。数据全部都像水一样，连在一起。 
# 一次性发送 1519个字节（全部在客户端操作系统的缓存区）但是客户端一次只取1024字节，所以缓存区还剩495字节，下次再取。
'''
# 粘包现象一。
# import socket
# import subprocess
# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# phone.bind(('127.0.0.1', 8080))
#
# phone.listen(5)
# conn, addr = phone.accept()
# while 1:
#     try:
#         cmd = conn.recv(1024)
#         obj = subprocess.Popen(cmd.decode('utf-8'),
#                                shell=True,
#                                stdout=subprocess.PIPE,
#                                stderr=subprocess.PIPE,
#                                )
#
#         ret = obj.stdout.read()
#         ret1 = obj.stderr.read()
#
#         total_size = len(ret + ret1)
#         print(total_size)  # int 1519 100000  str '1519'  bytes
#         conn.send(total_size + ret + ret1)
#     except Exception:
#         break
#
# conn.close()
# phone.close()


'''
2，针对于(客户端/服务端)发送的连续的小的数据，对方会一次性接收。
'''
# import socket
#
# so1 = socket.socket()
# so1.bind(('127.0.0.1', 8888))
# so1.listen(5)
#
# conn, addr = so1.accept()
#
# client_data1 = conn.recv(5)
# print('data1',client_data1.decode('utf-8'))
# client_data2 = conn.recv(5)
# print('data2',client_data2.decode('utf-8'))
# conn.send(client_data1)
# conn.close()
# so1.close()


# 循环接收
# import socket
#
# so1 = socket.socket()
# so1.bind(('127.0.0.1', 8888))
# so1.listen(5)
#
# conn, addr = so1.accept()
#
# client_data1 = conn.recv(5)
# client_data2 = conn.recv(5)
# client_data3 = conn.recv(5)
# client_data4 = conn.recv(5)
# print(client_data1,client_data2,client_data3,client_data4)
# conn.send(client_data1)
# conn.close()
# so1.close()