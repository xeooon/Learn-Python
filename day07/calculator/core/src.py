# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
import time

from lib import commom
from conf import settings


@commom.logger
def main(expression_l):  # 堆栈处理函数
    number_stack = []  # 定义数字(栈)列表
    symbol_stack = []  # 定义运算符(栈)列表
    file = settings.sys_platform()

    for ele in expression_l:  #判断输入的是运算符还是数字
        with open(settings.sys_platform()[1][0], encoding='utf-8', mode='a+') as f1:
            f1.write('\n%s\n 数字栈:%s\n 运算符栈:%s\n 待入栈运算符:%s\n' % (
                time.strftime("%Y-%m-%d %X"), number_stack, symbol_stack, ele))  # 写入func.log

        ret = commom.is_symbol(ele)
        if not ret:  # 如果是数字则加入到number_stack数字(栈)列表
            ele = float(ele)  # 将字符串转换为浮点数（比int精度高）
            number_stack.append(ele)

        else:  # 如果是运算符则加入到symbol_stack 运算符(栈)列表
            while 1:
                if len(symbol_stack) == 0:  # 无条件添加到运算符栈
                    symbol_stack.append(ele)
                    break
                res = commom.prioitry(symbol_stack[-1], ele)  # 运算符栈栈顶元素与待入栈元素 比较优先级

                if res == '<':  # 无条件添加到运算符栈
                    symbol_stack.append(ele)
                    break

                elif res == '=':  # 取出运算符栈顶元素,找到()
                    symbol_stack.pop()
                    break

                elif res == '>':  # 取出运算符栈顶元素, 取出两个数字栈元素,调用calculate函数运算
                    symbol = symbol_stack.pop()
                    num2 = number_stack.pop()
                    num1 = number_stack.pop()
                    number_stack.append(commom.calculate(num1, symbol, num2))  # 计算后增加到数字栈

    else:  # 计算最后的
        while len(symbol_stack) >= 1:
            symbol = symbol_stack.pop()
            num2 = number_stack.pop()
            num1 = number_stack.pop()
            number_stack.append(commom.calculate(num1, symbol, num2))  # 计算后增加到数字栈

    return number_stack, symbol_stack
