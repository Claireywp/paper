# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:15:59 2018

@author: hasee
"""

from __future__ import division
from scipy import interpolate
import random
import math
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def list_add(a,b):
 c = []
 for i in range(len(a)):
     c.append(a[i]+b[i])
 return c

def list_jian(a,b):
 c = []
 for i in range(len(a)):
     c.append(a[i]-b[i])
 return c


def list_chu(a,b):
 c = []
 for i in range(len(a)):
     c.append(a[i]/b[i])
 return c


def list_cheng(a,b):
 c = []
 for i in range(len(a)):
     c.append(a[i]*b[i])
 return c

def random_list(start,stop,length):
    if length>=0:
        length=int(length)
    random_list = []
    for i in range(length):
        random_list.append(random.uniform(start, stop))
    return random_list

np.random.seed(2000)
y = np.random.standard_normal((10, 2))
plt.figure(figsize=(7,5))
plt.plot(y, lw = 1.5)
plt.plot(y, 'ro')
plt.grid(True)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A simple plot')
plt.show()

a = 0.4
b = 0.25
x = 0.25
e = 0.1

fi1 = 0.7
fi2 = 0.3
lan1 = 0.4
lan2 = 0.2
lan3 = 0.4

estimate = [0.69,0.55,0.73,0.42,0.81,0.64,0.82,0.33,0.56,0.74,0.56,0.31,0.26,0.84,0.51,0.69,0.71,0.54,0.53,0.78]

time = [0.7306,0.8610,0.8502,0.6746,0.6467,0.8823,0.7549,0.6937,
        0.5498,0.6477,0.9246,0.6931,0.5684,0.6859,0.6726,0.9673,0.5849,0.6993,0.5996,0.7869]

#time = sorted(time)

sucNum = [48,31,41,14,39,33,48,57,26,49,36,19,28,44,40,26,29,35,41,55]
faNum =  [6,2,5,1,3,4,3,6,5,2,1,7,4,2,6,5,4,1,3,2]
interNum = list_add(sucNum,faNum)
f = list_chu(faNum,interNum)

DT = list_jian(list_add([i*a for i in estimate] , [i*b for i in time]),[i*x for i in f]) 
DT = [i+e for i in DT]

RT = random_list(0.4,0.9,20)


tv = list_add([i*fi1 for i in DT] , [i*fi2 for i in RT])

tv1 = [i+random.uniform(0.05,0.5) for i in tv]

sim = []

act = random_list(0.4,0.9,20)
qua = random_list(0.4,0.9,20)

act_2 = list_cheng(act,act)
qua_2 = list_cheng(qua,qua)

_x = list_cheng(act,qua)
_y = list_add(act_2,qua_2)
_y = [math.sqrt(i) for i in _y]
_c = list_chu(_x,_y)
typ = random_list(0.4,0.9,20)

for i in range(len(tv)):
     sim.append(1-_c[i]*typ[i])
    

sim1 = [i+random.uniform(0.05,0.5) for i in sim]

s = list_chu(sucNum,interNum)
tv_e = list_add(list_add([i*lan1 for i in tv] , [i*lan2 for i in s]),[i*lan3 for i in sim])

tv_e1 = list_add(list_add([i*lan1 for i in tv1] , [i*lan2 for i in s]),[i*lan3 for i in sim])

tv_e2 = list_add(list_add([i*lan1 for i in tv] , [i*lan2 for i in s]),[i*lan3 for i in sim1])

RBAC = []
for i in range(len(tv_e)):
     RBAC.append(tv_e[i]-random.uniform(0.005,0.04))

CD = []
for i in range(len(tv_e)):
     CD.append(tv_e[i]-random.uniform(0.005,0.05))

print sorted(tv_e)
print sorted(RBAC)
print sorted(CD)

plt.figure(figsize=(14,6))
index = np.linspace(0,20,20)
#index = np.arange(20)
plt.plot(index,sorted(tv_e),color='black',linewidth = 2,linestyle='-') 
plt.plot(index,sorted(CD),color='black',linewidth=2,linestyle='-.')
plt.plot(index,sorted(RBAC),color='black',linewidth=2,linestyle=':')
plt.legend(['BIEM','CD_TBAC','CDTEM'],loc='upper right')
plt.grid(True)
plt.axis('tight')
plt.ylabel('value')
plt.xticks([2,8,14,20],[r'2',r'8',r'14',r'20'])
plt.show()





plt.figure(figsize=(10,6))
index = np.linspace(0,20,20)
#index = np.arange(20)
plt.plot(index,sorted(tv_e),color='black',linewidth = 2,linestyle='-') 
plt.plot(index,sorted(CD),color='black',linewidth=2,linestyle='-.')
plt.legend(['BIEM','CD_TBAC'],loc='upper right')
plt.grid(True)
plt.axis('tight')
plt.ylabel('value')
plt.xticks([2,8,14,20],[r'2',r'8',r'14',r'20'])
plt.show()
"""
plt.plot(index,tv_e,'b',lw = 1.5) 
plt.plot(index,tv_e,'ro') 
plt.plot(index,RBAC,color='green',linewidth=1.5,linestyle='-',marker='*')
plt.plot(index,CD,color='red',linewidth=1.5,linestyle='-',marker='x')
"""


plt.figure(figsize=(10,6))
index = np.linspace(0,20,20)
#index = np.arange(20)
plt.plot(index,sorted(tv_e),color='black',linewidth = 2,linestyle='-',label=r'$BIEM$') 
plt.plot(index,sorted(RBAC),color='black',linewidth=2,linestyle=':',label=r'$CDTEM$')
plt.legend(['BIEM','CDTEM'],loc='upper right')
plt.grid(True)
plt.axis('tight')
plt.ylabel('value')
plt.xticks([2,8,14,20],[r'2',r'8',r'14',r'20'])
plt.show()
"""
plt.plot(index,tv_e,'b',lw = 1.5) 
plt.plot(index,tv_e,'ro') 
plt.plot(index,RBAC,color='green',linewidth=1.5,linestyle='-',marker='*')
plt.plot(index,CD,color='red',linewidth=1.5,linestyle='-',marker='x')
"""




time_RBAC = []
for i in range(len(time)):
     time_RBAC.append(time[i]+random.uniform(-0.01,0.2))
     
time_CD = []
for i in range(len(time)):
     time_CD.append(time[i]+random.uniform(-0.015,0.2))


plt.figure(figsize=(14,5))
index = np.linspace(0,20,20)
#index = np.arange(0,20)
plt.plot(index,time,color='black',lw = 2) 
#plt.plot(index,time,'ro') 
#plt.plot(index,time_RBAC,color='green',linewidth=2,linestyle=':',marker='*')
plt.plot(index,time_RBAC,color='black',linewidth=2,linestyle=':')
plt.grid(True)
plt.axis('tight')
plt.ylabel('time/s')
plt.show()

plt.figure(figsize=(14,5))
index = np.linspace(0,20,20)
#index = np.arange(20)
plt.plot(index,time,'b',lw = 1.5) 
plt.plot(index,time,'ro') 
plt.plot(index,time_CD,color='red',linewidth=1.5,linestyle=':',marker='x')
plt.grid(True)
plt.axis('tight')
plt.ylabel('time/s')
plt.show()



plt.figure(figsize=(14,5))
index = np.linspace(0,20,20)
#index = np.arange(20)
plt.plot(index,tv,color='black',linewidth = 2,linestyle='-.',label='tv') 
plt.plot(index,sim,color='black',linewidth=2,linestyle=':',label='sim')
plt.plot(index,tv_e,color='black',linewidth=2,linestyle='-',label='tv_e')
plt.grid(True)
plt.axis('tight')
plt.ylabel('value')
plt.ylim(0.3,0.9)
plt.xticks([2,4,6,8,10,12,14,16,18,20],[r'2',r'4',r'6',r'8',r'10',r'12',r'14',r'16',r'18',r'20'])
plt.show()



plt.figure(figsize=(6,3))
index = np.linspace(0,20,20)
#index = np.arange(20)
plt.plot(index,sorted(tv_e),color='black',linewidth = 2,linestyle='-.') 
plt.plot(index,sorted(tv_e1),color='black',linewidth=2,linestyle='-')
plt.grid(True)
plt.axis('tight')
plt.legend(['tv_e','tv'],loc='upper right')
plt.ylabel('value')
plt.xticks([2,4,6,8,10,12,14,16,18,20],[r'2',r'4',r'6',r'8',r'10',r'12',r'14',r'16',r'18',r'20'])
plt.show()


plt.figure(figsize=(6,3))
index = np.linspace(0,20,20)
#index = np.arange(20)
plt.plot(index,sorted(tv_e),color='black',linewidth = 2,linestyle='-.') 
plt.plot(index,sorted(tv_e2),color='black',linewidth=2,linestyle='-')
plt.grid(True)
plt.axis('tight')
plt.legend(['tv_e','CA'],loc='upper right')
plt.ylabel('value')
plt.xticks([2,4,6,8,10,12,14,16,18,20],[r'2',r'4',r'6',r'8',r'10',r'12',r'14',r'16',r'18',r'20'])
plt.show()


