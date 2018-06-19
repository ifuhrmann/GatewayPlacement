# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 06:09:54 2018

@author: Iddo
"""

import pylab as pl
import numpy as np
import math
import random 
import matplotlib 

X=[[],[]]
n=100
for x in range(0,n):
    X[0].append(random.random()*100)
    X[1].append(random.random()*100)

ax=0
ay=0
for i in range(0,len(X[0])):
   ax+=X[0][i]
   ay+=X[1][i]
ax/=len(X[0])
ay/=len(X[1])

AvgX=[ax]
AvgY=[ay]

pl.plot(AvgX,AvgY,".r")
pl.plot(X[0],X[1],".k")
pl.show()

S=[]
M=[]
k=3

for i in range(0,k):
    S.append( [ [],[] ] )
    M.append([])
    M.append([])
    M[0].append(random.random()*100)
    M[1].append(random.random()*100)
    
flag=0
while(flag==0): #initialize gateway positions flag should re-generate stuff if there's an empty set (doesn't do that now)
    for i in range(0,n):
        dMin=10**50
        jMin=0
        for j in range(0,k):
            d=math.sqrt( (X[0][i]-M[0][j])**2 + (X[1][i]-M[1][j])**2 )
            if(d<dMin):
                dMin=d
                jMin=j
        S[jMin][0].append( X[0][i] )
        S[jMin][1].append( X[1][i] )
    flag=1


pl.plot(M[0],M[1],".k")
for i in range(0,k):
    pl.plot(S[i][0],S[i][1],".")
pl.show()


SNew=[]
for i in range(0,k):
    SNew.append( [ [],[] ] )

flag=0
for i in range(0,200):
    flag=1
    for i in range(0,k):
        mx=0
        my=0
        for j in range(0, len(S[i][0]) ):
            mx+=S[i][0][j]
            my+=S[i][1][j]
        mx/=len(S[i][0])
        my/=len(S[i][0])
        M[0][i]=mx
        M[1][i]=my
    
    for i in range(0,n):
        dMin=10**50
        jMin=0
        for j in range(0,k):
            d=math.sqrt( (X[0][i]-M[0][j])**2 + (X[1][i]-M[1][j])**2 )
            if(d<dMin):
                dMin=d
                jMin=j
        SNew[jMin][0].append( X[0][i] )
        SNew[jMin][1].append( X[1][i] )

    #here if the set is the same as the old set stop iterating
    
    for i in range(0,k):
        for j in range(0, len(S[i][0])):
            del(S[i][0][0])
            del(S[i][1][0])
    
    for i in range(0,k):
        for j in range(0, len(SNew[i][0])):
            S[i][0].append(SNew[i][0][j])
            S[i][1].append(SNew[i][1][j])
    
    for i in range(0,k):
        for j in range(0, len(S[i][0])):
            del(SNew[i][0][0])
            del(SNew[i][1][0])
    


pl.plot(M[0],M[1],".k")
for i in range(0,k):
    pl.plot(S[i][0],S[i][1],".")
pl.show()
