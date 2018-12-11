# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""


# 函数名的运用：
# 1，函数名可以作为变量。
# def func1():
#     print(111)
# ret = func1
# ret()

# 2,函数名可以作为函数的参数
# def func2():
#     print(666)
#
# def func3(x):
#     x()
# func3(func2)

# 3,函数名可以作为容器类类型的元素
# def func1():
#     print(666)
#
#
# def func2():
#     print(666)
#
#
# def func3():
#     print(666)
#
# l1 = [func1,func2,func3]
# for i in l1:
#     i()

# 函数名可以作为函数的返回值
# def func1():
#     print(666)
#
# def func2(x):
#     print(888)
#     return x
#
# ret = func2(func1)
# ret()




# 闭包
# 1.闭包是嵌套在函数中的
# 2.闭包是内层函数对外层函数的变量(非全局变量)的引用(改变)
# 3.闭包需要将其作为一个对象返回,而且必须逐层返回直至最外层函数的返回值.
# def func1():
#     '''
#     此函数满足前两个条件，但还不是闭包
#     :return:
#     '''
#     name = '太白'
#     def func2():
#         print(name)

'''
闭包举例：
'''
# 这是闭包
# def wrapper():
#     name = '太白'
#     def inner():
#         print(name)
#     return inner

# 这也是闭包
# def wrapper(name):
#     def inner():
#         print(name)
#     return inner
# n1 = 'wusir'
# wrapper(n1)

# 这不是闭包
# name = 'alex'
# def wrapper():
#     def inner():
#         print(name)
#     return inner




'''
闭包的作用
'''
# 非闭包函数：随着函数的结束临时空间关闭
# 闭包的函数：python遇到闭包，产生一个空间，这个空间不会随着函数的结束而消失。

# 非闭包函数
# def func1(s1):
#     n = 1
#     n += s1
#     print(n)
#
# func1(5)
# func1(5)
# func1(5)
# func1(5)

# 闭包函数
# def wrapper(s1):
#     n = 1
#     def inner():
#         nonlocal n
#         n += s1
#         print(n)
#     return inner
#
# ret = wrapper(5)
# ret()
# ret()
# ret()
# ret()






