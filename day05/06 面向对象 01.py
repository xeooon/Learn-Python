# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# 函数: 一个函数是封装一个功能

# 员工信息表
# def add():
#     pass
#
# def pop():
#     pass
#
# def update():
#     pass
#
# def select():
#     pass


# 相同功能的函数进行归类
#  面向对象的特点:
# 1. 它是将某些相关的功能(函数),封装到了一起
# 2. 你要站在上帝的角度, 创建一个公共模版,然后通过模版创造不同的对象.
# 类: 具有相同属性和技能的一类事物.
# 对象: 类的具体表现

# 猫 是一类, 隔壁老奶奶家养的 阿花.
# 狗 是一类, 我们家养的一条哈士奇.

# 结构分析 : 类一般就分为两部分: 变量和方法
# 思想层面 : 创建一个类, 公共模板, 通过创建个体对象,可以享有公共方法

# class Person:
#     mind = '有思想'  # 静态属性,静态变量,静态字段
#     animal = '高级动物'
#     language = '文字语言'
#
#     def work(self):  # 函数,方法,动态方法,动态属性
#         print('人类都会工作')
#     def eat(self):
#         print('人类都需要吃饭')


'''
类名调用静态属性
'''
# 类名调用静态属性
# 方法1: __dict__  只能查询(不能增删改) 类中所有的静态属性,动态方法.
# print(Person.__dict__)

# 方法2: 万能的点 .   可查,可改,可增,可删
# print(Person.mind)  # 查出了有思想
#
# Person.mind = '有灵魂'
# print(Person.__dict__)  # 有思想改为了有灵魂
#
# Person.fuse = '黄色'
# print(Person.__dict__)  # 末尾增加了黄色
#
# del Person.mind
# print(Person.__dict__)  # 删除了mind

# 类名执行动态方法(一般不建议用类名执行,除非是特殊方法:类方法,静态方法)
# Person.work('xeon')  # 不推荐


'''
对象的深入研究
# 实例化对象的过程有几步:
# 1.实例化对象在内存中产生一个对象空间(内存地址)
# 2.自动执行__init__方法,并且将对象空间(内存地址)传给self参数
# 3.在__init__方法中,给对象空间封装一些静态属性
'''
# 类名+() 就是一个实例化对象的过程,内存会新开辟一个空间

# p1 = Person()  # 实例对象
# p2 = Person()  # 实例对象
# print(p1, p2)


# class Game_Role:  # 类
#     a1 = '英雄联盟'  # 静态属性
#     name = '太白'
#     def __init__(self, name, sex, ad, hp):  # __init__ 方法, 特殊方法,给对象封装属性
#         self.name = name  # 对象属性
#         self.sex = sex
#         self.ad = ad
#         self.hp = hp
#
#     def fight(self):
#         pass
#
#     def work(self):
#         self.hobby = '大刀'
#         print(self.__dict__)
#
# gailun = Game_Role('盖伦', 'man', '30', '500')  # 对象


'''
对象调用类的静态属性
'''
# 对象调用类的静态属性
# 万能的点, 可以调用类中的静态属性
# print(gailun.a1)

# 对象执行类中的方法:
# print(gailun.name)

# self: 约定俗成 self, 类中的方法的第一个参数,要设定为self,python在对象调用方法时,会自动将对象空间传给self
# self是对象本身

# 在工作中: 类中的静态属性,一般通过类名去调用或者改变.
#          类中的动态方法一般通过对象去执行


# 对象查看自己空间的属性
# 查看全部: __dict__
# 查看某个对象自己的静态属性：万能的点 . 增删改查都可以
# print(gailun.name)


'''
特殊的类属性
'''
# 类名.__name__# 类的名字(字符串)
# 类名.__doc__# 类的文档字符串
# 类名.__base__# 类的第一个父类(在讲继承时会讲)
# 类名.__bases__# 类所有父类构成的元组(在讲继承时会讲)
# 类名.__dict__# 类的字典属性
# 类名.__module__# 类定义所在的模块
# 类名.__class__# 实例对应的类(仅新式类中)