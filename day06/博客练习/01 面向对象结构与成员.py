# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
'''
面向对象结构分析
'''
# class A:
#     compy_name = '老男孩教育'  # 静态变量(静态字段)
#     __iphone = '135333xxx'  # 私有静态变量(私有静态字段)
#
#     def __init__(self, name, age):  # 特殊方法
#         self.name = name  # 对象属性(普通字段)
#         self.__age = age  # 私有对象属性(私有普通字段)
#
#     def func1(self):  # 普通方法
#         pass
#
#     def __func(self):  # 私有方法
#         print(666)
#
#     @classmethod  # 类方法
#     def class_func(cls):
#         '''定义类方法, 至少有一个cls参数'''
#         print('类方法')
#
#     @staticmethod  # 静态方法
#     def static_func():
#         '''定义静态方法, 无默认参数'''
#         print('静态方法')
#
#     @property  # 属性
#     def prop(self):
#         pass
#
'''
面向对象的私有与公有
'''

# 对于每一个类的成员而言都有两种形式:
# 公有成员: 在任何地方都能访问
# 私有成员: 只有在类的内部才能访问


'''
私有成员和公有成员的访问限制不同
# 静态字段(静态变量)
'''
# 公有静态字段: 类可以访问, 类内部可以访问, 派生类中可以访问
# class C:
#     name = '公有静态字段'
#     def func(self):
#         print(C.name)
#
# class D(C):
#     def show(self):
#         print(C.name)
#
# print(C.name)  # 类访问
#
# obj = C()
# obj.func()  # 类内部可以访问
#
# obj_son = D()
# obj_son.show()  # 派生类中可以访问


# 私有静态字段: 仅类内部可以访问
# class C:
#     __name = '私有静态字段'
#
#     def func(self):
#         print(C.__name)
# class D(C):
#     def show(self):
#         # print(C.__name)
#         pass
#
# # C.__name  # 不可在外部访问
#
# obj = C()
# # obj.__name()  # 不可在外部访问
# obj.func()  # 类内部可以访问
#
# obj_son = D()
# # obj_son.show()  # 不可在派生类中访问

'''
普通字段(对象属性)
'''
# 公有普通字段: 对象可以访问, 类内部可以访问, 派生类中可以访问
# class C:
#     def __init__(self):
#         self.foo = '公有字段'
#
#     def func(self):
#         print(self.foo)  # 类内部访问
#
# class D(C):
#     def show(self):
#         print(self.foo)  # 派生类中访问
#
# obj = C()
#
# # obj.foo  # 通过对象访问?
# obj.func()  # 类内部访问
#
# obj_son = D()
# obj_son.show()  # 派生类中访问


# 私有普通字段: 仅类内部可以访问
# class C:
#     def __init__(self):
#         self.__foo = '私有字段'
#
#     def func(self):
#         print(self.__foo)  # 类内部访问
#
# class D(C):
#     def show(self):
#         print(self.__foo)  # 派生类中访问
#
# obj = C()
#
# # obj.__foo  # 通过对象访问  错误的方式
# obj.func()  # 类内部访问  正确的方式
#
# obj_son = D()
# # obj_son.show()  # 派生类中访问  错误的方式

'''
方法
'''
# 公有方法: 对象可以访问, 类内部可以访问, 派生类中可以访问
# class C:
#     def __init__(self):
#         pass
#
#     def add(self):
#         print('in C')
# class D(C):
#     def show(self):
#         print('in D')
#
#     def func(self):
#         self.show()
#
# obj = D()
# obj.show()  # 通过对象访问
# obj.func()  # 类内部访问
# obj.add()   # 派生类中访问


# 私有方法: 仅类内部可以访问
# class C:
#     def __init__(self):
#         pass
#
#     def __add(self):
#         print('in C')
# class D(C):
#     def __show(self):
#         print('in D')
#
#     def func(self):
#         self.__show()
#
# obj = D()
# # obj.__show()  # 不能通过对象访问
# obj.func()  # 类内部可以访问
# # obj.__add()  # 派生类中不能访问

'''
对于这些私有成员来说, 他们只能在类的内部使用,不能在类的外部以及派生类中使用
'''


'''
面向对象的成员
字段
'''
# 字段包括: 普通字段和静态字段, 他们定义和使用中有所区别, 而最本质的区别是,内存中保存的位置不同,
# 动态字段属于 对象
# 静态字段属于 类

# class Province:
#     country = '中国'  # 静态字段
#
#     def __init__(self, name):
#         self.name = name  # 普通字段
#
# # 直接访问普通字段
# obj = Province('河北省')
# print(obj.name)
#
# # 直接访问静态字段
# print(Province.country)

