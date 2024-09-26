#Hypergeometrische und Binomialverteilung  
import numpy as np 
import scipy.stats as ss
import matplotlib.pyplot as plt 

N=800
M=340
p=340/800
n=12
X=np.arange(0,n+1)
fh=ss.hypergeom(N,M,n).pmf(X)
fb=ss.binom(n,p).pmf(X)

plt.figure(1) 
plt.bar(X,fh, label='H(800,340,12)')
plt.bar(X,fb, width=0.2,color='r',label='B(340/800,12)')
plt.ylabel('PMF') 
plt.xlabel('x') 
plt.xlim(-1,13)
plt.legend()


