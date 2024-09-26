#Binomialverteilung (PDF) 
#Testen von 200 Geräten mit Ausfallwahrscheinlichkeit 0.06
import numpy as np 
import scipy.stats as ss
import matplotlib.pyplot as plt 

n=200
p=0.06
X=np.arange(0,n+1)
X0=np.arange(10,16)
bi=ss.binom(n,p)
f=bi.pmf(X)
F=bi.cdf(X)
f0=bi.pmf(X0)
F0=bi.cdf(X0)

plt.figure(1) 
plt.bar(X,f)
plt.bar(X0,f0,color='red')
plt.title('Z�hldichte (PMF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X=x)')
plt.xlim(0,40)

plt.figure(2) 
plt.step(np.append([-1],X),np.append([0],F),where='post')
plt.step(np.append([9],X0),np.append(F[9],F0),where='post',color='red')
plt.plot([0,10],[F[9],F[9]],'r-.')
plt.plot([0,15],[F[15],F[15]],'r-.')
plt.plot([10,10],[0,F[9]],'r-.')
plt.plot([15,15],[0,F[15]],'r-.')
plt.title('Verteilungsfunktion (CDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X<=x)')
plt.xlim(0,20)
plt.ylim(0,1)

#Berechung von P(10≤X≤15)
F1=ss.binom(200,0.06).cdf(15)
F2= ss.binom(200,0.06).cdf(9)
print(F1-F2)


 




