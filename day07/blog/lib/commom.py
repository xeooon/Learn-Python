# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# ---------------------------- 此部分是 公共组件 ----------------------------
# 这里的配置文件需要写绝对路径，r的意思是转义
# 我当前的log.py文件需要，我的conf里面的settings.py里面的LOG_PATH对象

from conf import settings

def logger(f):
    def inner(*args, **kwargs):
        with open(settings.LOG_PATH, encoding='utf-8', mode='a+') as f1:
            f1.write('您访问了%s\n' % (f.__name__))
        ret = f(*args, **kwargs)
        return ret
    return inner