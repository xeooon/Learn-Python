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
# from conf import settings

log1 = commom.get_logger('购物车相关')   # 区分不同业务 [task_id:日记页面相关]
log2 = commom.get_logger('日记页面相关')


def login():
    pass

# @commom.logger
def comment():
    print('欢迎访问评论页面')

# @commom.logger
def article():
    print('欢迎访问文章页面')

# @commom.logger
def diary():
    log2.info('日记页面出现问题...')
    print('欢迎访问日记页面')

def shopping():
    log1.info('购物车：二狗花了300买了一个充气。。。')
    print('欢迎进入购物车')

dic = {1: register.register, 2: login, 3: comment, 4: article, 5: diary, 6:shopping}

def run():
    while 1:
        print('1:register\n', '2:login\n', '3:comment\n', '4:article\n', '5:diary\n', '6:shopping')
        try:
            choice = int(input('请输入'))
            dic[choice]()

        except KeyError:
            print('不存在此项')
        except ValueError:
            print('请输入数字')
        except Exception:
            print(Exception)