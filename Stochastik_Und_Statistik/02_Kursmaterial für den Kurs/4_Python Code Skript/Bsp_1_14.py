#Mieten
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Daten einlesen
df = pd.read_excel('Bsp_1_14.xlsx')
print (df.columns) #Bezeichnung der Datenreihen
Miete=df.values[:,0]
h=df.values[:,1]

#Rohdaten erzeugen
Stichprobe=[] 
for k in range (0,Miete.size): 
    Stichprobe=np.append([Stichprobe], np.ones(h[k])*[Miete[k]]) #Rohdaten werden generiert 

#Quartile
Q1=np.quantile(Stichprobe,0.25)
Q2=np.quantile(Stichprobe,0.5)
Q3=np.quantile(Stichprobe,0.75) 
IQR=Q3-Q1  
print(IQR) 
    
n=np.sum(h)  #Stichprobengrösse 151
H=np.cumsum(h)  #kumulierte absolute Häufigkeiten 
F=H/n # kumulierte relative Häufigkeit
#Nichtklassierte Daten plotten
plt.figure(1)
plt.step(Miete, F,color='red')
plt.xlabel('Nettomiete') 
plt.ylabel('F(x)') 
plt.ylim(0,1)
plt.xlim(left=0)
plt.vlines(731,0,0.25,color='blue',linestyles='dashed',label='1.Quartil') # 1.Quartil
plt.hlines(0.25,0,731,color='blue',linestyles='dashed')
plt.vlines(1025,0,0.5,color='green',linestyles='dashed',label='2.Quartil') # Median
plt.hlines(0.5,0,1025,color='green',linestyles='dashed')  
plt.vlines(1480,0,0.75,color='orange',linestyles='dashed',label='3.Quartil') # 3.Quartil
plt.hlines(0.75,0,1480,color='orange',linestyles='dashed')
plt.legend()
plt.title('Empirische Verteilungsfunktion (CDF) - Stichprobengrösse = {}'.format(n))

#Tabelle der Klassenhäufigkeiten 
K=pd.Series(['270-570', '570-870', '870-1000', '1000-1500', '1500-2500', '2500-3500', '3500-5000'])
K_gr=[270, 570, 870, 1000, 1500, 2500, 3500, 5000] #Klassengrenzen 
#Klassierte Daten als Tabelle ausgeben
hk=np.histogram(Stichprobe,bins=K_gr)[0]
Hk=np.cumsum(hk) 
Fk=Hk/n 
dfk=pd.DataFrame((hk,Hk,Fk),index=['abs. Häufigkeit', 'abs. Summenhäufigkeit','rel. Summenhäufigkeit'], columns=K)
print(dfk)

#Histogramm plotten
plt.figure(2)
plt.hist(Miete,K_gr,density='True',histtype='step',color='red')
plt.xlabel('Miete in Franken')
plt.ylabel('PDF')
plt.title('Histogramm der PDF: Relative Häufigkeit der Mieten')

#Verteilungsfunktion 
#empirisch Verteilungsfunktion und 
plt.figure(3) 
plt.step(Miete, F,color='red')
#empirische Verteilungsfunktion  klassierten Daten 
Fk_p=np.append(0,Fk)
plt.plot(K_gr,Fk_p)
plt.ylim(0,1)
plt.xlabel('Miete in Franken')
plt.ylabel('Verteilungsfunktion')
plt.title('Verteilungsfunktion der Mieten') 
plt.legend(('empirische CDF','CDF der klassierten Daten'),loc='best')

#Berechnung des 0.7351 Quantils der Rohdaten 
Q=np.quantile(Stichprobe,0.7351)
print(Q)