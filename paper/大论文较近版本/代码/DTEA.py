# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:28:27 2018

@author: Administrator
"""

from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
import datetime


starttime = datetime.datetime.now()


dta=[0.615,0.006,0.332,0.251,0.123,0.649,0.414,0.316,0.13,0.414,
     0.743,0.845,0.741,0.315,0.669,0.096,0.737,0.497,0.159,0.173,
     0.644,0.337,0.865,0.739,0.035,0.029,0.141,0.545,0.295,0.253,
     0.437,0.812,0.709,0.511,0.102,0.501,0.485,0.889,0.437,0.815,
     0.325,0.075,0.18,0.444,0.188,0.416,0.502,0.763,0.485,0.23,0.341,
     0.123,0.223,0.279,0.153,0.73,0.837,0.798,0.749,0.302,0.501,0.938,
     0.516,0.94,0.195,0.207,0.55,0.347,0.025,0.305,0.165,0.303,0.628,
     0.167,0.486,0.853,0.163,0.084,0.638,0.115,0.193,0.927,0.812,0.214,
     0.359,0.346,0.417,0.109,0.207,0.136]

dta=np.array(dta,dtype=np.float)
dta=pd.Series(dta)
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2001','2090'))
dta.plot(figsize=(12,8))



sm.graphics.tsa.plot_acf(dta).show()

from statsmodels.tsa.stattools import adfuller as ADF
print(ADF(dta))


fig = plt.figure(figsize=(12,8))
ax1= fig.add_subplot(111)
diff1 = dta.diff(1)
diff1.plot(ax=ax1)


fig = plt.figure(figsize=(12,8))
ax2= fig.add_subplot(111)
diff2 = dta.diff(2)
diff2.plot(ax=ax2)


fig = plt.figure(figsize=(12,8))
ax3= fig.add_subplot(111)
diff3 = dta.diff(3)
diff3.plot(ax=ax3)



diff1 = dta.diff(2)#我们已经知道要使用一阶差分的时间序列，之前判断差分的程序可以注释掉
fig = plt.figure(figsize=(12,8))
ax1=fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta,lags=40,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta,lags=40,ax=ax2)

#
arma_mod70 = sm.tsa.ARMA(dta,(7,0)).fit()
print(arma_mod70.aic,arma_mod70.bic,arma_mod70.hqic)
arma_mod30 = sm.tsa.ARMA(dta,(0,1)).fit()
print(arma_mod30.aic,arma_mod30.bic,arma_mod30.hqic)
arma_mod71 = sm.tsa.ARMA(dta,(7,1)).fit()
print(arma_mod71.aic,arma_mod71.bic,arma_mod71.hqic)
arma_mod80 = sm.tsa.ARMA(dta,(8,0)).fit()
print(arma_mod80.aic,arma_mod80.bic,arma_mod80.hqic)


resid = arma_mod70.resid

fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)
plt.show()


print(sm.stats.durbin_watson(arma_mod70.resid.values))


resid = arma_mod70.resid#残差
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)


r,q,p = sm.tsa.acf(resid.values.squeeze(), qstat=True)
data = np.c_[range(1,41), r[1:], q, p]
table = pd.DataFrame(data, columns=['lag', "AC", "Q", "Prob(>Q)"])
print(table.set_index('lag'))

#预测
predict_sunspots = arma_mod70.predict('2090', '2100', dynamic=True)
print(predict_sunspots)
fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.ix['2000':].plot(ax=ax)
fig = arma_mod70.plot_predict('2090', '2100', dynamic=True, ax=ax, plot_insample=False)
plt.show()

predict_sunspots.plot(ax=ax)

"""
predict_sunspots = arma_mod20.predict('2090', '2100', dynamic=True)
print(predict_sunspots)
fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.ix['2001':].plot(ax=ax)
predict_sunspots.plot(ax=ax)
"""


endtime = datetime.datetime.now()

print (endtime - starttime).seconds