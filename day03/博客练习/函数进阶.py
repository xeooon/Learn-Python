# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

'''
命名空间一共分为三种:
'''
# 1.全局命名空间
# 2.局部命名空间
# 3.内部命名空间: 存放了python解释器为我们提供的名字: input print...


'''
三种命名空间之间加载的与取值顺序
'''
# 1.加载数序:
#     内置命名空间(程序运行前加载) ---> 全局命名空间(程序运行中:从上到下加载) ---> 局部命名空间(程序运行中:调用时才加载)
# 2.取值顺序:
#     在局部调用: 局部命名空间 ---> 全局命名空间 ---> 内置命名空间
#     在全局调用: 全局名称空间 ---> 内置名称空间

# 综上所述,在寻找变量时,从小范围,一层一层到大范围去找寻

'''
作用域
'''
# 作用域就是作用范围,按照生效范围可以分:
# 1.全局作用域: 包含内置名称空间, 全局名称空间, 在整个文件的任意位置都能被引用,全局有效
# 2.局部作用域: 局部名称空间,只能在局部范围内生效


'''
globals和locals方法

'''

# print(globals())
# print(locals())


# def func():
#     a = 12
#     b = 20
#     print(locals())
#     print(globals())
# func()


'''
globals 和 nonlocal关键字
'''
# gloal:
# 1.声明一个全局变量
# 2.在局部作用域想要对全局作用域的全局变量进行修改时,需要用到global(限于字符串,数字)
# 3.对可变数据类型(list, dict, set) 可以直接引用,不通过global

# global 关键字举例
# def func():
#     global a
#     a = 3
# func()
# print(a)

# count = 1
# def search():
#     global count
#     count = 2
# search()
# print(count)


# 对于可变数据类型的应用举例
# li = [1, 2, 3]
# dic = {'a': 'b'}
#
# def change():
#     li.append('a')
#     dic['q'] = 'g'
#     print(dic)
#     print(li)
# change()
# print(li)
# print(dic)


#nonlocal
# 1.不能修改全局变量
# 2.在局部作用域中,对父级作用域(或者更外城作用域,非全局作用域)的变量进行引用和修改,并且引用的哪层,从那层及以下此变量全部发生改   变.

# nonlocal关键字举例
# def add_b():
#     b = 42
#     def do_global():
#         b = 10
#         print(b)
#         def dd_nonlocal():
#             nonlocal b
#             b = b + 20
#             print(b)
#         dd_nonlocal()
#     print(b)
#     do_global()
#     print(b)
# add_b()




'''
函数的嵌套和作用域链
'''
# 函数的嵌套调用
# def max2(x, y):
#     m = x if x > y else y
#     return m
#
# def max4(a, b, c, d):
#     res1 = max2(a, b)
#     res2 = max2(res1, c)
#     res3 = max2(res2, d)
#     return res3
#
# print(max4(23, -7, 31, 11))


# 函数的嵌套定义
# def f1():
#     print('in f1')
#     def f2():
#         print('in f2')
#     f2()
# f1()

# def f1():
#     def f2():
#         def f3():
#             print('in f3')
#         print('in f2')
#         f3()
#     print('in f1')
#     f2()
# f1()

# 函数的作用域链：小范围作用域可以使用大范围的变量，但是反之不行，他是单向的。



''''
函数名的本质
'''
# 函数名本质上就是函数的内存地址
# 1.可以被引用
# def func():
#     print('in func')
# f = func
# print(f)

# 2.可以被当做容器类型的元素
# def f1():
#     print('f1')
# def f2():
#     print('f2')
# def f3():
#     print('f3')
# l = [f1, f2, f3]
# d = {'f1': f1, 'f2': f2, 'f3': f3}
#
# # 调用
# l[0]()
# d['f2']()


# 可以当做函数的参数和返回值
# def f1():
#     print('f2')
#
# def func1(argv):
#     argv()
#     return argv
#
# f = func1(f1)
# f()


# 第一类对象概念:不明白？那就记住一句话，就当普通变量用
# 第一类对象（first-class object）指
# 1.可在运行期创建
# 2.可用作函数参数或返回值
# 3.可存入变量的实体。



'''
闭包
'''
# def func():
#     name='张志强'
#     def inner():
#         print(name)
        
# 内部函数包含,对外部函数作用域,而非全局作用域,变量的引用,该内部函数称为闭包函数
# 函数内部定义的函数称为内部函数
# 数内的变量我们要想在函数外部用，可以直接返回这个变量
# 在函数外部调用函数内部的函数,直接就把这个函数的名字返回

# def func():
#     name = 'eva'
#     def inner():
#         print(name)
#     return inner
# f = func()
# f()


# 判断闭包函数的方法 __closure__
# 输出的__closure__有cell元素:是闭包函数
# def func():
#     name = 'eva'
#     def inner():
#         print(name)
#     print(inner.__closure__)
#     return inner
# f = func()
# f()



#输出的__closure__为None ：不是闭包函数
# name = 'egon'
# def func2():
#     def inner():
#         print(name)
#     print(inner.__closure__)
#     return inner
# f2 = func2()
# f2()


# 闭包的嵌套
# def wrapper():
#     money = 1000
#     def func():
#         name = 'eva'
#         def inner():
#             print(name, money)
#         return inner
#     return func
# f = wrapper()
# i = f()
# i()


# 闭包函数获取网络应用
# from urllib.request import urlopen
#
# def index():
#     url = 'http://www.cnblogs.com/jin-xin/articles/8259929.html'
#     def get():
#         return urlopen(url).read()
#     return get
#
# xiaohua = index()
# content = xiaohua()
# print(content)




