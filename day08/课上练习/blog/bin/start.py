# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# ---------------------------- 此部分是 启动文件 ----------------------------

import os
import sys

# 模块的引用顺序:
# 1.先从内存中找 ----> 2.然后内置模块(os,time...) ----> 3.最后sys.path()
BASE_BATH = os.path.dirname(os.path.dirname(__file__))  # 自动获取当前项目根目录
# print(BASE_BATH)
sys.path.append(BASE_BATH)
from core import src

# 当成执行文件: __main__
# 当成模块被引用: 模块名
if __name__ == '__main__':  # 防止其他文件引用并执行
    src.run()

