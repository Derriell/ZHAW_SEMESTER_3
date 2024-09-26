import numpy as np 
import matplotlib.pyplot as plt 

## Aufgabe 1.1: Defekte auf Platine 

# Defekte 
X=np.arange(7.)
print('X=',X)  
# absolute Häufigkeiten
hi=np.array([83., 25., 28., 18., 12., 10., 2.]) 
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
fig11 = plt.bar(X,hi)
plt.title('Defekte auf Platine') 
plt.xlabel('Anzahl Defekte')
plt.ylabel('Absolute Häufigkeit')
plt.subplot(212) 
fig12=plt.bar(X,fi,color='r')
plt.xlabel('Anzahl Defekte')
plt.ylabel('Relative Häufigkeit')

#Plot Summenfunktionen
plt.figure(2)
fig21=plt.subplot(211) 
plt.step(np.append([0],X),np.append([0],Hi),where='post')
plt.title('Defekte auf Platine') 
plt.xlabel('Anzahl Defekte')
plt.ylabel('Abs. Summenhäufigkeit')
plt.ylim(0,180)
fig22=plt.subplot(212) 
plt.step(np.append([0],X),np.append([0],Fi),where='post',color='r')
plt.xlabel('Anzahl Defekte')
plt.ylabel('Rel. Summenhäufigkeit')
plt.ylim(0,1)