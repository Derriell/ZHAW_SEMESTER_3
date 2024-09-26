import numpy as np 
import scipy.stats as ss
import matplotlib.pyplot as plt 

# Aufgabe 5.5: Maschinen
# Binomial Verteilung 
n=100
p=0.01
X=np.arange(0,n+1,1) 
P=ss.binom.pmf(X,n,p)
plt.figure(1)
plt.stem(X,P,linefmt ='green',markerfmt='go',use_line_collection='true')
plt.xlim([0,10])
plt.ylim([0,1])
plt.title('Zähldichte (PMF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X=x)')
plt.figure(2)
plt.step(X,ss.binom.cdf(X,n,p),'g',where='post')
plt.xlim([0,10])
plt.ylim([0,1])
plt.title('Verteilungsfunktion (CDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X<=x)')

#Erwartungswert
m=ss.binom.mean(n,p)