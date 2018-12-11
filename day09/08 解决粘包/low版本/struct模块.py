# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

import struct
# 将不固定长度的数字 ---> 固定的bytes
ret = struct.pack('i', 151988)
# ret = struct.pack('q',1519324324424324324324324)  # 数据量大了就不可以
print(ret, type(ret), len(ret), sep='\n')
# 返回的结果：
# b'\xb4Q\x02\x00'
# <class 'bytes'>
# 4



# 固定的bytes --->  转为不固定长度的数字
# ret = struct.pack('i', 151988)
# ret1 = struct.unpack('i', ret)[0]  # 是一个元组格式 (151988,)
# print(ret1)  # 151988




