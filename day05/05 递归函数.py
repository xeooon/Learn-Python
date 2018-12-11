# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

'''
递归函数: 自己用自己.
'''

# 默认递归次数: 999或998
# 保护内存



# 设置递归次数为100次,太多影响效率
# import sys
# sys.setrecursionlimit(100)
# def func(x):
#     print(x)
#     x += 1
#     func(x)
# func(1)


# 某些情况下特别好使:
'''
alex 36  比wusir 大两岁   n = 4
wusir 34  比日天大两岁    n = 3
日天  32 比太白大两岁     n = 2
太白金星 30              n = 1
'''

# def age(n):
#     if n == 1:
#         return 30
#     elif n > 1:
#         return age(n - 1) + 2
# print(age(4))  # 返回 36



# 递归
# 一定要有返回值(返回值基本都是函数的调用)
# 斐波那契数列
# 1 1 2 3 5 8 13 21

#
# x, y = 0, 1
# while x < 100:
#     print(x)
#     x, y = y, x + y







