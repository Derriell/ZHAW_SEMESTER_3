import numpy as np 
import scipy.stats as ss
import matplotlib.pyplot as plt 

#Aufgabe 5.2
# Kugeln Aufgabe a) weiss
N1=5 
M1=3 
n1=3 
X1=np.arange(0,n1+1) #weisse Kugeln
hpd1=ss.hypergeom(N1, M1, n1)
P1=hpd1.pmf(X1)
plt.figure(1)
plt.subplot(121)
plt.stem(X1,P1,use_line_collection='true')
plt.xlim([0,4])
plt.ylim([0,1])
plt.title('Zähldichte (PMF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X=x)')
plt.subplot(122)
plt.step(X1,np.cumsum(P1),where='post')
plt.xlim([0,4])
plt.ylim([0,1])
plt.title('Verteilungsfunktion (CDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X<=x)')
plt.subplots_adjust(wspace=0.5)

# Hypergeometrische Verteilung  
# Kugeln Aufgabe a) schwarz
N2=5 
M2=2 
n2=3 
X2=np.arange(0,n2+1) #schwarze Kugeln
hpd2=ss.hypergeom(N2,M2,n2)
P2=hpd2.pmf(X2)
plt.figure(2)
plt.subplot(121)
plt.stem(X2,P2,linefmt ='red',markerfmt='ro',use_line_collection='true')
plt.xlim([0,4])
plt.ylim([0,1])
plt.title('Zähldichte (PMF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X=x)')
plt.subplot(122)
plt.step(X2,np.cumsum(P2),'r',where='post')
plt.xlim([0,4])
plt.ylim([0,1])
plt.title('Verteilungsfunktion (CDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X<=x)')
plt.subplots_adjust(wspace=0.5)

# Binomialverteilung 
# Kugeln Aufgabe c)
n3=3
p3=2/5
X3=np.arange(0,n3+1) #schwarze Kugeln
bi=ss.binom(n3, p3)
P3=bi.pmf(X1)
plt.figure(3)
plt.subplot(121)
plt.stem(X3,P3,linefmt ='green',markerfmt='go',use_line_collection='true')
plt.xlim([0,4])
plt.ylim([0,1])
plt.title('Zähldichte (PMF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X=x)')
plt.subplot(122)
plt.step(X3,np.cumsum(P3),'g',where='post')
plt.xlim([0,4])
plt.ylim([0,1])
plt.title('Verteilungsfunktion (CDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X<=x)')
plt.subplots_adjust(wspace=0.5)
