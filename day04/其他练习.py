# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# def func():
#     def func2():
#         print(333)
#     return func2
# func()()


# def wrapper(s1):
#     n = 1
#     def inner():
#         nonlocal n
#         n += s1
#         print(n)
#     return inner
# ret = wrapper(5)
# ret()
# ret()
# ret()
# ret()

#
# import time
# def func1():
#     time.sleep(0.2)
#     print('来了,老弟')
#
# def timmer(f):
#     def inner():
#         start_time = time.time()
#         f()
#         end_tiime = time.time()
#         print('此函数执行的时间是%s' %(end_tiime - start_time))
#     return inner
# func1 = timmer(func1)
# func1()


# 被装饰函数带参数
# import time
# def timmer(f):  # f = func1(a)
#     def inner(*args, **kwargs):  # args = alex , kwargs = {}
#         start_time = time.time()
#         # 被执行函数之前
#         ret = f(*args, **kwargs)  # ret = func1(alex)
#         # 被执行函数之后
#         end_tiime = time.time()
#         print('此函数执行所消耗的时间为%s' % (end_tiime - start_time))
#         return ret
#     return inner
#
# @timmer  # func1 = timmer(func1(a))
# def func1(a):
#     time.sleep(0.2)
#     print('来了老弟,%s' % a)
#     return 666
# print(func1('alex'))




#
#


'''
列表推导式
'''

# 30以内所有能被3整除的数
# a = [i for i in range(30) if i % 3 is 0]
# print(a)
#



# 30以内所有能被3整除的数的平方
# 方法1
# a = [i**2 for i in range(30) if i % 3 == 0]
# print(a)

# 方法2
# def squared(x):
#     return x*x
# a = [squared(i) for i in range(30) if i % 3 is 0]
# print(a)



# 找到嵌套列表中名字含有两个‘e’的所有名字
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# print([name for last in names for name in last if name.count('e') >= 2])



'''
字典推导式
'''
# 将一个字典的key和value对调
# mcase = {'a': 10, 'b': 34}
# mcase_frequency = {mcase[k]: k for k in mcase}
# print(mcase_frequency)


# 合并大小写对应的value值，将k统一成小写
# mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys()}
# print(mcase_frequency)


'''
集合推导式
'''
# 计算列表中每个值的平方，自带去重功能
# squared = {x**2 for x in [1, -1, 2]}
# print(squared)

