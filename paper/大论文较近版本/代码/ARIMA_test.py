# -*- coding: utf-8 -*-
"""
Created on Fri Feb 01 19:25:14 2019

@author: Hasee
"""

import matplotlib.pyplot as plt
import pandas as pd

dta=pd.read_excel('./ARIMA_test2.xls', index_col = 'time_new')
data = dta['tv_in']

"""
data=[0.434,0.615,0.216,0.604,0.958,0.37,0.308,0.5,0.839,0.502,0.192,0.082,
     0.905,0.418,0.521,0.16,0.564,0.602,0.077,0.496,0.892,0.565,0.284,0.301,
     0.608,0.678,0.558,0.784,0.391,0.692,0.515,0.241,0.556,0.459,0.989,0.829,
     0.352,0.616,0.9,0.341,0.722,0.89,0.073,0.523,0.601,0.618,0.196,0.777,0.523,
     0.657,0.822,0.006,0.723,0.924,0.336,0.145,0.19,0.491,0.066,0.928,0.369,
     0.769,0.16,0.431,0.263,0.382,0.005,0.798,0.53,0.409,0.534,0.43,0.956,0.426,
     0.784,0.04,0.009,0.652,0.326,0.452,0.327,0.111,0.696,0.603,0.167,0.945,
     0.688,0.261,0.663,0.548]
"""
plt.plot(figsize=(20,8))
plt.plot(data)
plt.show()

#自相关图
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(data).show()

#偏自相关图
from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(data).show()


#平稳性检测
from statsmodels.tsa.stattools import adfuller as ADF
print('原始序列的ADF检验结果为：')
print(ADF(data))


#白噪声检验
from statsmodels.stats.diagnostic import acorr_ljungbox
print('差分序列的白噪声检验结果为：')
print(acorr_ljungbox(data, lags=1))



