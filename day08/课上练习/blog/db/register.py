# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# ---------------------------- 此部分是 DB     ----------------------------
# 这里的配置文件需要写绝对路径，r的意思是转义
# 我当前的db.py文件需要，我的conf里面的settings.py里面的DB_PATH对象

from conf import settings

def register():
    with open(settings.DB_PATH, encoding='utf-8', mode='a+') as f1:
        f1.write('太白金星|123\n')