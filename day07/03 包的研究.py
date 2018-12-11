# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# import  from ... import ...
# import aaa  # 实际引用的 aaa 下面的__init__文件
# print(aaa.x)  # 返回 1
# print(aaa.y)  # 返回 2
# print(aaa.z)  # 返回 3333


# 总结：
# 执行文件！！的当前目录是在sys.path的第一个参数。
# 所以当前目录的文件可以直接import。
# 无论怎么样导入文件import 还是 from ... import ... 一定是从执行文件当前目录开始。




'''
模块的分发
比如之前已经写好了，但是原有模块更改了，又不能影响线上的调用方式，所以需要用到模块的分发
'''

# import nb
# nb.f1()
# nb.f2()
# nb.f3()
# nb.f4()
# nb.f5()
# nb.f6()


'''
包的总结：
'''
# 如果要是 from 包.包.包（执行文件同一个目录，sys.path） import ... 那么 __init__ 可以不用任何操作
# .的左边一定是包
# 如果你是 import 包  __init__ 必须要各种写。