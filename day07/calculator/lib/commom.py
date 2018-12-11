# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

import re
import time
from conf import settings


def logger(f):  # 定义日志装饰器
    def inner(*args, **kwargs):
        with open(settings.sys_platform()[0][0], encoding='utf-8', mode='a+') as f1:
            f1.write('%s 访问%s模块\n' % (time.strftime("%Y-%m-%d %X") ,f.__name__))

        ret = f(*args, **kwargs)
        return ret
    return inner


@logger
def is_symbol(element):  # 判断是否是数字还是符号
    res = False  #默认是数字
    sysbol = ['+', '-', '*', '/', '(', ')']
    if element in sysbol:  # 遍历格式化的列表，如果在我的sysbol里面就是运算符，True
         res = True
    return res


@logger
def prioitry(top_sym, wait_sym):  # 优先级比较函数，比较栈顶元素与遍历元素的优先级
    level1 = ['+', '-']
    level2 = ['*', '/']
    level3 = ['(']
    level4 = [')']

    if top_sym in level1:  # 如果栈顶运算符在level1里 + - 级别
        if wait_sym in level2 or wait_sym in level3:  # 栈顶运算符优先级低 < 待入栈运算符优先级高，直接入栈
            return '<'
        else:  # 栈顶运算符优先级高 > 待入栈运算符优先级低, 直接计算
            return '>'

    elif top_sym in level2:  # 如果栈顶运算符在level2里 * / 级别
        if wait_sym in level3:  # 栈顶运算符优先级低 < 待入栈运算符优先级高，直接入栈  * < (
            return '<'
        else:  # 栈顶运算符优先级高 > 待入栈运算符优先级低, 直接计算
            return '>'

    elif top_sym in level3:  # 如果栈顶运算符在level3里（ 级别
        if wait_sym in level4:  # 如果栈顶运算符找到了成对的，则取出
            return '='
        else:  # 如果找不到成对的，则无条件入栈
            return '<'


@logger
def calculate(num1, symbol, num2):  # 计算最小表达式单元的函数
    res = 0
    if symbol == '+':
        res = num1 + num2
    elif symbol == '-':
        res = num1 - num2
    elif symbol == '*':
        res = num1 * num2
    elif symbol == '/':
        res = num1 / num2
    # print('计算的步骤: [%s %s %s] = %s' % (num1, symbol, num2, res))  # 调试用
    return res  # 返回计算的结果


@logger
def init_action(expression):  # 格式化数据函数
    expression = re.sub(' ', '', expression)  # 将表达式输入的空替换掉
    init_l = [i for i in re.split('(\-\d+\.*\d*)', expression) if i]  # 把表达式处理成列表的形式，利用列表推导式去重
    expression_l = []  # 定义空列表存放格式化好的

    while 1:
        if len(init_l) == 0: break
        exp = init_l.pop(0)  # 从0位开始取出内容
        if len(expression_l) == 0 and re.search('^\-\d+\.*\d*$', exp):  # 如长度为0，查找exp并且以数字(负数 整数 浮点数)结尾
            expression_l.append(exp)  # 那么直接添加到列表里面
            continue

        if len(expression_l) > 0:  # 除开头任意部分有大于零
            if re.search('[\+\-\*\/\(\)]$', expression_l[-1]):  # 查找expression_l的最后一位,任意一位以加减乘除左右括号结尾
                expression_l.append(exp)  # 那么直接添加到列表里面
                continue

        new_l = [i for i in re.split('([\+\-\*\/\(\)])', exp) if i]  # 获得exp的值，任意一位以加减乘除左右括号为模版分割并去重
        expression_l += new_l

    return expression_l
