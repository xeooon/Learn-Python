# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
#
# login_status = {'username': None, 'status': False}
#
# def login(f):
#     def inner(*args, **kwargs):
#         if login_status['status']:
#             ret = f(*args, **kwargs)
#             return ret
#         else:
#             print('请先登录')
#             username = input('请输入账号').strip()
#             password = input('请输入密码').strip()
#             if username == '二狗' and password == '123':
#                 login_status['username'] = username
#                 login_status['status'] = True
#                 ret = f(*args, **kwargs)
#                 return ret
#     return inner
#
# @login
# def article():
#     print('欢迎访问文章页面.')
#
# @login
# def diary():
#     print('欢迎访问日记页面.')
#
# @login
# def comment():
#     print('欢迎访问评论页面')
#
#
# dic = {1:login, 2:article, 3:diary, 4:comment}
#
#
# while 1:
#     print('''
#     欢迎来到的博客园首页:
#         1.登录
#         2.访问文章页面
#         3.访问日记页面
#         4.访问评论页面
#     ''')
#     num = input('请输入访问的编号:').strip()
#     dic[int(num)]()
