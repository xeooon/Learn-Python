# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
'''
bmi看起来是一个名词,但是你用了一个方法去实现.
property（）:将方法伪装成名词,虽然在代码层面上没有提升,但是他会让你的代码看起来更合理.
'''
# 计算BMI指数, 输入姓名，体重kg， 身高m
# class B:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     @property
#     def bmi(self):
#         return self.weight / self.height ** 2
#
# a1 = B('张三', 70, 1.67)
# print(a1.bmi)


'''
对伪装属性进行改值时就会调用
'''
# class Foo:
#     def __init__(self, name):
#         self.name = name
#
#     @property  # ***
#     def AAA(self):
#         print('get 的时候运行我')
#
#     @AAA.setter  # *
#     def AAA(self, value):
#         print('set的时候运行我')
#
#     @AAA.deleter  # *
#     def AAA(self):
#         print('delete的时候运行我')

# obj = Foo('alex')
# obj.AAA = 666  # 对伪装属性进行改值时就会调用 def AAA(self, value)
# del obj.AAA  # 返回 delete的时候运行我

# obj = Foo('alex')
# obj.name = '太白'
# print(obj.name)


'''
定义一个类为计算苹果的真实价格
首先苹果的原始价格为8元， 折扣价格为0.8
如果改变价格原始价格，则折扣价格不变
'''
# class Product:
#     def __init__(self, name, origin_price, discount):
#         self.name = name
#         self.__origin_price = origin_price  # 私有动态属性
#         self.__discount = discount  # 私有动态属性
#
#     @property  # 方法封装为名词
#     def price(self):
#         return self.__origin_price * self.__discount
#
#     @price.setter  # 可以对原有类内容修改
#     def price(self, new_price):
#         self.__origin_price = new_price
#
# apple = Product('苹果', 8, 0.8)
# print(apple.price)  # 返回 6.4
#
# apple.price = 7  # 修改原始价格
# print(apple.price)  # 返回 5.6
