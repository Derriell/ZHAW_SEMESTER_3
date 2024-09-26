#Ausgaben für Transport
#stetig metrisches Merkmal und Klassierung der Daten 

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

K=np.array([0, 100, 200, 500, 800, 1000, 2000]) #Klassengrenzen
h=np.array([0, 35, 182, 317, 84, 132, 0]) #absolute Klassenhäufigkeiten
APDF=np.array([0, 35/100, 182/300, 317/300, 84/200, 132/1000, 0]) #absolute Säulenhöhen im Histogramm
PDF=APDF/np.sum(h) #Säulenhöhen der PDF im Histogramm
 
plt.figure(1)
plt.step(K,PDF,color='red',where='post');
plt.xlabel('Ausgaben in Franken') 
plt.ylabel('Häufigkeitsverteilung - PDF')
plt.title('Jährliche Ausgaben - Histogramm')
plt.xlim(left=0)
plt.ylim(ymin=0)

#Alternativ mit dem histogram Befehl 
K=np.array([0, 100, 200, 500, 800, 1000, 2000]) #Klassengrenzen
#Stichprobe der Ausgaben
#mittlere Werte (für das Plotten des Histogramms)
St=np.concatenate((np.ones(h[1])*((K[0]+K[2])/2) , np.ones(h[2])*((K[2]+K[3])/2) ,np.ones(h[3])*((K[3]+K[4])/2) , np.ones(h[4])* ((K[4]+K[5])/2) , np.ones(h[5])*((K[5]+K[6])/2))) 

plt.figure(2)
#Histogram der Häufigkeitsfunktion (PDF)
plt.hist(St,K,density='True',histtype='step',color='red') 
plt.xlabel('Ausgaben in Franken') 
plt.ylabel('Häufigkeitsverteilung - PDF')
plt.title('Jährliche Ausgaben - Histogramm')
plt.xlim(left=0)

plt.figure(3)
#Histogram der Häufigkeitsfunktion (PDF) 
plt.hist(St,K,density='True',histtype='step',color='red')
plt.xlabel('Ausgaben in Franken') 
plt.ylabel('Häufigkeitsverteilung - PDF')
plt.title('Jährliche Ausgaben - Histogramm')
plt.xlim(left=0)

#Angenäherte Normalverteilung 
mu= np.mean(St) #Erwartungswert einer approx Normalverteilung 
sig= np.std(St) #Standardabweichung einer approx Normalverteilung 
XN=np.linspace(0,2000,num=100) #Definition der approx. Normalverteilung
YN=norm.pdf(XN,mu,sig)
plt.plot(XN,norm.pdf(XN,mu,sig),color='green') 
plt.xlim(left=0)

#Stichprobe generieren für die klassierten Daten 
#Klassierte Daten (zufällige Werte im Intervall, auch möglich für die pdf)
St_s=np.concatenate((np.random.randint(100, 199,size=35),np.random.randint(200, 499,size=182), np.random.randint(500, 799,size=317), np.random.randint(800,999,size=84), np.random.randint(1000, 2000,size=132))) 
K=np.array([0, 100, 200, 500, 800, 1000, 2000])  #Klassengrenzen
h_s,K_s=np.histogram(St,K) #h=[35 182 317 84 132]; #absolute Klassenhäufigkeiten
Flaechen=h_s/750 #Saeulenflächen im Histogramm der PDF
CDF=np.append([0],np.cumsum(Flaechen)) #Werte der kumulativen Verteilungsfunktion CDF

#Ohne Klassierung bzw. mit 750 Klassen
K_num = 750
h_s_m,K_m = np.histogram (St_s, bins=K_num, density=True)
CDF_m = np.cumsum (h_s_m)
 

plt.figure(4) 
plt.subplot(1,2,1)
plt.plot(K,CDF,color='red') # Verteilungsfunktion CDF 
plt.xlabel('Ausgaben in Franken') 
plt.ylabel(' F(x)')
plt.grid() 
plt.title(' CDF klassierte Daten')
plt.xlim(left=0)
plt.ylim(ymin=0)

plt.subplot(1,2,2)
plt.plot (K_m[1:], CDF_m/CDF_m[-1],color='red') # Empirische Verteilungsfunktion CDF 
plt.xlabel('Ausgaben in Franken') 
plt.ylabel(' Empirische Verteilungsfunktion F(x)')
plt.grid() 
plt.title(' CDF nichtklassierte Daten')
plt.xlim(left=0)
plt.ylim(ymin=0)
plt.tight_layout()