# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
import json
'''数据类型转字符串'''
# a = [12,24,34]
# a1 = json.dumps(a)
# print(a1, type(a1))
'''字符串转数据类型'''
# b = '[12, 24, 34]'
# b1 = json.loads(b)
# print(b1 , type(b1))

'''数据类型转字符串写到文件'''
# with open("aa","w", encoding="utf8", ) as f:
#     a = [12, 24, 34]
#     json.dump(a,f)

'''从文件中读取内容转成数据类型'''
with open("aa","r", encoding="utf8", ) as f:

    a = json.load(f)
    print(a, type(a))

