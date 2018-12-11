'''
import 模块 发生了三件事：
1，在内存中开辟一个名称空间aaa
2，自动将包下面的__init__文件中代码加载到内存。
3， 通过aaa. 获取模块中的对象。
'''
# import  from ... import ...
# import aaa  # 实际引用的 aaa 下面的__init__文件
# print(aaa.x)
# # print(aaa.y)
# # print(aaa.z)

# 可以
# from aaa import m1
# m1.func1()


# import aaa
# aaa.m1.func1()
# from aaa.m1 import func1
# func1()
# import sys
# print(sys.path)
# sys.path.pop(1)
# print(sys.path)

# import aaa
# aaa.m1.func1()


# 引用bbb
# import aaa
# print(aaa.bbb)

# import aaa
# print(aaa.bbb.xx)
# print(aaa.bbb.oo)

# import aaa
# aaa.bbb.m2.func2()


# 总结：
# 执行文件！！的当前目录是在sys.path的第一个参数。
# 所以当前目录的文件可以直接import。
# 无论怎么样导入文件import 还是 from ... import ... 一定是从执行文件当前目录开始。


# 模块的分发

# import NB as nb
# nb.f1()
# nb.f2()
# nb.f3()
# nb.f4()
# nb.f5()
# nb.f6()

# 相对导入，绝对导入

#

# 包的总结：
# 如果要是 from 包.包.包（执行文件同一个目录，sys.path） import ... 那么 __init__ 可以不用任何操作
# .的左边一定是包
# 如果你是 import 包  __init__ 必须要各种写。


