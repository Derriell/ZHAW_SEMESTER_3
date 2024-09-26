#Berechnung von Mittelwert und Varianz bei klassierten Daten 
import numpy as np

K_m=np.array([150, 350, 650, 900, 1500]) #Mitten der Klassen 
h=np.array([35,  182,  317, 84, 132])  #Absolute Häufigkeiten der Klassen
n=np.sum(h) #Stichprobengrösse 
Mean=1/n*np.sum(K_m*h) #Mittelwert
Varianz=1/n*np.sum((K_m-Mean)**2*h) #Varianz 
Varianz=1/n*np.sum((K_m**2)*h)-Mean**2 #Varianz alternativ mit weniger Rechenaufwand

#Kennwerte
StAbw=np.sqrt(Varianz) #Standardabweichung 
kVarianz=n/(n-1)*Varianz #korrigierte Varianz 
kVarianz=1/(n-1)*(np.sum((K_m**2)*h)-n*Mean**2) #korrigierte Varianz alternativ mit weniger Rechenaufwand
kStAbw=np.sqrt(kVarianz) #korrigierte Standardabweichung 

#Mittelwert und Varianz alternativ berechnet mit Statistikbefehlen   
Stichprobe=[] 
for k in range (0,K_m.size): 
    Stichprobe=np.append([Stichprobe], np.ones(h[k])*[K_m[k]]) #Rohdaten werden generiert 

#Numpy-Funktionen auf Rohdaten 
Mean_s=np.mean(Stichprobe) #Mittelwert 
Varianz_s=np.var(Stichprobe) #Varianz 
StAbw_s=np.std(Stichprobe) #Standardabweichung 
kVarianz_s= np.var(Stichprobe,ddof=1) #korrigierte Varianz 
kStAbw_s=np.std(Stichprobe, ddof=1) #korrigierte Standardabweichung 

#Median, 1. Quantil und 3. Quantil
Median=np.median(Stichprobe)
Q1=np.quantile(Stichprobe,0.25) 
Q3=np.quantile(Stichprobe,0.75) 
IntQuAbs=Q3-Q1

#Modalwert klassierte Daten
max_num=max(h)
Mod=K_m[(h==max_num)]
