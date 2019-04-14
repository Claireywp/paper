# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 18:09:28 2018

@author: hasee
"""

#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
from __future__ import print_function
import pandas as pd
from random import randrange
import random
import numpy as np
from scipy import stats
import matplotlib.pylab as plt
import statsmodels as sms
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from statsmodels.graphics.tsaplots import  plot_acf,plot_pacf
#from pandas.core import datetools

#时间序列建模的步骤：
#１获取被观测系统时间序列数据；
#２对数据绘图，观测是否为平稳时间序列（均值和方差是常量）；对于非平稳时间序列要先进行d阶差分运算，化为平稳时间序列；
#３经过第二步处理，已经得到平稳时间序列。要对平稳时间序列分别求得其自相关系数ACF 和偏自相关系数PACF ，
#通过对自相关图和偏自相关图的分析，得到最佳的阶层 p 和阶数 q
#由以上得到的d、q、p
#４，得到ARIMA模型。然后开始对得到的模型进行模型检验。
'''
dta=[10930,10318,10595,10972,7706,6756,9092,10551,9722,10913,11151,8186,6422,
6337,11649,11652,10310,12043,7937,6476,9662,9570,9981,9331,9449,6773,6304,9355,
10477,10148,10395,11261,8713,7299,10424,10795,11069,11602,11427,9095,7707,10767,
12136,12812,12006,12528,10329,7818,11719,11683,12603,11495,13670,11337,10232,
13261,13230,15535,16837,19598,14823,11622,19391,18177,19994,14723,15694,13248,
9543,12872,13101,15053,12619,13749,10228,9725,14729,12518,14564,15085,14722,
11999,9390,13481,14795,15845,15271,14686,11054,10395]
'''
dta=[]
for i in range(90):
     dta.append(random.uniform(0.48,0.9))
print (len(dta))
dta=pd.Series(dta)
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('1','90'))
dta.plot(figsize=(12,8))

#时间序列的差分
#ARIMA 模型对时间序列的要求是平稳型（宽平稳过程是指随机过程的均值函数是个常量，自相关函数是只与时间差有关），因此，当我们研究时间序列很重要的
#一个应用（或者出发点），是希望通过时间序列的历史数据来得到其未来的一些预测。换句话说，我们希望时间序列在历史数据上的一些性质，在将来保持不变。
#所以你得到一个非平稳的时间序列时，首先要做的即是做时间序列的差分，直到得到一个平稳时间序列。如果你对时间序列做d次差分才能得到一个平稳序列，
#那么可以使用ARIMA(p,d,q)模型，其中d是差分次数。
#plt.show()
#fig=plt.figure(figsize=(12,8))
#ax1=fig.add_subplot(111)
#diff1=dta.diff(1)
#diff1.plot(ax=ax1)
#plt.show()
#fig=plt.figure(figsize=(12,8))
#ax2=fig.add_subplot(111)
#diff2=dta.diff(2)
#diff2.plot(ax=ax2)
#plt.show()


dta=dta.diff(1)
data=pd.DataFrame(dta,columns=['B'],index=sm.tsa.datetools.dates_from_range('2','90'))
#print(data)
fig=plt.figure(figsize=(12,8))#创建图纸（大小为１２＊８）
ax1=fig.add_subplot(211)#在图纸中创建子图（２行×１列×子图序号１）ax1=第一个子图（其中axes就是子图的意思）
plot_acf(data,ax=ax1,lags=1)

ax2=fig.add_subplot(212)#在图纸中创建子图（２行×１列×子图序号２）ax2=第二个子图
plot_pacf(data,ax=ax2,lags=1)

arma_mod20 = sm.tsa.ARMA(data,(7,0)).fit()
#print(arma_mod20.aic,arma_mod20.bic,arma_mod20.hqic)
#arma_mod30 = sm.tsa.ARMA(data,(0,1)).fit()
#print(arma_mod30.aic,arma_mod30.bic,arma_mod30.hqic)
#arma_mod40 = sm.tsa.ARMA(data,(7,1)).fit()
#print(arma_mod40.aic,arma_mod40.bic,arma_mod40.hqic)
#arma_mod50 = sm.tsa.ARMA(data,(8,0)).fit()
#print(arma_mod50.aic,arma_mod50.bic,arma_mod50.hqic)
resid=arma_mod20.resid
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = plot_acf(resid.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = plot_pacf(resid, lags=40, ax=ax2)
print(sm.stats.durbin_watson(arma_mod20.resid.values))
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)
r,q,p = sm.tsa.acf(resid.values.squeeze(), qstat=True)
data = np.c_[range(1,41), r[1:], q, p]
table = pd.DataFrame(data, columns=['lag', "AC", "Q", "Prob(>Q)"])
print(table.set_index('lag'))
predict_sunspots = arma_mod20.predict('2100', '2110', dynamic=True)
print(predict_sunspots)
fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.ix['2011':].plot(ax=ax)
predict_sunspots.plot(ax=ax)
plt.show()