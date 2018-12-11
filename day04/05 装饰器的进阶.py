# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""


'''
装饰器语法糖传参
'''
# def login(a, b):
#     print(a, b)
#
#     def wrapper(f):
#         def inner(*args, **kwargs):
#             ret = f(*args, **kwargs)
#             return ret
#         return inner
#     return wrapper
#
# @login(1,2)
# def func1():
#     print(111)
# func1()






'''
给500个函数加上装饰器在去掉,在加在去...
'''


# 给装饰器传参数
# login_status = {
#     'username': None,
#     'status': False,
# }
#
# def login(a):
#     def wrapper(f):
#         def inner(*args, **kwargs):
#             if a:
#                 if login_status['status']:
#                     ret = f(*args, **kwargs)
#                     return ret
#                 else:
#                     print('请先登录')
#                     username = input('请输入用户名').strip()
#                     password = input('请输入密码').strip()
#                     if username == '二狗' and password == '123':
#                         login_status['username'] = username
#                         login_status['status'] = True
#                         ret = f(*args, **kwargs)
#                         return ret
#             else:
#                 ret = f(*args, **kwargs)
#                 return ret
#         return inner
#     return wrapper
#
# flag = False
#
# @login(flag)
# def func1():
#     print(111)
# @login(flag)
# def func2():
#     print(12)
# @login(flag)
# def func3():
#     print(131)
#
# func1()




'''
一个装饰器,区分不同账号登录不同的网站
'''
# login_status = {
#     'username': None,
#     'status': False,
# }
#
# def login(a):
#     def wrapper(f):
#         def inner(*args, **kwargs):
#             if login_status['status']:
#                 ret = f(*args, **kwargs)
#                 return ret
#             else:
#                 print('请先登录')
#                 '''根据a 京东，天猫 去验证不同密码'''
#                 username = input('请输入用户名').strip()
#                 password = input('请输入密码').strip()
#                 if username == '二狗' and password == '123':
#                     login_status['username'] = username
#                     login_status['status'] = True
#                     ret = f(*args, **kwargs)
#                     return ret
#         return inner
#     return wrapper
#
# @login('京东')
# def jd():
#     print('欢迎访问文章页面')
#
# @login('京东')
# def jdmarkte():
#     print('欢迎访问日记页面')
#
# @login('天猫')
# def TM():
#     print('欢迎访问评论页面')
#
# @login('天猫')
# def TMmarke():
#     print('欢迎访问评论页面')


'''
多个装饰器装饰一个函数,先装饰最近一个函数,就近原则
'''
# def wrapper1(func):
#     def inner1():  # func = f
#         print('wrapper1 , before func')
#         func()  # 函数名f()
#         print('wrapper1,after func')
#     return inner1
#
# def wrapper2(func):
#     def inner2():
#         print('wrapper2 , before func')
#         func()
#         print('wrapper2,after func')
#     return inner2
#
# @wrapper2  # f = wrapper2(f) 里面的f是inner1, 外面的f 是inner2
# @wrapper1  # f = wrapper1(f) 里面的f是函数名f, 外面的f 是inner1
# def f():
#     print('in f')
# f()






# def dec1(func1):  #10、第三步func1 =two
#     print("1111")  #11、第三步 输出1111
#     def one():      #14执行这里
#         print("2222")    #15输出这里
#         func1()         #16、执行这里也就是 two（）
#         print("3333")   #最后输出这个
#     return one   #12、将one返回给test   然后再执行test（）最下面的执行语句
# def dec2(func2):   #6、第二步 func = three
#     print("aaaa")  #7、第二步 输出aaaaaa
#     def two():         #17、执行到这里
#         print("bbbb")  #18、输出
#         func2()         #19、执行这里，也就是three（）
#         print("cccc")   #25、输出，然后返回到 func1 后面，因为从那过来的
#     return two      #8、将two返回给test   然后执行@dec1
# def dec3(func3):    #2、第一步执行时func = test
#     print("!!!!")   #3、第一步执行时输出   three = dec2(tree)
#     def three():      #20、执行这里
#         print("####")  #21、输出
#         func3()         #22、执行这里，也就是test（）
#         print("****")   #25、输出，然后返回到 func2 后面，因为从那过来的
#     return three     #4、将three返回给test   然后执行@dec2
# @dec1         #9、第三步： test = dec1(func1) = one(return返回的）        func1 = test = two
# @dec2        #5、第二步 test = dec2(func2) = two(return返回的）        func2 = test = three
# @dec3      #1、第一步 test = dec3(func3) = three(return返回的）        func3 = test
# def test():           #23、执行这里
#     print("test test")   #24输出，返回到func3（）后面，因为从那过来的
# test()               #13、执行到这里    执行因为test = one，执行one（）函数
