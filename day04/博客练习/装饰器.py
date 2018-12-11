# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

'''
什么是装饰器
'''

# 装饰器本质上就是一个python函数，他可以让其他函数在不需要做任何代码变动的前提下，
# 增加额外的功能，装饰器的返回值也是一个函数对象。
# 装饰器的应用场景：比如插入日志，性能测试，事务处理，缓存等等场景。



'''
装饰器的形成过程
'''

# import time
# def func1():
#     print('in func1')
#
# def timer(func):
#     def inner():
#         start = time.time()
#         func()
#         print(time.time() - start)
#     return inner
# func1 = timer(func1)
# func1()

# import time
# def timer(func):
#     def inner():
#         start = time.time()
#         func()
#         print(time.time() - start)
#     return inner
# @timer  #==> func1 = timer(func1)
# def func1():
#     print('in func1')
#
# func1


def timer(func):
    def inner(a):
        start = time.time()
