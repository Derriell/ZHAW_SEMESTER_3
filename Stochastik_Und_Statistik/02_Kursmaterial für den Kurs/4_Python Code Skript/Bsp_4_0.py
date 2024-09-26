#Stabdiagramm der Zähldichten für das Zufallsexperiment
#Würfeln mit (A) fairem Würfel und (B) nicht-fairem Würfel
import numpy as np 
import matplotlib.pyplot as plt 

X=np.arange(1,7)
Zdichte=1/6*np.ones(6)
hx=np.array([22, 15, 8, 18, 21, 16])
fx=1/np.sum(hx)*hx

plt.figure(1)
plt.subplot(211)
plt.stem(X,Zdichte,use_line_collection='true')
plt.title('Zähldichte: Würfeln mit fairem Würfel') 
plt.xlabel('Ergebnisraum Omega') 
plt.ylabel('Wahrscheinlichkeit')
plt.xlim(0,7)
plt.ylim(0,0.3)

plt.subplot(212)
plt.stem(X,fx, use_line_collection='true', linefmt='r',markerfmt='ro')
plt.title('Zähldichte: Würfeln mit realem Würfel') 
plt.xlabel('Ergebnisraum Omega') 
plt.ylabel('Wahrscheinlichkeit')
plt.xlim(0,7)
plt.ylim(0,0.3)
plt.tight_layout()



 




