import numpy as np 
import scipy.stats as ss
import matplotlib.pyplot as plt 

# Aufgabe 5.6: Telefon
# Binomial Verteilung 
l=300/60
n=20
X=np.arange(0,n+1,1) 
P=ss.poisson.pmf(X,l)
plt.figure(1)
plt.stem(X,P,linefmt ='green',markerfmt='go',use_line_collection='true')
plt.xlim([0,10])
plt.ylim([0,1])
plt.title('Zähldichte (PMF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X=x)')
plt.figure(2)
plt.step(X,ss.poisson.cdf(X,l),'g',where='post')
plt.xlim([0,10])
plt.ylim([0,1])
plt.title('Verteilungsfunktion (CDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X<=x)')

#mehr als 10 Anrufe
Anrg10=1-ss.poisson.cdf(10,l)
