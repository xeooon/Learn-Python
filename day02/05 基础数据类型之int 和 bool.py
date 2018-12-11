# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# int 和 bool

# int:


# bit_length() : 计算十进制转换成二进制的有效位数
'''
十进制         二进制
1               0000 0001
3               0000 0011
6               0000 0110
'''
# i = 10
# i1 = 6
# print(i.bit_length())
# print(i1.bit_length())

# bool
# True False

# str ----> bool  非空即True
# s1 = 'alex'
# print(bool(s1))  # 返回 True
# s2 = ' '
# print(bool(s2))  # 返回 True
# s3 = ''
# print(bool(s3))  # 返回 False

# bool ----> str
# print(str(True),type(str(True)))