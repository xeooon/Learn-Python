# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# 这里是from ... import *时，指定特定的
__all__ = ['read1', 'read2']
name = '太白金星'

print('from the tbjx.py')

name = '太白金星'

def read1():
    print('tbjx模块：', name)

def read2():
    print('tbjx模块')
    read1()

def change():
    global name
    name = 'barry'