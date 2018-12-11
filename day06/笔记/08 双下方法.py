# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
'''
__str__ 如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值。
'''
# class A:
#     def __init__(self): pass
#
#     def __str__(self):
#         print(666)
#         return '太白'
# a = A()
# print(a)  # 返回 666 太白
#
# ret = '姓名 %s' % a
# print(ret)  # 返回 姓名 太白


'''
__call__ 对象后面加括号，触发执行。
'''
# class Foo:
#     def __str__(self): pass
#
#     def __call__(self, *args, **kwargs):
#         print(args)
#         print('__call__')
# obj = Foo()
# obj('WuSir', 'alex')  # 对象() 触发__call__() 方法


'''
__new__   先执行
__init__  后执行
'''
# class A:
#     def __init__(self):
#         self.x = 1
#         print('in init')
#
#     def __new__(cls, *args, **kwargs):
#         print('in new')
#         return object.__new__(cls)
#
# obj = A()
# print(obj.x)  # 先执行__new__ 然后执行__init__


'''
设计模式：
    单列模式：让一个类的实例化对象有且只有一个  ***
'''
# class A:
#     pass
#
# ret = A()
# ret1 = A()
# print(ret, ret1)  # 他们俩的内存地址不一致

# class A:
#     __instance = None  # 定义私有属性为None
#
#     def __new__(cls, *args, **kwargs):  # 先执行__new__方法，走if判断
#         if cls.__instance is None: # 如果为None
#             obj = object.__new__(cls) # 在原对象创建一个
#             cls.__instance = obj  # 调用私有方法，重新赋值
#         return cls.__instance  # 返回私有属性
# ret1 = A()
# ret2 = A()
# ret3 = A()
# print(ret1, ret2, ret3)  # 他们三个的内存地址是一样的


'''
__item__系列： __getitem__  __setitem__  __delitem__   ***
对一个对象进行类似字典的操作，就会触发__item__系列的某个方法
'''
# class Foo:
#     def __init__(self, name):
#         self.name = name
#
#     def __getitem__(self, item):
#         print('__getitem__ 此方法执行了')
#         print(item)
#         return self.__dict__[item]
#
#     def __setitem__(self, key, value):
#         self.key = value
#
#     def __delitem__(self, key):
#         print('del obj[key]时，我执行')
#         self.__dict__.pop(key)
#
#     def __delattr__(self, item):
#         print('del obj.key时，我执行')
#         self.__dict__.pop(item)
# f = Foo('alex')
# print(f['name'])  # 返回 alex
#
# f['age'] = 25
# print(f.__dict__)  # 返回 {'name': 'alex', 'key': 25}
#
# del f['name']
# print(f.__dict__)  # 返回 {'key': 25}







