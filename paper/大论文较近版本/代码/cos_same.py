# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 15:48:07 2018

@author: hasee
"""
import math

def cos(vector1,vector2):  
    dot_product = 0.0;  
    normA = 0.0;  
    normB = 0.0;  
    for a,b in zip(vector1,vector2):  
        dot_product += a*b  
        normA += a**2  
        normB += b**2  
    if normA == 0.0 or normB==0.0:  
        return None  
    else:  
        return dot_product / ((normA*normB)**0.5)  
      
      
v1=(-2,3,-1,4,5,0,1,-4,0,2);  
v2=(4,-1,0,4,5,-2,1,3,-4,0);  
print cos(v1,v2);  
  
v3=(2,-3,-1,-1,1,0,5,2,-2,-4);  
v4=(4,-1,0,4,5,-2,1,3,-4,0);  
print cos(v3,v4);


v5=(0.7,0.6);
v6=(0.5,0.8);
print cos(v5,v6); 
print cos(v5,v6)*0.3;  
         
x=[1,2,3];  
y=[4,5,6];  
z=[7,8,9];  
print zip(x,y,z);  
         
         
         
def distance(vector1,vector2):  
    d=0;  
    for a,b in zip(vector1,vector2):  
        d+=(a-b)**2;  
    return d**0.5;  
      
v1=(1,1,1);  
v2=(-1,-1,-1);  
print distance(v1,v2);  
  
v3=(1,1);  
v4=(-1,-1);  
print distance(v3,v4);  