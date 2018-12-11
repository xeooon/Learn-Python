# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# ---------------------------- 此部分是 核心逻辑 ----------------------------
# 我当前的src.py文件需要，我的lib里面的commom.py的logger对象
# 我当前的src.py文件需要，我的db里面的register.py的register对象

from lib import commom
from db import register

def login():
    pass

@commom.logger
def comment():
    print('欢迎访问评论页面')

@commom.logger
def article():
    print('欢迎访问文章页面')

@commom.logger
def diary():
    print('欢迎访问日记页面')

dic = {1: register.register, 2: login, 3: comment, 4: article, 5: diary}

def run():
    while 1:
        choice = input('请输入')
        if choice.isdigit():
            choice = int(choice)
            dic[choice]()
        else:
            print('请重新输入')
