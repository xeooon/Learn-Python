# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# a = 1
# b = 2
# print(a,b)
#
#
#
# def func1():
#     a1 = 1
#     b2 = 2
#     print(666)
# func1()
# len()
# print()

# 从上到下依次运行

# 全局名称空间:存储的是全局(当前py文件)的变量与值的对应关系
# 临时(局部)命名空间:当函数执行时,会在内存中临时开辟一个空间,此空间记录函数中的变量与值的对应关系,而且随着函数的结束,临时名称空间而关闭


# python中的空间:
    # 1.全局名称空间
    # 2.局部名称空间:
    # 3.内置名称空间: 内置函数len(), print()等

# 加载顺序:
# 内置名称空间 ---> 全局名称空间 ---> 函数执行时临时(局部)名称空间


# 作用域:
# 全局作用域:包含内置名称空间 全局名称空间
# 局部作用域: 包含临时(局部)名称空间


# 取值顺序:
# 函数执行时临时(局部)名称空间 ---> 全局名称空间 ---> 内置名称空间
# 满足就近原则
# len = 66
# print(len)
# a = 1
# def func():
#     a = 66
#     def func1():
#         a = 99
#         print(a)
#     func1()
# func()



'''
# LEGB原则:

# 1.location: 字函数
# 2.eclose: 父级函数
# 3.global:全局函数
# 4.bulit in: 内置函数


'''







'''

# global
'''

# 局部只能引用全局的变量，但是不能修改，修改就会报错。
# global 可以修改全局变量，
# 在局部空间可以申明一个全局变量
# a = 1
# def func():
#     global a
#     a += 1
#     print(a)
# func()

# def func():
#     global a
#     a = 1
# # print(a)
# func()
# print(a)







'''
nonlocal  python 2.7 没有
'''
# 不能操作全局变量
# 子名称空间，只能引用父级名称空间的变量，但是不能修改。

# a = 2
# def func():
#     nonlocal a
#     print(a)
# func()

# 在局部作用域中，对父级作用域（或者更外层作用域非全局作用域）的变量进行引用和修改，并且引用的哪层，从那层及以下此变量全部发生改　变。
# def func1():
#     a = 1
#     def inner():
#         nonlocal a
#         a += 1
#         # print(a)
#     print(a)
#     inner()
#     print(a)
# func1()



'''
# 函数的嵌套
# 程序执行到哪里,我就执行这个函数
'''
# def func1():
#     print(111)
#     def func2():
#         '''1万行代码'''
#         print(222)
#     print(333)
#     func2()
#     print(444)
# func1()


# 111 333 222 444
# 111 333 444 222

# def func1():
#     print(111)
#
# def func2():
#     print(222)
#     func1()
#
#
# def func3():
#     func2()
#     print(333)
#
# func3()








# 函数名的运用 第一类对象
# def func1():
#     print(111)

# 1.函数名可以当普通变量用
# a = 1
# b = a
# print(b)

# print(func1)
# f1 = func1
# f2 = f1
# # print(f2)
# f2()




# 2.函数名可以作为函数的参数
# def func1():
#     print(111)
#
# def func2(x):
#     print(x)
#     x()
# func2(func1)


# 3.函数名可以作为函数的返回值
# def func1():
#     print(111)
#
# def func2(x):
#     return x
#
# ret = func2(func1)  # x  func1
# ret()




# 4.函数名可以作为容器类型的参数

# a = 1
# b = 2
# c = 3
# l1 = [a,b,c]


# def func1():
#     print(111)
#
#
# def func2():
#     print(222)
#
#
# def func3():
#     print(333)
#
#
# def func4():
#     print(444)

# for i in l1:
#     print(i)
# l1 = [func1, func2, func3, func4]
# for i in l1:
#     i()


# dic = {
#     1: func1,
#     2: func2,
#     3: func3,
#     4: func4,
# }
# while 1:
#     choice = int(input('请输入数字：'))
#     dic[choice]()
