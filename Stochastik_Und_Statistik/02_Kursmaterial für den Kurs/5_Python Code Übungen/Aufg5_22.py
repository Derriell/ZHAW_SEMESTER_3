import numpy as np 
import scipy.stats as ss
import matplotlib.pyplot as plt 

# Aufgabe 5.21
# Binomialverteilung 
n=1000
p=0.5
X=np.arange(1,1000.) 
bi=ss.binom(n, p)
pmf=bi.pmf(X)
cdf=bi.cdf(X)

#Wert für x=540
p540b=bi.pmf(540)
#Wert für x=540 mit Normvert.
mean,var = ss.binom.stats(n,p)
M=mean  
S=np.sqrt(var)
n=ss.norm(M,S)
p540n=n.pdf(540)

#Plots
#Binomialvert.
plt.figure(1)
plt.bar(X,pmf)
plt.xlim([450,550])
plt.ylim([0,0.03])
plt.title('Zähldichte (PMF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X=x)')
plt.figure(2)
plt.bar(X,cdf)
plt.xlim([450,550])
plt.ylim([0,1])
plt.title('Verteilungsfunktion (CDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X<=x)')

#Normvert.
pdfn=n.pdf(X)
cdfn=n.cdf(X)
plt.figure(3)
plt.bar(X,pmf)
plt.plot(X,pdfn,'r-')
plt.xlim([450,550])
plt.ylim([0,0.03])
plt.title('Zähldichte (PMF) und Dichtefunktion (PDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X=x)')
plt.figure(4)
plt.bar(X,cdf)
plt.plot(X,cdfn,'r-')
plt.xlim([450,550])
plt.ylim([0,1])
plt.title('Verteilungsfunktion (CDF)') 
plt.xlabel('Treffer X') 
plt.ylabel('Wahrscheinlichkeit P(X<=x)')

