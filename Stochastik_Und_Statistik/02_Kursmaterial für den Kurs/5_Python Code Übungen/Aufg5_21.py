import numpy as np 
import scipy.stats as ss
import matplotlib.pyplot as plt 

# Aufgabe 5.21: BCH-Code
# Binomialverteilung 
n=127
p=0.1
X=np.arange(1,26.) 
bi=ss.binom(n, p)
pmf=bi.pmf(X)
cdf=bi.cdf(X)
plt.figure(1)
plt.bar(X,pmf)
plt.xlim([0,25])
plt.ylim([0,0.15])
plt.title('Zähldichte (PMF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X=x)')
plt.figure(2)
plt.bar(X,cdf)
plt.xlim([0,25])
plt.ylim([0,1])
plt.title('Verteilungsfunktion (CDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X<=x)')
#Antwort b
X0=14
Ergb=1-bi.cdf(X0)
#Antwort c
X1=18
Ergc1=1-bi.cdf(X1)
X2=12
X3=5
Ergc2=bi.cdf(X2)-bi.cdf(X3)
#Antwort d
mean,var = ss.binom.stats(n,p)
M=mean  
S=np.sqrt(var)
#Antwort e
n=ss.norm(M,S)
pdfn=n.pdf(X)
cdfn=n.cdf(X)
plt.figure(3)
plt.bar(X,pmf)
plt.plot(X,pdfn,'r-')
plt.xlim([0,25])
plt.ylim([0,0.15])
plt.title('Zähldichte (PMF) und Dichtefunktion (PDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X=x)')
plt.figure(4)
plt.bar(X,cdf)
plt.plot(X,cdfn,'r-')
plt.xlim([0,25])
plt.ylim([0,1])
plt.title('Verteilungsfunktion (CDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X<=x)')
#Antwort f
Ergf0=1-n.cdf(X0)
Ergf1=1-n.cdf(X1)
Ergf2=n.cdf(X2)-n.cdf(X3)
#Aufgabe g
Ergg0=1-n.cdf(X0+0.5)-n.cdf(-0.5)
Ergg1=1-n.cdf(X1+0.5)-n.cdf(-0.5)
Ergg2=n.cdf(X2+0.5)-n.cdf(X3-0.5)
#Aufgabe h
Ergh=ss.binom.cdf(3,10,Ergb)
