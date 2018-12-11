# class BMI():
#     def __init__(self, tizhong, shengao):
#         self.tizhong = tizhong
#         self.shengao = shengao
#
#         print(tizhong / shengao)
#
# p1 = BMI(62, 1.8)


# class Foo:
#     def __init__(self, name):
#         self.name = name
#
#     @property
#     def AAA(self):
#         print('get的时候运行我啊')
#
#     @AAA.setter
#     def AAA(self, value):
#         print(value)
#         print('set的时候运行我啊')
#
#     @AAA.deleter
#     def AAA(self):
#         print('delete的时候运行我啊')
#
# obj = Foo('alex')
# obj.name = '太白'
# print(obj.name)
#
# del obj.name
# print(obj.name)
# del obj.AAA



# class Product:
#     def __init__(self,name,  yuanshi, zhekou):
#         self.name = name
#         self.yuanshi = yuanshi
#         self.zhekou = zhekou
#
    # @property
#     def m(self):
#         return self.yuanshi ** self.zhekou
#
# a1 = Product('苹果', 5, 0.8)
# print(a1.m)


# import fs
#
# print(getattr(fs, 'n1'))
#
# ret = getattr(fs, 'func')
# ret()
#
#
# print(getattr(fs.A, 'name'))
# getattr(fs.A, 'func2')(None)



# 讨论__init__和 __new__先后执行顺序

# class A:
#     def __init__(self):
#         self.x = 1
#         print('in init')
#
#     def __new__(cls, *args, **kwargs):
#         print('in __new__')
#         return object.__new__(cls)
#
# obj = A()  # 01类名()先找__new__


#
# import random
# print(random.random())  # 随机在0~1之间的float
# print(random.uniform(1,10))  # 随机在1~10之间的浮点型
# print(random.randint(1,10))  # 1~10之间的整数
# print(random.randrange(1, 10, 2))  # 大于等于1且小于10之间的奇数
#
# print(random.choice([1, '23, [4, 5]']))  # 多选择一
# print(random.sample([1, '23, [4, 5]'], 2))  # 列表元素任意2个组合
# item = [1,2,3]