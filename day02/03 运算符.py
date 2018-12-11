# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

#



'''
算数运算: + - * / % ** //
'''
# a = 10
# b = 3
# print(a % b)

# print(2**2)

# print(a // b)

# 比较计算: == != > < >= <=
# print(3 != 2)

'''
赋值运算: += -= *= /= %= **= //=
'''

'''
逻辑运算: not and or
优先级:() > not > and > or : 同一优先级,从左到右依次计算
'''
# 1. 逻辑运算两边都是比较
# print(3 > 2 and 3 < 4 or 5 > 6 and 2 < 5)  # 返回True
# print( True or True)

# 2. 逻辑运算两边都是数值
# X or y, if x is True , return x , else return y.
# X or y, if x is True , return y , else return x.
# 1 True
# 0 False

# print(1 or 3)

# int 与 bool 转换
# int ---> bool:  非零即True.
# print(bool(100))

# bool ---> int
# print(int(True))
# print(int(False))

# 3. 逻辑运算两边是数值或者比较
# print(1 and 3 or 4 < 6)  # 返回3
# print(1 and 4 < 6 or 4)  # 返回True


'''
成员运算: 判断某些元素在不在一个序列中 str  tuple  list  dict set
'''
# in   not in
# s1 = 'ab'
# s2 = 'abdfasdfasdfsadfvasde'
# print(s1 in s2)

# conment = input('>>>')
# s1 = 'TMD'

