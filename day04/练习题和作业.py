# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
"""
标题 : 24期周末班 - day04 - 习题和作业
作者 : 张志强
QQ号 : 1344683865
微信 : qingniaoxiaoqiang
邮箱 : Xeon@xeon.org.cn
"""

# ###################################### 练习题 #######################################

'''
1、整理装饰器的形成过程，背诵装饰器的固定格式
'''
# 1.不能重复造轮子
# 2.线上的函数你不能改变
# 3.函数的原本调用方式不能改变

# 固定格式
# def wrapper1(f1):
#     def inner1(*args, **kwargs):    # 聚合
#         # 执行被装饰函数之前的操作
#         ret = f1(*args, ** kwargs)  # 打散
#         # 执行被装饰函数之后的操作
#         return ret
#     return inner1
#
# @wrapper1  # func1 = wrapper1(func1)
# def func1(a):
#     print(666, a)
# func1('xeon')  # inner()


'''
2、编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需
求添加代码’
'''
# def wrapper2(f2):
#     def inner2(*args, **kwargs):  # 聚合
#         print('被执行函数之前')
#         f2(*args, **kwargs)       # 打散
#     return inner2
#
# @wrapper2  # func2 = wrapper(func2)
# def func2():
#     print('func2')
# func2()  # inner2()


'''
3、编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据
需求添加代码’
'''
# def wrapper3(f3):
#     def inner3(*args, **kwargs):  # 聚合
#         f3(*args, **kwargs)       # 打散
#         print('被执行函数之后')
#     return inner3
#
# @wrapper3  # func3 = wrapper3(func3)
# def func3():
#     print('func3')
# func3()  # inner3()


'''
4、编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访问该函数.
'''
# l1 = ['老铁', '111']
# def login4(f4):
#     def inner4(*args, **kwargs):
#         for i in range(3):  # 循环3次
#             username = input('请输入账号:').strip()
#             password = input('请输入密码:').strip()
#             if username == l1[0] and password == l1[1]:  # 必须全部为字符串
#                 f4(*args, **kwargs)
#             else:
#                 count = 2
#                 print('帐号或密码有误,剩余尝试%s次.' % (count - i))
#     return inner4
#
# @login4  # func4 = login4(func4)
# def func4():
#     print('欢迎%s访问此函数.')
# func4()  # inner4()


'''
5、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,
给用户三次机会），要求登录成功一次，后续的函数都无需再输入用户名和密码
'''
# user_status = {'username': None}
# def login5(f5):
#     def inner5(*args, **kwargs):
#         if user_status['username'] != None:  # 如果用户不为None
#             ret = f5(*args, **kwargs)
#             return ret
#         with open('register', encoding='utf-8') as f1:
#             file = f1.readline().strip().split('|')
#         for i in range(3):  # 循环3次
#             username = input('请输入账号:').strip()
#             password = input('请输入密码:').strip()
#             if username == file[0] and password == file[1]:  # 必须全部为字符串
#                 user_status['username'] = username
#                 ret = f5(*args, **kwargs)
#                 return ret
#             else:
#                 count = 2
#                 print('帐号或密码有误,剩余尝试%s次.' % (count - i))
#     return inner5
#
# @login5  # func5 = login5(func5)
# def func5():
#     print('欢迎访问此函数1.')
# func5()  # inner5()
#
# @login5  # func5_1 = login5(func5_1)
# def func5_1():
#     print('欢迎访问此函数2.')
# func5_1()  # inner5_1()


'''
6、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,可支持多账号密码），
要求登录成功一次（给三次机会），后续的函数都无需再输入用户名和密码。
'''
# user_status = {'username': None, 'status': False}
# def wrapper6(f6):
#     def inner6(*args, **kwargs):
#         if user_status['status']:
#             ret6 = f6(*args, **kwargs)
#             return ret6
#         else:
#             for count in range(3):  # 循环3次
#                 username = input('请输入帐号:').strip()
#                 password = input('请输入密码:').strip()
#                 with open('register', encoding='utf-8') as f1:
#                     for i in f1:
#                         i = i.strip().split('|')
#                         if i[0] == username and i[1] == password:  # 需要把文件的取值放在前面
#                             user_status['username'] = username
#                             user_status['status'] = True
#                             ret6 = f6(*args, **kwargs)
#                             return ret6
#                     else:
#                         print('帐号或密码有误,剩余尝试%s次.' % (2 - count))
#     return inner6
#
# @wrapper6  # func6 = wrapper6(func6)
# def func6():
#     print(666)
# func6()  # inner6()
#
# @wrapper6  # func6_1 = wrapper6(func6_1)
# def func6_1():
#     print(666_1)
# func6_1()  # inner6()


'''
7、给每个函数写一个记录日志的功能，
功能要求：每一次调用函数之前，要将函数名称，时间节点记录到log的日志中。
所需模块：
import time
struct_time = time.localtime()
print(time.strftime("%Y‐%m‐%d %H:%M:%S",struct_time))
'''
# import time
# def wrapper7(f7):
#     def inner7(*args, **kwargs):
#         time_now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
#         stime = time.time()
#         ret7 = f7(*args, **kwargs)
#         etime = time.time()
#         with open('log', encoding='utf-8', mode='a') as f1:
#             f1.write('在%s时间,执行了%s函数,耗时%s秒.\n' % (time_now, f7.__name__, etime - stime))
#         return ret7
#     return inner7
#
# @wrapper7  # func7 = wrapper7(func7)
# def func7():
#     time.sleep(0.2)
#     print(666)
# func7()  # inner7()


# ###################################### 作 业 #######################################


'''
1)，启动程序，首页面应该显示成如下格式：
    欢迎来到博客园首页
    1:请登录
    2:请注册
    3:文章页面
    4:日记页面
    5:评论页面
    6:收藏页面
    7:注销
    8:退出程序
2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。
3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，
        没成功则结束整个程序运行，成功之后，可以选择访问3~6项，访问页面之前，
        必须要在log文件中打印日志，日志格式为-->用户:xx 在xx年xx月xx日 执行了 %s函数，
        访问页面时，页面内容为：欢迎xx用户访问评论（文章，日记，收藏）页面
4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选择。
5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。
'''
import time
def auth(f):  # 装饰器
    def inner(*args, **kwargs):
        time_now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
        if login_status['status']:
            stime = time.time()
            ret = f(*args, **kwargs)
            etime = time.time()
            with open('log', encoding='utf-8' ,mode='a') as f1:
                f1.write('在%s时间,执行了%s函数,耗时%s秒.\n' % (time_now, f.__name__, etime - stime))
            return ret
        else:
            for count in range(3):  # 循环3次
                username = input('请输入帐号:').strip()
                password = input('请输入密码:').strip()
                with open('register', encoding='utf-8') as f1:
                    for i in f1:
                        i = i.strip().split('|')
                        if i[0] == username and i[1] == password:  # 需要把文件的取值放在前面
                            login_status['username'] = username
                            login_status['status'] = True
                            stime = time.time()
                            ret = f(*args, **kwargs)
                            etime = time.time()
                            with open('log', encoding='utf-8', mode='a') as f1:
                                f1.write('在%s时间,执行了%s函数,耗时%s秒.\n' % (time_now, f.__name__, etime - stime))
                            return ret
                    else:
                        print('\033[31;1m帐号或密码有误,剩余尝试%s次.\033[0m' % (2 - count))
    return inner

@auth
def login():  # 登录函数
    print('\033[32;1m%s登录成功.\033[0m' % login_status['username'])

def register(username, password):  # 注册函数
        with open('register', encoding='utf-8') as f1:  # 只读方式打开文件对比当前用户
            for i in f1:
                i = i.strip().split('|')
                if username in i[0]:  # 判断用户是否存在
                    print('\033[31;1m用户%s已存在,请登录.\033[0m' % username)
                    break
            else:
                with open('register', encoding='utf-8', mode='a') as f2:
                    f2.write('{}|{}\n'.format(username, password))
                    print('\033[33;1m用户%s注册成功,已为您自动登录.\033[0m' % username)
                    login_status['username'] = username
                    login_status['status'] = True
@auth
def article():
    print('\033[32;1m欢迎访问文章页面\033[0m')
@auth
def diary():
    print('\033[34;1m欢迎反问日志页面.\033[0m')
@auth
def comment():
    print('\033[35;1m欢迎访问评论页面.\033[0m')
@auth
def collect():
    print('\033[36;1m欢迎访问收藏页面.\033[0m')

def logout():
    time_now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    stime = time.time()
    print('\033[33;1m%s用户注销成功.\033[0m' % login_status['username'])
    login_status['username'] = None
    login_status['status'] = False
    etime = time.time()
    with open('log', encoding='utf-8', mode='a') as f1:
        f1.write('在%s时间,执行了%s函数,耗时%s秒.\n' % (time_now, logout.__name__, etime - stime))

login_status = {'username': None, 'status': False}
dic = {0: login, 1: register, 2: article, 3: diary, 4: comment, 5: collect, 6: logout}
def index():
    while 1:
        print('\033[33;1m欢迎来到博客园首页\033[0m'.center(40, '-'))
        l1 = {0: '请登录', 1: '请注册', 2: '文章页面', 3: '日记页面',
              4: '评论页面', 5: '收藏页面', 6: '注销', 7: '退出程序'}
        for k, v in l1.items(): print(k, v)
        num = input('\n请输入访问的编号:').strip()
        if num == '0': dic[0]()
        elif num == '1':
            username = input('请输入注册的账号:').strip()
            password = input('请输入注册的密码:').strip()
            dic[1](username,password)
        elif num == '2': dic[2]()
        elif num == '3': dic[3]()
        elif num == '4': dic[4]()
        elif num == '5': dic[5]()
        elif num == '6': dic[6]()
        elif num == '7':
            print('\033[32;1m退出程序成功\033[0m')
            break
        else: print('\033[31;1m无此编号\033[0m')
index()












# import time
#
# userstat = {"username": None, "status": False}
#
#
# def wapper(f):
#     def inner():
#         if userstat["status"]:
#             with open("run.log", encoding="utf-8", mode="a") as f1:
#                 tm1 = time.localtime()
#                 time1 = "{}年{}月{}日".format(tm1.tm_year, tm1.tm_mon, tm1.tm_mday)
#                 f1.write("用户：{} 在{} 执行了 {}函数\n".format(userstat["username"], time1, f.__name__))
#                 f()
#         else:
#             print("请登录后访问")
#             if loging():
#                 f()
#             else:
#                 return False
#
#     return inner
#
#
# def loging():
#     '''用户登录'''
#     print("用户登录程序启动~~~~！")
#     for i in range(3):
#         username = input("请输入用户名：")
#         if not username.strip():
#             print("用户名不能为空")
#             continue
#         password = input("请输入 密码：")
#         with open("register", encoding="utf-8") as f1:
#             for i in f1:
#                 user = i.strip().split(":")
#                 if username == user[0] and password == user[1]:
#                     userstat["username"] = username
#                     userstat["status"] = True
#                     print("用户{}登录成功".format(username))
#                     return True
#             else:
#                 print("登录错误请重试")
#     else:
#         print("你的三次机会已用完")
#         return False
#
#
# def register():
#     '''用户注册'''
#     print("注册程序开始运行(づ￣3￣)づ╭～")
#     username = input("请输入用户名：")
#     password = input("请输入密 码：")
#     with open("register", encoding="utf-8", mode="r+") as f2:
#         for i in f2:
#             user = i.strip().split(":")
#             if user[0] == username:
#                 print("用户名已存在请重新注册")
#                 break
#         else:
#             f2.write("{}:{}\n".format(username, password))
#             userstat["username"] = username
#             userstat["status"] = True
#             print("用户{}注册成功".format(username))
#
#
# @wapper
# def article():
#     """文章页面"""
#     print("欢迎用户：{}访问文章页面".format(userstat["username"]))
#
#
# @wapper
# def diary():
#     '''日记页面'''
#     print("欢迎用户：{}访问日记页面".format(userstat["username"]))
#
#
# @wapper
# def comment():
#     '''评论页面'''
#     print("欢迎用户：{}访问评论页面".format(userstat["username"]))
#
#
# @wapper
# def collection():
#     '''收藏页面'''
#     print("欢迎用户：{}访问收藏页面".format(userstat["username"]))
#
#
# def logout():
#     '''注销账户'''
#     if userstat["status"]:
#         userstat["username"] = ""
#         userstat["status"] = False
#     else:
#         print("\033[7;31m你没登录注销啥~！\033[0m'")
#
#
# def quitexe():
#     '''退出程序'''
#     return False
#
#
# menulist = {'1': loging,
#             '2': register,
#             '3': article,
#             '4': diary,
#             '5': comment,
#             '6': collection,
#             '7': logout,
#             '8': quitexe,
#             }
#
# # print(menulist)
# while 1:
#     print("欢迎来到博客园首页\n1:请登录\n2:请注册\n3:文章页面\n4:日记页面\n5:评论页面\n6:收藏页面\n7:注销\n8:退出程序")
#     select = input("请输入你的选择：")
#     if select in menulist:
#         if menulist[select]() == False: break
#     else:
#         print("没有此选项，重新输入")
