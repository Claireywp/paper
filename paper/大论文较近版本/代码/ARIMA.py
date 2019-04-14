# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 16:22:27 2018

@author: hasee
"""

from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot


dta=[10930,10318,10595,10972,7706,6756,9092,10551,9722,10913,11151,8186,6422, 
6337,11649,11652,10310,12043,7937,6476,9662,9570,9981,9331,9449,6773,6304,9355, 
10477,10148,10395,11261,8713,7299,10424,10795,11069,11602,11427,9095,7707,10767, 
12136,12812,12006,12528,10329,7818,11719,11683,12603,11495,13670,11337,10232, 
13261,13230,15535,16837,19598,14823,11622,19391,18177,19994,14723,15694,13248, 
9543,12872,13101,15053,12619,13749,10228,9725,14729,12518,14564,15085,14722, 
11999,9390,13481,14795,15845,15271,14686,11054,10395]


dta=pd.Series(dta) #Series结构是基于NumPy的ndarray结构，是一个一维的标签矩阵
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2011','2100'))
print ("基本数据图片")
dta.plot(figsize=(12,8))

# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
#figure(figsize=(8,6), dpi=80)

fig = plt.figure(figsize=(12,8))
ax1= fig.add_subplot(111)
diff1 = dta.diff(1)
print ("时间序列的差分d")
diff1.plot(ax=ax1)