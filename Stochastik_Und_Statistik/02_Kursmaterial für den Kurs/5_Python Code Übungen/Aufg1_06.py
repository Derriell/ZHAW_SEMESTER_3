import numpy as np 
import matplotlib.pyplot as plt 

## Aufgabe 1.6: Klassierte Daten

#Klassengrenzen
KlGr=np.array([4, 10, 20, 30, 40, 80, 120])
print('KlGrenzen=',KlGr)  
#absolute Klassenhaeufigkeiten
hi=np.array([20, 160, 80, 40, 88, 12])
n=np.sum(hi)
print('hi=',hi)
#Saeulenhoehen im Histogram der PDF
Kldiff=np.diff(KlGr)
print('Kldiff=',Kldiff)
Sumhi=np.sum(hi)
print('Sumhi=',Sumhi)
Saeulenhoehe=hi/np.diff(KlGr)/np.sum(hi)
print('Sauelenhoehe=',Saeulenhoehe) 
Ser=np.append([Saeulenhoehe],[0]) 
print(Ser)
#figure 
plt.figure(1)
plt.subplot(121) 
#Klassenmitten generieren
KlMitten=np.empty(KlGr.size-1)
for k in range (0,KlGr.size-1):
    KlMitten[k]=(KlGr[k+1]+KlGr[k])/2
plt.bar(KlMitten,Saeulenhoehe,width=Kldiff,color='red') 
plt.ylabel('pdf')
plt.title('Lebensversicherungsverträge')
plt.subplot(122)
plt.plot(KlGr,np.append([0],[np.cumsum(hi)/Sumhi]),color='red')
plt.xlabel('Versicherungssumme [TFR]')
plt.ylabel('cdf')
plt.tight_layout()

#Stichprobe generieren für die klassierten Daten 
#Klassierte Daten
St_s=np.empty(shape=[0, n])
for k in range (0,KlGr.size-1):
    St_s=np.concatenate((St_s,np.random.randint(KlGr[k],KlGr[k+1],size=hi[k])),axis=None)

#Histogramm erstellen für die simulierten Daten
h_s,K_s=np.histogram(St_s,KlGr) #h=[35 182 317 84 132] #absolute Klassenhäufigkeiten
Flaechen=h_s/n #Saeulenflächen im Histogramm der PDF über Histigramm-Befehl
CDF=np.append([0],np.cumsum(Flaechen)) #Werte der kumulativen Verteilungsfunktion CDF

#Simulierte Daten
h_s_m,K_m = np.histogram (St_s, bins=n, density=True)
CDF_m = np.cumsum (h_s_m)

plt.figure(2) 
plt.subplot(121)
plt.plot(K_s,CDF,color='red') # Verteilungsfunktion CDF 
plt.xlabel('Ausgaben in Franken') 
plt.ylabel(' F(x)')
plt.grid() 
plt.title(' CDF klassierte Daten')
plt.xlim(left=0)
plt.ylim(ymin=0)

plt.subplot(122)
plt.plot (K_m[1:], CDF_m/CDF_m[-1],color='red') # Empirische Verteilungsfunktion CDF 
plt.xlabel('Ausgaben in Franken') 
plt.ylabel(' Empirische Verteilungsfunktion F(x)')
plt.grid() 
plt.title(' CDF nichtklassierte Daten')
plt.xlim(left=0)
plt.ylim(ymin=0)
plt.tight_layout()

