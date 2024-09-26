#Poissonteilung (PMF) 
#Telefonanrufe
import numpy as np 
import scipy.stats as ss
import matplotlib.pyplot as plt 

l=2
n=10
X=np.arange(0,n+1)
f=ss.poisson(l).pmf(X)
F=ss.poisson(l).cdf(X)

plt.figure(1) 
plt.bar(X,f)
plt.title('Zähldichte (PMF)') 
plt.xlabel('Anrufe X') 
plt.ylabel('Wahrscheinlichkeit P(X=x)')
plt.xlim(-1,10)



 




