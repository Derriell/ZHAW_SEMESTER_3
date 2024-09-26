#Hypergeometrische Verteilung (PDF) 
#Lotto 6 aus 49
import numpy as np 
import scipy.stats as ss
import matplotlib.pyplot as plt 

N=49 
M=6 
n=6
X=np.arange(0,n+1)
hyge=ss.hypergeom(N, M, n)
f=hyge.pmf(X)
F=hyge.cdf(X)

plt.figure(1) 
plt.bar(X,f)
plt.title('Zähldichte (PMF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X=x)')
plt.xlim(-1,7)

plt.figure(2) 
plt.step(np.append([-1],X),np.append([0],F),where='post')
plt.title('Verteilungsfunktion (CDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X<=x)')
plt.xlim(-1,7)
plt.ylim(0,1)

#Berechung von P(X≥4)
print(1-ss.hypergeom(49,6,6).cdf(3))

