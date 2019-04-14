# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 20:53:29 2018

@author: hasee
"""

import matplotlib.pyplot as plt
import numpy as np
import xlrd


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\Users\hasee\Desktop\TU1.xls')
    # 获取所有sheet
    print workbook.sheet_names() # [u'sheet1', u'sheet2']
    #获取sheet2
    sheet2_name= workbook.sheet_names()[0]
    print sheet2_name
    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_name('Sheet1')
    # sheet的名称，行数，列数
    print sheet2.name,sheet2.nrows,sheet2.ncols
    # rows = sheet2.row_values(1) # 获取第四行内容
    cols = sheet2.col_values(1) # 获取第三列内容
    # print rows
    print cols
    #获取单元格内容的三种方法
    #print sheet2.cell(1,0).value.encode('utf-8')
    #print sheet2.cell_value(1,0).encode('utf-8')
    #print sheet2.row(1)[0].value.encode('utf-8')
    # 获取单元格内容的数据类型
    #print sheet2.cell(1,3).ctype
if __name__ == '__main__':
    read_excel()

workbook = xlrd.open_workbook(r'C:\Users\hasee\Desktop\TU1.xls')
sheet2 = workbook.sheet_by_name('Sheet1')
cols1 = sheet2.col_values(1)
cols2 = sheet2.col_values(4)
N=50
#y=[20,10,30,25,15]
#y1=np.random.randint(10,50,5)
#x=np.random.randint(10,1000,N)
y = cols1[1:]
y1 = cols2[1:]

index=np.arange(N)
plt.bar(left=index,height=y,color='red',width=0.3)
plt.bar(left=index+0.3,height=y1,color='black',width=0.3)
plt.show()
