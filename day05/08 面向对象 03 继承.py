# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

'''
继承: 1.节省代码 2.提高效率 3.让类之间产生关联
'''
# class Animal:  # 父类
#     def __init__(self, kind, age, sex):
#         self.kind = kind
#         self.age = age
#         self.sex = sex
#
# class Person(Animal):  # 子类
#     pass
# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass
#
# p1 = Person('黄种人', 25, '男')
# p2 = Dog('藏獒', 3, '公')
# p3 = Cat('虎斑', 2, '母')
#
# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)

# Animal : 父类, 基类
# Person : 子类, 派生类


'''
继承: 单继承, 多继承
# 类:
#   经典类: 不继承object的类
#       python2.x:经典类 和新式类(object) 共存
#
# 新式类(查询效率高)
#     python3.x 默认继承object,全部是新式类
'''


'''
# 单继承
# 类名 一般不调用方法
'''

# class Animal:
#     a1 = '太白'
#     def __init__(self, kind, age, sex):
#         self.kind = kind
#         self.age = age
#         self.sex = sex
#
#     def func1(self):
#         print(666)
# class Person(Animal):
#     pass

# 类名调用静态属性
# print(Person.a1)

'''
# 子类有自己的属性,我如何既要执行父类方法,又要执行子类方法

# bark 叫
# bite 咬
'''
class Animal:
    def __init__(self, kind, age, sex):
        self.kind = kind
        self.age = age
        self.sex = sex

    def bark(self):
        print('动物都会叫')

class Dog(Animal):  # 父类
    def __init__(self, name1, age1, sex1, bite):
        super().__init__(name1, age1, sex1)  # 自动将self传给父类Animal的self
        self.bite = bite

    def bark(self):  # 狗的动态属性
        super().bark()
        print('汪汪汪')

d1 = Dog('藏獒', 3, '公', 300)
d1.bark()

# 两种方式解决,既要执行子类的方法,又要执行父类的方法
# 第一种  Animal.__init__(self, name1, age1, sex1)  # 直接调用另一个类的方法
# 第二种：super().__init__(name1, age1, sex1)  # 自动将self传给父类的self


'''
多继承
# 新式类: c3算法 mro 主要是查询 新式类的多继承的继承顺序
'''
# class A:
#     def func(self):
#         print(666)
#     pass
#
# class B:
#     def func(self):
#         print(777)
#     pass
#
# class C(A):
#     def func(self):
#         print(888)
#     pass
#
# class D(B):
#     def func(self):
#         print(999)
#     pass
#
# class E(C, D):
#     pass
#
# e1 = E()
# e1.func()
# print(E.mro())






