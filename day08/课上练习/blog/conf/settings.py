# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# ---------------------------- 此部分是 配置文件 ----------------------------
# 这里的配置文件需要写绝对路径，r的意思是转义

import os
import logging.config


base_dir = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(base_dir, 'register')
LOG_PATH = os.path.join(base_dir, 'log/access.log')
EXEC_PATH = os.path.join(base_dir, 'log/exec.log')


standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束

# log配置字典
# 第一层键值对的键固定的关键字不能改变。
LOGGING_DIC = {
    'version': 1, # 版本
    'disable_existing_loggers': False,  #
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'id_simple_format':{
                'format': id_simple_format
        }
    },
    'filters': {},  # 过滤器
    'handlers': {
        #打印到终端的日志
        'stream': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'file1': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': LOG_PATH,  # 日志文件
            'maxBytes': 300,  # 日志大小 300bytes
            'backupCount': 5, # 最多只有5个文件
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        'bosssb_file': {
            'level': 40,
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,轮训机制，只保留5份
            'formatter': 'id_simple_format',
            'filename': EXEC_PATH,  # 日志文件
            'maxBytes': 300,  # 日志大小 300bytes
            'backupCount': 5, # 最多只有5个文件
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },  # 操控者
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['file1', 'stream', 'bosssb_file'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}


