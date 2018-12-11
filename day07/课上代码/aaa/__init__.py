# print('in aaa __init__')
x = 1
y = 2
z = 3333

# import m1  # 直接引用不到 m1

from aaa import m1  # 这样可以

# m1 = '名称空间'

# bbb = 'alex'

from aaa import bbb