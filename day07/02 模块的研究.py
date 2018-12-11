# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
# 自定义模块
# 以tbjx.py为演示
# import tbjx


# 模块首次引用：先从内存 ---> 内置模块（os,time sys..） ---> sys.path 去找
# 执行文件: 解释器运行到文件
# 被引用文件: import, 不是主动触发的


'''
模块引用发生了三件事儿:
'''
# 1.他在内存中, 开辟了一个以tbjx命名的空间.
# 2.你模块中的所有内容都加载到了内存.
# 3.你要通过tbjx.的方式去引用模块中的对象.


'''
为模块起别名:
'''
# 1.将模块名叫较长的改成短的, 便于操作, 主要用途
# import tbjx as sm

# 2.可以拓展代码，扩展代码可以用分发文件和相对路径
# sql = input('请输入').strip()
# if sql == 'mysql':
#     import mysql1 as db
# elif sql == 'oracle':
#     import oracle1 as db
# db.sqlsentance()


'''
导入多个模块
'''
# 需要满足pep8规范
# import os
# import sys

# from ... import ...
# 优点: 方便使用, 节省内存
# 缺点: 可能会与当前执行文件产生冲突
# import tbjx
# tbjx.read1()  # 返回 tbjx模块： 太白金星

# name = 'alex'
# from tbjx import read1, name
# read1()  # 返回 tbjx模块： 太白金星
# print(name)  # 返回 太白金星
# print(name)  # 返回 太白金星


# 不建议全部引用 *
# 但是可以在一定条件下使用
# 在模块中添加__all__ = ['read1', 'read2']
# from tbjx import *
# read1()
# read2()


'''
py文件的功能:
'''
# 1.可以被当成模块使用(可以被调用)
# 2.可以执行本文件的功能()

# import tbjx
# print(__name__)  # 返回 __main__
# 当成执行文件: __main__
# 当成模块被引用: 模块名
#
#__name__
# 在本文件调试


'''
模块的引用顺序:先从内存 ---> 内置模块（os,time sys..） ---> sys.path 去找
'''
# import sys
# print(sys.path)  # 先是当前路径
# print(sys.modules)  # python解释器运行时自动加载到内存的一些模块


'''
包里面可以有多个模块
包的示例：
引用day07下面的aaa包的m1模块，bbb包的m2模块，ccc包的m3模块
'''

# 找到m1文件的方式:
# 1.将m1路径主动添加到sys.path用apped添加
# 2.用from...import..

# 方法1：不在aaa和bbb和ccc里面做任何操作，直接调用
# from aaa import m1
# from aaa.bbb import m2
# from aaa.bbb.ccc import m3
#
# m1.func1()  # aaa里面m1模块的func1执行了
# m2.func2()  # aaa里面的bbb目录的m2模块的func2执行了
# m3.func3()  # aaa里面的bbb里面的ccc目录的m3模块的func3执行了


# 方法2：在aaa目录的__init__.py增加内容
# from ... import ...
# import aaa
# aaa.m1.func1()  # aaa里面m1模块的func1执行了
# aaa.bbb.m2.func2()  # aaa里面的bbb目录的m2模块的func2执行了
# aaa.bbb.ccc.m3.func3()  # aaa里面的bbb里面的ccc目录的m3模块的func3执行了
