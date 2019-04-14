# -*- coding: utf-8 -*-
"""
Created on Fri Feb 01 16:02:31 2019

@author: Hasee
"""


from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

dta=[0.434,0.822,0.772,0.49,0.796,0.407,0.912,0.574,
     0.161,0.364,0.764,0.902,0.52,0.577,0.824,0.023,
     0.893,0.332,0.812,0.661,0.532,0.65,0.792,0.788,
     0.519,0.044,0.131,0.759,0.241,0.558,0.695,0.173,
     0.255,0.073,0.78,0.024,0.039,0.08,0.115,0.477,0.558,
     0.137,0.246,0.112,0.052,0.563,0.374,0.264,0.066,0.18,
     0.58,0.315,0.192,0.34,0.275,0.612,0.082,0.195,0.429,
     0.542,0.62,0.036,0.618,0.257,0.692,0.079,0.63,0.329,
     0.924,0.126,0.932,0.051,0.533,0.444,0.081,0.938,0.155,
     0.74,0.474,0.886,0.075,0.207,0.148,0.266,0.2,0.085,0.873,
     0.081,0.91,0.337,0.221,0.449,0.428,0.035,0.822,0.17,0.934,
     0.754,0.904,0.062,0.933,0.754,0.532,0.692,0.282,0.241,0.576,
     0.534,0.869,0.929,0.656,0.575,0.812,0.552,0.029,0.606,0.324,
     0.86,0.805,0.615,0.64,0.404,0.88,0.844,0.374,0.488,0.253,0.404,
     0.571,0.353,0.623,0.534,0.192,0.036,0.49,0.632,0.886,0.755,
     0.198,0.634,0.09,0.273,0.441,0.178,0.723,0.675,0.864,0.268,
     0.902,0.096,0.788,0.29,0.382,0.788,0.497,0.055,0.13,0.878,
     0.027,0.625,0.844,0.663,0.037,0.677,0.532,0.56,0.215,0.282,
     0.758,0.09,0.745,0.35,0.704,0.818,0.41,0.642,0.75,0.022,0.534,
     0.861,0.348,0.546,0.399,0.141,0.705,0.814,0.489,0.02,0.675,0.228,
     0.45,0.12,0.81,0.213,0.491,0.697,0.641,0.666,0.713,0.115]

#print(len(dta))
#len(dta)=90

dta=np.array(dta,dtype=np.float)
dta=pd.Series(dta)
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('1','200'))
dta.plot(figsize=(12,8))



sm.graphics.tsa.plot_acf(dta).show()

from statsmodels.tsa.stattools import adfuller as ADF
print(ADF(dta))


fig = plt.figure(figsize=(12,8))
ax1= fig.add_subplot(111)
diff1 = dta.diff(1)
diff1.plot(ax=ax1)


#fig = plt.figure(figsize=(12,8))
#ax2= fig.add_subplot(111)
#diff2 = dta.diff(2)
#diff2.plot(ax=ax2)


diff1 = dta.diff(1)#我们已经知道要使用一阶差分的时间序列，之前判断差分的程序可以注释掉
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


resid = arma_mod80.resid

fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)
plt.show()


print(sm.stats.durbin_watson(arma_mod80.resid.values))


resid = arma_mod70.resid#残差
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)


r,q,p = sm.tsa.acf(resid.values.squeeze(), qstat=True)
data = np.c_[range(1,41), r[1:], q, p]
table = pd.DataFrame(data, columns=['lag', "AC", "Q", "Prob(>Q)"])
print(table.set_index('lag'))

#预测
predict_sunspots = arma_mod80.predict('200', '210', dynamic=True)
print(predict_sunspots)
fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.ix['0':].plot(ax=ax)
fig = arma_mod80.plot_predict('200', '210', dynamic=True, ax=ax, plot_insample=False)
plt.show()

predict_sunspots.plot(ax=ax)