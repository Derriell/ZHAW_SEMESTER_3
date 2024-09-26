#Klassierung von Daten

import numpy as np
import matplotlib.pyplot as plt

Kanten=np.array([0, 10, 20, 30,40,50,60]) #Klassengrenzen
St=np.array([3, 7, 12, 18, 19, 20, 25, 25, 27, 28, 29, 31, 32, 34, 37, 38, 40, 41, 45, 47.]) #Stichprobe
n=np.size(St) #Stichprobengrösse
hx,Kl_kant=np.histogram(St,Kanten)
fx,Kl_kant=np.histogram(St,Kanten,density='True')
 
plt.figure(1)
plt.subplot(1,2,1)
plt.hist(St,Kanten,density='True',histtype='step',color='red') #mit dem histogram Befehl
plt.xlabel('Werte') 
plt.ylabel('f(x)')
plt.title('Klassierte Daten - PDF (Histogramm)')
plt.xlim(0,60)

Fl=hx/n
CDFx=np.append([0],np.cumsum(Fl)) #Werte der kumulativen Verteilungsfunktion CDF
 
plt.subplot(1,2,2)
plt.plot(Kanten,CDFx,color='red') # Verteilungsfunktion CDF 
plt.xlabel('Werte') 
plt.ylabel('F(x)')
plt.title('Klassierte Daten - CDF')
plt.xlim(0,60)
plt.ylim(0,1)
plt.tight_layout()