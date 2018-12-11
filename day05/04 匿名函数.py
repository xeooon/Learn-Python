# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

'''
匿名函数: 一句话函数, 一行代码实现的函数
'''

# lambda 形参,参数: 返回值
# func1 = lambda x, y: x + y
# print(func1(2, 3))  # 返回 5

# 下面这个函数不会执行
# def func(x, y, z):
#     return (x + y - z) * 2

# func2 = lambda x, y, z: (x + y - z) * 2
# print(func2(1, 5, 3))  # 返回6

# 匿名函数与内置函数相结合使用, 返回对2取余的数并排列
# l1 = [1, 2, 3, 4, 5, 6]
# obj1 = filter(lambda x: x % 2 == 0, l1)
# print(list(obj1))  # 返回 [2, 4, 6]


# 把字典当中value最大的返回
# dic = {'k1': 10, 'k2': 100, 'k3': 30}
# ret = dic[max(dic, key=lambda x: dic[x])]
# print(ret)
