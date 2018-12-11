# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
'''
# 类方法：必须通过类的调用
# 此方法的意义：就是对类里面的变量或者方法进行修改添加
'''
# class B:
#     country = 'China'  # 静态变量（属性，字段）
#
#     def func(self, name, age): # 特殊方法, 双下方法
#         self.name = name
#
#     @classmethod  # 类方法
#     def func2(cls):
#         cls.area = '东北'
#         cls.name = '狗哥'
#
# print(B)
# print(B.__dict__)
#
# B.func2()
# print(B.__dict__)  # B的类增加了func2的方法


'''
# 计算调用此函数的次数
'''
# class C:
#     count = 0
#
#     def __init__(self):
#         C.cou()
#
#     @classmethod
#     def cou(cls):
#         cls.count += 1
#
# obj = C()
# obj = C()
# obj = C()
# obj = C()
# obj = C()
# print(C.count)  # 返回5次


'''
静态方法： 就是一个不依赖类以及对象的一个普通函数，
为啥在类里面？ 为了保证代码的一致性，可调控性，整洁性
'''
# 例子1：
# class C:
#     def __init__(self):
#         pass
#
#     @staticmethod  # 静态方法
#     def func(*args, **kwargs):
#         print(666)
#
# C.func()
# c1 = C()
# c1.func()

# 例子2：时间测试
# import time
# class TimeTest(object):
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     @staticmethod  # 静态方法
#     def showTime():
#         return time.strftime('%H:%M:%S', time.localtime())
#
# print(TimeTest.showTime())
# t = TimeTest(2, 10, 10)
# nowTime = t.showTime()
# print(nowTime)