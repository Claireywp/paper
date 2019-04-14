# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:15:07 2018

@author: hasee
"""

import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['0', '2', '5', '8', '11','14','17','20']
x = range(len(names))
y = [0,0.19,0.26,0.34,0.42,0.48,0.5,0.52]
y1=[0,0.16,0.24,0.32,0.4,0.43,0.48,0.49]
y2=[0,0.15,0.26,0.31,0.35,0.42,0.45,0.48]
y3=[0,0.14,0.24,0.3,0.32,0.35,0.41,0.435]
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围
plt.figure(figsize=(12,6))
plt.plot(x, y, marker='o',color = 'k',ms=8,label=u'原始误差率')
plt.plot(x, y1, marker='v',color = 'k',ms=8,label=u'添加推荐信任度参数')
plt.plot(x, y2, marker='+', color = 'k',ms=10,label=u'添加上下文参数')
plt.plot(x, y3, marker='x', color = 'k',ms=10,label=u'基于Beta分布的改进信任模型')
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.01)
font2 = {'family': 'SimHei',
         'weight': 'normal',
         'size': 15,
         }
plt.xlabel(u"时间段",font2) #X轴标签
plt.ylabel(u"误差率",font2) #Y轴标签
#plt.title("A simple plot") #标题
plt.savefig('temp.jpg')
plt.show()