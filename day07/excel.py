# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""


import xlwt
def write_excel():
    '''
    第二种方式，自动判断需要合并的单元格范围
    :return:
    '''
    table_head = ['部门','姓名','联系方式','入职时间','地址']
    content = [["测试部",'小王',15933333333,'2016-02-09',"四川，成都"],
               ["测试部",'小张',15933333334,'2017-02-09','四川，雅安'],
               ["测试部",'小李',15933333335,'2015-02-09','双流'],
               ["开发部",'小熊1',15933333336,'2012-02-09','华阳'],
               ["开发部",'小熊2',15933333337,'2014-12-31','华阳'],
               ["市场部",'小熊3',15933333338,'2014-02-09','华阳'] ]
    # 初始化workbook 并且添加excel Sheet
    workbook = xlwt.Workbook(encoding = 'utf-8')
    xlsheet = workbook.add_sheet("excel写入练习",cell_overwrite_ok=True)

    #写excel表头
    headlen = len(table_head)
    for i in range(headlen):
        xlsheet.write(0,i,table_head[i], set_style('Times New Roman',200))

        contentRow = len(content) #列表元素个数  = 待写入内容行数

    #从content获取要写入的第一列的内容,存入列表
    first_col = []
    for i in range(contentRow):
        first_col.append(content[i][0])
        print("first_col",first_col)

    # 去掉列表中重复元素，并且顺序不变
    nfirst_col = list(set(first_col))
    nfirst_col.sort(key=first_col.index)  # sort排序与原顺序一致
    print("nfirst_col",nfirst_col)

    row = 1
    for i in nfirst_col:
        count = first_col.count(i) # 计算元素的重复个数，比如测试 ：3
        uprange = row+count-1  #合并范围后的上行数
        xlsheet.write_merge(row,uprange,0,0,i) #合并单元格写入内容
        row = uprange+1 #从下一行开始写入

    #获取content子列表第二个元素，循环写入excel第2列到最后开始的数据
    for row in range(contentRow):
        for col in range(1,len(content[row])):
            xlsheet.write(row+1,col,content[row][col])
    workbook.save('excel.xls')

