# Quantile (aus CMF) 
import numpy as np
import matplotlib.pyplot as plt

X=np.array([-2,1,5,7]) 
Xnum,absH =np.unique(X, return_counts=True) 
relH=absH/np.size(X)
kumrelH =np.cumsum(relH)

plt.figure()
plt.step(Xnum,kumrelH,where='post', color='red')
plt.xlim(np.min(X), np.max(X)+1)
plt.ylim(0, 1)
plt.vlines(-0.5,np.min(X),0.25,color='blue',linestyles='dashed',label='1.Quartil') # 1.Quartil
plt.hlines(0.25,np.min(X),-0.25,color='blue',linestyles='dashed')
plt.vlines(3,np.min(X),0.5,color='green',linestyles='dashed',label='2.Quartil') # Median
plt.hlines(0.5,np.min(X),3,color='green',linestyles='dashed')  
plt.vlines(6,np.min(X),0.75,color='orange',linestyles='dashed',label='3.Quartil') # 3.Quartil
plt.hlines(0.75,np.min(X),6,color='orange',linestyles='dashed')
plt.legend()
plt.title('CMF der Stichprobe')
