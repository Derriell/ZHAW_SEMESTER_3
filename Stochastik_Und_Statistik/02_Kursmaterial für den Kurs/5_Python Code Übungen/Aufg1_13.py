import numpy as np 
import matplotlib.pyplot as plt 

## Aufgabe 1.13
X = np.array([5, 18, 15, 7, 23, 220, 130, 85, 103, 25, 80, 7, 24, 6, 13, 65, 37, 25,
     24, 65, 82, 95, 77, 15, 70, 110, 44, 28, 33, 81, 29, 14, 45, 92, 17, 53])
b=np.max(X)-np.min(X)
plt.figure(1) 
plt.subplot(211)
plt.hist(X,density=1,bins=20) 
plt.axis([0,250,0,0.03])
plt.ylabel('absolute Häufigkeit')
plt.title('Histogramm: Partikelkonzentration')
plt.subplot(212)
plt.hist(X,density=1,bins=5) 
plt.axis([0,250,0,0.03])
plt.xlabel('Mikrogramm pro Kubikmeter')
plt.ylabel('absolute Häufigkeit')

plt.figure(2) 
plt.hist(X,density=1,cumulative=True, bins=b) 
plt.title('Empirische Verteilungsfunktion CDF')
plt.xlabel('Mikrogramm pro Kubikmeter')
plt.ylabel('absolute Häufigkeit')

plt.figure(3) 
plt.hist(X,density=1,histtype='step',cumulative=True, bins=b)
plt.title('Empirische Verteilungsfunktion CDF')
plt.xlabel('Mikrogramm pro Kubikmeter')
plt.ylabel('absolute Häufigkeit')

plt.figure(4)
plt.boxplot(X)
plt.title('Partikelkonzentration :Boxplot')
plt.ylabel('Mikrogramm pro Kubikmeter')

#Kennwerte 
print(np.percentile(X,[0.25,0.5,0.75])) #[5.0875 5.175  5.2625]
print(np.mean(X)) #51.72
print(np.std(X)) #44.332, Standardabw.
print(np.std(X,ddof=1)) #44.96, korr. Standardabw. 

