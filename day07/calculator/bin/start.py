# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

import sys
import os

BASE_BATH = os.path.dirname(os.path.dirname(__file__))
print(BASE_BATH)
sys.path.append(BASE_BATH)

from core import src
from lib import commom


if __name__ == "__main__":  # 如果为执行文件时才运行
    print(''.center(60, '='))
    print('\033[33m欢迎使用计算器:\n此计算器只支持此[0-9, +, -, *, /, (, )]范围的元素\033[0m')
    print(''.center(60, '='))

    while 1:
        calculate_input = '1 - 2 * ((60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
        # calculate_input = input('\033[32m\n请输入计算的表达式[Q]:\033[0m')
        if len(calculate_input) == 0:
            continue

        elif calculate_input.isupper() == 'Q':
            break

        else:
            try:
                expression_l = commom.init_action(calculate_input)
                fin = src.main(expression_l)  # 数字栈,格式化处理后直接调用main主函数
                print('\n\033[33;1m最终结果为: %s\033[0m' % fin[0][0])  # 2776672.6952380957
                break

            except ValueError:
                print('\033[31m输入有误，请输入此[0-9, +, -, *, /, (, )]范围的元素。\033[0m')

            except IndexError:
                print('\033[31m输入有误，请输入此[0-9, +, -, *, /, (, )]范围的元素。\033[0m')
