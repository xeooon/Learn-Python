# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# 集合:{1,2,3}
# 集合里面的元素必须是不可变的数据类型,集合本身是可变数据类型
# print({[1, 2, 3], {'name': 'barry'}})

# 集合是无序的,不重复的

# 1.列表去重
# l1 = [1, 1, 2, 3, 4, 3, 2, 4, 5, 6]
# set1 = set(l1)
# l1 = list(set1)
# print(l1)


# 2.关系测试
# 交集，并集，差集,.....
# set1 = {'alex', 'WuSir', 'barry', '女神',}
# for i in set1:
#     print(i)



'''
浅copy
第一层开辟新的内存地址,但是从第二层乃至更深的层来说,共用的都是一个内存地址.
'''

# age1 = 12
# age2 = age1
# print(age1, age2)

# l1 = ['alex', 'wusir', 'barry', '女神']
# l2 = l1
# l1.append('日天')
# print(l1)
# print(l2)


# l1 = ['alex', 'wusir', 'barry', '女神', [1, 2, 3]]
# l2 = l1.copy()
# l1[-1].append('女神')
#
# print(l1, id(l1), id(l1[-1]))
# print(l2, id(l2), id(l2[-1]))


# l1 = ['alex', 'wusir', 'barry', '女神', [1, 2, 3]]
# l2 = l1.copy()
# l1[0] = 'SB'
#
# print(l1, id(l1), id(l1[-1]))
# print(l2, id(l2), id(l2[-1]))

'''

深copy
复制两个完全独立的数据(多少层都是独立的)
'''
# import copy
# l1 = ['alex', 'wusir', 'barry', '女神', [1, 2, 3]]
# l2 = copy.deepcopy(l1)
# l1[-1].append('女神')
# print(l1, '第一层列表', id(l1), '第二层列表', id(l1[-1]))
# print(l2, '第一层列表', id(l2), '第二层列表', id(l1[-2]))
