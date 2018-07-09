# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 11:57:39 2018

@author: Iddo
"""

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



def kMeansPartition(X,D,k,I):
    S=[]
    M=[[],[]]
    
    for i in range(0,k): #puts intiial medians on random nodes (uniquely) 
        S.append( [ [],[] ] ) #this menas that the set of things closest to it will never be empty
        x=random.randint(0,n-1)
        y=random.randint(0,n-1)
        while(x in M[0] and y in M[1]):
            x=random.randint(0,n)
            y=random.randint(0,n)
        M[0].append(X[0][x])
        M[1].append(X[1][y])
    I=M[:]
    print(I)
    flag=0
    while(flag==0): #initialize gateway positions flag should re-generate stuff if there's an empty set (doesn't do that now)
        for i in range(0,n): #if it happens this is going to cause division by zero 
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
    
    
    
    SNew=[]
    for i in range(0,k):
        SNew.append( [ [],[] ] )
    
    flag=0
    c=0
    while flag==0:
        c+=1
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
        flag=1
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
            if(X[0][i] not in S[jMin][0] and X[1][i] not in S[jMin][1]):
                flag=0
        if(c==300):
            flag=1
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
        
    
    print(c)
    pl.plot(M[0],M[1],"ok")
    for i in range(0,k):
        pl.plot(S[i][0],S[i][1],".")
    pl.show()
    d=0
    for i in range(0,k):
       for j in range(0,len(S[i][0])):
           d+=math.sqrt( (S[i][0][j]-M[0][i])**2 + (S[i][1][j]-M[1][i])**2  )
    D.append(d)
    return(I)
    






def convergenceTest(X,D,k,I):
    S=[]
    M=I[:]
    
    for i in range(0,k): #puts intiial medians on random nodes (uniquely) 
        S.append( [ [],[] ] ) #this menas that the set of things closest to it will never be empty
    flag=0
    while(flag==0): #initialize gateway positions flag should re-generate stuff if there's an empty set (doesn't do that now)
        for i in range(0,n): #if it happens this is going to cause division by zero 
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
    
    
    SNew=[]
    for i in range(0,k):
        SNew.append( [ [],[] ] )
    
    flag=0
    c=0
    while (flag==0):
        c+=1
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
        if(c==300):
            flag=1
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
        
    
    print(c)
    pl.plot(M[0],M[1],"ok")
    for i in range(0,k):
        pl.plot(S[i][0],S[i][1],".")
    pl.show()
    d=0
    for i in range(0,k):
       for j in range(0,len(S[i][0])):
           d+=math.sqrt( (S[i][0][j]-M[0][i])**2 + (S[i][1][j]-M[1][i])**2  )
    D.append(d)
    




#this file runs the same initial conditions 300 times vs when the algorithm thinks it has converged
# to test whether it actually has

X=[[],[]]
n=150
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

D=[]
maxK=16

I=[[],[]]
I=kMeansPartition(X,D,5,I)
convergenceTest(X,D,5,I)