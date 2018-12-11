
# 将列表[0,1,0,3,2] ,排序为:[1,3,2,0,0]

l1 = [0,1,0,3,2]
l2 = []
l3 = []
# for i in l1:
#     if i > 0:l2.append(i)
#     else:l3.append(i)
# print(l2 + l3)


# 将字典与列表,进行组合, 字典的key:列表的值
# dic = {'key1': None, 'key2': None, 'key3': None}
# ls = [1, 2, 3]
# i = 0
# for j in range(len(ls)):
#     print('三遍j:', j)  #第0遍 0
#     for k in dic.keys():
#         # print('三遍key:',k)  # key1 ##key2
#         count = 0
#         for j in range(i, len(ls)):  # j=0 i= 0  len=0 1 2  ## j=1  i=1 count=1
#             if count < 1:
#                 dic[k] = ls[j]   # k = key1    j=0    ## k = key2     ## j=1
#                 count += 1       #j 0
#                 i += 1
#             else:
#                 break
# print(dic)
