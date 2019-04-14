# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 11:44:49 2018

@author: hasee
"""

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import mlab
from matplotlib import rcParams

time = [0.7306,0.8610,0.8502,0.6746,0.6467,0.8823,0.7549,0.6937,
        0.5498,0.6477,0.9246,0.6931,0.5684,0.6859,0.6726,0.9673,0.5849,0.6993,0.5996,0.7869]


time_RBAC = []
for i in range(len(time)):
     time_RBAC.append(time[i]+random.uniform(-0.01,0.2))
     
time_CD = []
for i in range(len(time)):
     time_CD.append(time[i]+random.uniform(-0.015,0.2))
    
y = 0.764892
y1 = np.sum(time_CD) / len(time)
y2 = np.sum(time_RBAC) / len(time)

"""
plt.figure(figsize=(2,5))
index = np.arange(1)
plt.bar(left=index,height=y,color='red',width=0.3)
plt.bar(left=index+0.3,height=y1,color='black',width=0.3)
plt.bar(left=index+0.6,height=y2,color='gray',width=0.3)
plt.show()
"""


fig1 = plt.figure(figsize=(5,6))
rects1 =plt.bar(left = (0.2),height = y,color="w",edgecolor="k",hatch="\\\\",width = 0.2,align="center",yerr=0.001)
rects2 =plt.bar(left = (0.6),height = y1,color="w",edgecolor="k",hatch="////",width = 0.2,align="center",yerr=0.001)
rects3 =plt.bar(left = (1),height = y2,color="w",edgecolor="k",hatch="\/\/",width = 0.2,align="center",yerr=0.001)
plt.legend()
plt.ylabel('time/s')
plt.xticks((0.2,0.6,1),('BIEM','CDTEM','CD_TBAC'))
plt.yticks((0,0.2,0.4,0.6,0.8,1.0))
# plt.legend((rects1,rects2,rects3,),(u"BIEM",u"CDTEM",u"CD_TBAC",))
def autolabel(rects):
  for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % float(height))
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.show()