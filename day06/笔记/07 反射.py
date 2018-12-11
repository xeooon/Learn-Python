# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

'''
isinstance: 它判断的是，obj是否是此类，或者此类的子孙类，实例化出来的对象
'''
# class A: pass
# class B(A): pass
#
# obj = B()
#
# print(isinstance(obj, B))  # 返回 True
# print(isinstance(obj, A))  # 返回 True


'''
getattr()  获取属性 ***
hasattr()  是否有属性 ***
setattr()  设置属性 *
delattr()  删除属性 *

反射就是： 通过 字符串 去操作对象（实例化对象 类，模块）
'''
'''
对实例化对象的示例
'''
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = A('脸哥', 27)  # 实例化对象A

ret = getattr(obj, 'abc', None)  # 获取obj的abc属性，没有则返回为None目的是不让报错
print(ret)

print(hasattr(obj, 'age'))  # obj是否有age属性

# 增加判断例子
if hasattr(obj, 'name'):
    ret = getattr(obj, 'name')
    print(ret)

setattr(obj, 'sex', '男')  # 设置属性
print(getattr(obj, 'sex'))

delattr(obj, 'name')  # 删除属性
print(obj.__dict__)



'''
对类的示例
'''
# class A:
#     name = 'alex'
#     def __init__(self): pass
#
#     def func(self): print('IN FUNC')

# print(getattr(A, 'name'))  # 获取A类的name为alex

# ret = getattr(A, 'func')
# ret(None)  # 执行A类的动态方法

# ret = input('>>>')
# f1 = getattr(A, ret)(None)  # 输入func， 返回IN FUNC


'''
对当前模块（文件）
'''
# def func():
#     print('in func')
#
# import sys
#
# current_mode = sys.modules[__name__]
# getattr(current_mode, 'func')


'''
对其他模块（文件）
'''
# 首先在相对路径建立一个fs的python文件
# fs文件内容
# n1 = '二狗'
#
# def func():
#     print(666)
#
# class A:
#     name = 'alex'
#
#     def func2(self):
#         print('--------IN FUNC2')

# import fs  # 标红先忽略
# print(getattr(fs, 'n1'))  # 返回 二狗
#
# ret = getattr(fs, 'func')
# ret()  # 返回 666

# 方法1：获取A类的静态属性
# clas = getattr(fs, 'A')
# print(clas.name)  # 返回 alex

# 方法2：即执行A类方法，又执行A类的动态方法
# print(getattr(fs.A, 'name'))  # 返回 alex
# getattr(fs.A, 'func2')(None)  # 返回 --------IN FUNC2

