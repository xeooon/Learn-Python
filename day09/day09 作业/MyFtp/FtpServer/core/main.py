# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

import optparse  # 参数处理模块


# class ArgvHandler(object):
#     def __init__(self):
#         self.parser = optparse.OptionParser()
#         parser.add_option("-s", "--host", dest="host", help="服务器端需要绑定一个IP地址")
#         parser.add_option("-p", "--port", dest="port", help="服务器端需要绑定一个端口")
#         (optparse, args) = self.parser.parse_args()
#
#         print(optparse, args)


class ArgvHandler(object):
    def __init__(self):
        self.parser = optparse.OptionParser()
        (options, args) = self.parser.parse_args()  # 只要start方法，其余在列表里面

        print(options, args)  # {} ['asdf']
