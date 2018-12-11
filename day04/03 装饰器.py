# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

'''
需求:在生产环境测试函数的真正的执行效率(函数执行消耗的时间)
1.不能重复造轮子
2.线上的函数你不能改变
3.函数的原本调用方式不能改变
'''

# 方法1:被装饰函数带参数
import time
def timmer(f):  # f = func1(a)
    def inner(*args, **kwargs):  # args = alex , kwargs = {}
        start_time = time.time()
        # 执行被装饰的函数之前的操作
        f(*args, **kwargs)  # ret = func1(alex)
        # 执行被装饰的函数之后的操作
        end_tiime = time.time()
        print('此函数执行所消耗的时间为%s' % (end_tiime - start_time))
    return inner

@timmer  # func1(a) = timmer(func1(a))
def func1(a):
    time.sleep(0.2)
    print('来了老弟,%s' % a)
    return 666
print(func1('alex'))  # print(inner('alex'))


# 方法2:被装饰函数有返回值
# import time
# def timmer(f):  # f = func1(a)
#     def inner(*args, **kwargs):  # args = alex , kwargs = {}
#         start_time = time.time()
#         # 执行被装饰的函数之前的操作
#         ret = f(*args, **kwargs)  # ret = func1(alex)
#         # 执行被装饰的函数之后的操作
#         end_tiime = time.time()
#         print('此函数执行所消耗的时间为%s' % (end_tiime - start_time))
#         return ret
#     return inner
#
# @timmer  # func1(a) = timmer(func1(a))
# def func1(a):
#     time.sleep(0.2)
#     print('来了老弟,%s' % a)
#     return 666
# print(func1('alex'))  # print(inner('alex'))


'''
装饰器,本质其实是闭包, 闭包最大的应用就是装饰器.
装饰器在不改变原函数的内部函数体以及调用方式的前提下,给函数增加了额外的功能,
登录认证,登录注册,打印日志,函数效率.
'''
# 装饰器格式如下
# def wrapper(f):
#     def inner(*args, **kwargs):
#         # 执行被装饰函数之前的操作
#         ret = f(*args, **kwargs)
#         # 执行被装饰函数之后的操作
#         return ret
#     return inner
#
# @wrapper
# def func1():
#     pass
# func1()
