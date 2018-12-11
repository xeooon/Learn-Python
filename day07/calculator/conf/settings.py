# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
import sys
import os

def sys_platform():  # 判断系统平台函数
    log_exec = []
    log_func = []

    if sys.platform == 'darwin':  # 我的mac os 平台名
        f_name = ['exec.log', 'func.log']
        f_path = os.path.dirname(os.path.dirname(__file__))
        LOG_EXEC = f_path + '/log' + '/' + f_name[0]
        log_exec.append(LOG_EXEC)

        LOG_FUNC = f_path + '/log' + '/' + f_name[1]
        log_func.append(LOG_FUNC)

    else:  # 其他平台
        f_name = ['exec.log', 'func.log']
        f_path = os.path.dirname(os.path.dirname(__file__))
        LOG_EXEC = '%s\log\%s' % (f_path, (f_name[0]))
        log_exec.append(LOG_EXEC)

        LOG_FUNC = '%s\log\%s' % (f_path, (f_name[1]))
        log_func.append(LOG_FUNC)

    # print(log_exec[0], '\n', log_func[0])
    return log_exec, log_func