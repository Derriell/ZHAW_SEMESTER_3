# Quantile (aus CMF) 
import numpy as np
import matplotlib.pyplot as plt

X=np.array([4, 4, 0, 3, 5, 3, 1]) 
Xnum,absH =np.unique(X, return_counts=True) 
relH=absH/np.size(X)
kumrelH =np.cumsum(relH)

plt.figure()
plt.step(Xnum,kumrelH,where='post', color='red')
plt.xlim(0, np.max(X)+1)
plt.ylim(0, 1)
plt.vlines(1,0,0.25,color='blue',linestyles='dashed',label='1.Quartil') # 1.Quartil
plt.hlines(0.25,0,1,color='blue',linestyles='dashed')
plt.vlines(3,0,0.5,color='green',linestyles='dashed',label='2.Quartil') # Median
plt.hlines(0.5,0,3,color='green',linestyles='dashed')  
plt.vlines(4,0,0.75,color='orange',linestyles='dashed',label='3.Quartil') # 3.Quartil
plt.hlines(0.75,0,4,color='orange',linestyles='dashed')
plt.legend()
plt.title('CMF der Stichprobe')
