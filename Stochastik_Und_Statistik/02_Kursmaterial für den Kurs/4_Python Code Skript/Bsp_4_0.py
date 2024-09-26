#Stabdiagramm der Z�hldichten f�r das Zufallsexperiment
#W�rfeln mit (A) fairem W�rfel und (B) nicht-fairem W�rfel
import numpy as np 
import matplotlib.pyplot as plt 

X=np.arange(1,7)
Zdichte=1/6*np.ones(6)
hx=np.array([22, 15, 8, 18, 21, 16])
fx=1/np.sum(hx)*hx

plt.figure(1)
plt.subplot(211)
plt.stem(X,Zdichte,use_line_collection='true')
plt.title('Z�hldichte: W�rfeln mit fairem W�rfel') 
plt.xlabel('Ergebnisraum Omega') 
plt.ylabel('Wahrscheinlichkeit')
plt.xlim(0,7)
plt.ylim(0,0.3)

plt.subplot(212)
plt.stem(X,fx, use_line_collection='true', linefmt='r',markerfmt='ro')
plt.title('Z�hldichte: W�rfeln mit realem W�rfel') 
plt.xlabel('Ergebnisraum Omega') 
plt.ylabel('Wahrscheinlichkeit')
plt.xlim(0,7)
plt.ylim(0,0.3)
plt.tight_layout()



 




