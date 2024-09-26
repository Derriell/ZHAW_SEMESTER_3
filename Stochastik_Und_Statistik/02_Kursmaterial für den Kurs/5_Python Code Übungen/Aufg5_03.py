import numpy as np 
import scipy.stats as ss
import matplotlib.pyplot as plt 

#Aufgabe 5.3
# Binomialverteilung 
# Münzen
n=4
p=1/2
X=np.arange(0,n+1,1) #schwarze Kugeln
bi=ss.binom(n, p)
f=bi.pmf(X)
F=bi.cdf(X)
plt.figure(1)
plt.subplot(121)
plt.stem(X,f,linefmt ='green',markerfmt='go',use_line_collection='true')
plt.xlim([0,n+1])
plt.ylim([0,1])
plt.title('Zähldichte (PMF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X=x)')
plt.subplot(122)
plt.step(X,F,'g',where='post')
plt.xlim([0,n+1])
plt.ylim([0,1])
plt.title('Verteilungsfunktion (CDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X<=x)')
plt.subplots_adjust(wspace=0.5)
