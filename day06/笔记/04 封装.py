# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""


'''
封装:
    类的三大特性: 继承, 封装, 多态
'''
# class A:
#     def __init__(self, name):
#         self.name = name
#
# obj = A('二狗')


# 广义的封装: 就是将一些内容放到一个'容器'中.
# 狭义的封装: 私有


'''
类的结构
'''
# class B:
#     country = 'China'  # 静态变量（属性，字段）
#     __name = 'alex'  # 私有静态变量
#
#     def func(self):  # 动态普通方法
#         pass
#
#     def __func(self):  # 私有方法
#         pass
#
#     def __init__(self, name, age):  # 特殊方法：双下方法
#         self.name = name
#         self.name = age
#
#     @property  # 属性
#     def f1(self):
#         pass
#
#     @classmethod  # 类方法
#     def func2(cls):
#         pass
#
#     @staticmethod  # 静态方法
#     def func3(self):
#         pass


# 私有成员：私有变量， 私有对象属性，私有方法
# 私有成员：类外面不可以访问，派生类（子类）不可以访问，类内里面可以访问
# class A:
#     country = 'China'  # 静态变量（属性，字段）
#     __name = 'alex'  # 私有静态变量
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age  # 私有动态方法
#
#     def func(self):  # 动态普通方法
#         print(self.__name)
#
#     def __func(self):  # 私有方法
#         pass
#
# class B(A):
#     def func2(self):
#         print(self.__name)

# obj = A('二狗', 18)
# print(obj.country)   # 返回 China， 类外面可以访问
# # print(obj.__name)  # 私有： 类外面不可以访问
#
# obj.func()  # 返回 China alex 私有，类内里面可以访问
#
# o1 = B('脸哥', 25)
# # o1.func2()  # 私有， 派生类（子类），不可以访问

# obj = A('王二麻子', 11)
# print(A.__dict__)  # 查看实例化对象A的所有属性
# print(obj._A__name)  # python里面没有觉对的私有属性，不推荐这么用，理解可以



#
# 派生类(子类)
# 私有成员(没有绝对的私有成员): 只有类的内部可以访问, 类外面, 派生类, 不能访问
#
# 类方法: 必须通过类的调用, 而且此方法的意义: 就是对类里面的变量或者方法进行修改或添加.
#
# 计算创建的对象的个数
#
# 静态方法: 就是一个不依赖类以及对象的一个普通函数, 为什么在类里面?
# 为了保证代码的一致性, 整洁性