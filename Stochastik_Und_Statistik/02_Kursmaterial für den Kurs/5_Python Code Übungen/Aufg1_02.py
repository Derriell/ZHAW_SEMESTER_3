import numpy as np 
import matplotlib.pyplot as plt 

## Aufgabe 1.2: Geschwister 

#Daten
d=np.array([1,0,1,1,2,1,0,0,2,1,1,1,3,0,2,2,1,1,0,2,3,1,1,2,1])
#Geschwister 
X, hi = np.unique(d, return_counts=True)
print('X=',X)  
# absolute Häufigkeiten
print('hi=',hi) 
# relative Haeufigkeiten PDF 
fi=hi/sum(hi)
print('fi=',fi) 
# absolute Summenhäufigkeit 
Hi=hi.cumsum(axis=0)
print('Hi=',Hi)
# kumulative Verteilung CDF
Fi=fi.cumsum(axis=0)
print('Fi=',Fi)

#Plot Häufigkeiten
plt.figure(1) 
plt.subplot(211) 
fig11 = plt.bar(X,hi,  width=0.2)
plt.title('Geschwister') 
plt.xlabel('Anzahl Geschwister')
plt.ylabel('Absolute Häufigkeit')
plt.subplot(212) 
fig12=plt.bar(X,fi,color='r',  width=0.2)
plt.xlabel('Anzahl Geschwister')
plt.ylabel('Relative Häufigkeit')

#Plot Summenfunktionen
plt.figure(2)
fig21=plt.subplot(211) 
plt.step(np.append([0],X),np.append([0],Hi),where='post')
plt.title('Geschwister') 
plt.xlabel('Anzahl Geschwister')
plt.ylabel('Abs. Summenhäufigkeit')
plt.xlim(0,4)
plt.ylim(0,25)
fig22=plt.subplot(212) 
plt.step(np.append([0],X),np.append([0],Fi),where='post',color='r')
plt.xlabel('Anzahl Geschwister')
plt.ylabel('Rel. Summenhäufigkeit')
plt.xlim(0,4)
plt.ylim(0,1)