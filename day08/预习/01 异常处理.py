# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# 使用if判断式
# def test():
#     print('test running')
#
# choice_dic = {
#
#     '1': test
# }
#
# while 1:
#     choice = input('>>:').strip()
#     # 如果输入的内容不是choice 或者 不在我的choice_dic里面，那么我就让他继续输入
#     if not choice or choice not in choice_dic: continue
#     choice_dic[choice]()


# 异常处理的私人定制
# try:
#     被检测的代码块
# except 异常类型：
#     try 中一旦检测到异常，就执行这个位置的逻辑

# 方式1
# f = open('a.txt')
# g = (line.strip() for line in f)
# for line in g:
#     print(line)
#
# else:
#     f.close()

# try:
#     f = open('a.txt')
#     g = (line.strip() for line in f)
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#
# except SyntaxError
#     f.close()

