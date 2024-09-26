#Gewinnspiel
import numpy as np
import matplotlib.pyplot as plt

G=np.array([-1, 0, 4, 8, 10, 20]) #Gewinne
h=np.array([74, 13, 3, 5, 4, 1]) #absolute H�ufigkeiten 
n=np.sum(h) #Stichprobengr�sse 100 
f=h/n #relative H�ufigkeiten (PDF) 
H=np.cumsum(h) #kumulierte absolute H�ufigkeiten 
F=np.cumsum(f) #kumulierte relative H�ufigkeiten (CDF) 

plt.figure() 
plt.subplot(2,1,1) 
plt.bar(G,f) 
plt.title('Empirische Dichte PMF')
plt.xlabel('Franken') 
plt.ylabel('Relative H�ufigkeit')
plt.subplot(2,1,2) 

#Anpassungen f�r den Plot
plt.step(np.append(-2,G),np.append(0,F))
plt.title('Empirische Verteilungsfunktion CMF')
plt.ylim(0,1)
plt.xlabel('Franken') 
plt.ylabel('Relative H�ufigkeit')
plt.tight_layout()

#Kenngr�ssen
Mean=1/n*np.sum(G*h) #Mittelwert 
Varianz1=1/n*np.sum((G-Mean)**2*h) #Stichprobenvarianz 
Varianz2=1/n*np.sum(G**2*h)-Mean**2 #Stichprobenvarianz alternative Formel 
StAbw=np.sqrt(Varianz1) #Standardabweichung 
kVarianz=1/(n-1)*np.sum((G-Mean)**2*h) #korrigierte Stichprobenvarianz
kStAbw=np.sqrt(kVarianz) #korrigierte Standardabweichung
