#Quantile
import numpy as np
import matplotlib.pyplot as plt

X=np.array([5, -2, 1, 7]) 
Q1=np.quantile(X,0.25)
Q2=np.quantile(X,0.5)
Q3=np.quantile(X,0.75)

Xnum,absH =np.unique(X, return_counts=True) 
relH=absH/np.size(X)
kumrelH =np.cumsum(relH)

plt.figure()
plt.step(Xnum,kumrelH,where='post', color='red')
plt.xlim(0, 8)
plt.ylim(0, 1)

plt.hlines(0.25,0,8, color='green',linestyles='dashed')
plt.hlines(0.5,0,8, color='green',linestyles='dashed')
plt.hlines(0.75,0,8, color='green',linestyles='dashed')
