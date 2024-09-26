import numpy as np 
import scipy.stats as ss
import matplotlib.pyplot as plt 

# Aufgabe 5.4: Lotterie
# Binomial Verteilung 
n=3
p=1/5
X=np.arange(0,n+1,1) 
bi=ss.binom(n, p)
P=bi.pmf(X)
plt.figure(1)
plt.subplot(121)
plt.stem(X,P,linefmt ='green',markerfmt='go',use_line_collection='true')
plt.xlim([0,n+1])
plt.ylim([0,1])
plt.title('Zähldichte (PMF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X=x)')
plt.subplot(122)
plt.step(X,np.cumsum(P),'g',where='post')
plt.xlim([0,n+1])
plt.ylim([0,1])
plt.title('Verteilungsfunktion (CDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X<=x)')
