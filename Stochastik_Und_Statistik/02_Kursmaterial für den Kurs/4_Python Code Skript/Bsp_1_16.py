#Gewinnspiel
import numpy as np
import matplotlib.pyplot as plt

G=np.array([-1, 0, 4, 8, 10, 20]) #Gewinne
h=np.array([74, 13, 3, 5, 4, 1]) #absolute Häufigkeiten 
n=np.sum(h) #Stichprobengrösse 100 
f=h/n #relative Häufigkeiten (PDF) 
H=np.cumsum(h) #kumulierte absolute Häufigkeiten 
F=np.cumsum(f) #kumulierte relative Häufigkeiten (CDF) 

plt.figure() 
plt.subplot(2,1,1) 
plt.bar(G,f) 
plt.title('Empirische Dichte PMF')
plt.xlabel('Franken') 
plt.ylabel('Relative Häufigkeit')
plt.subplot(2,1,2) 

#Anpassungen für den Plot
plt.step(np.append(-2,G),np.append(0,F))
plt.title('Empirische Verteilungsfunktion CMF')
plt.ylim(0,1)
plt.xlabel('Franken') 
plt.ylabel('Relative Häufigkeit')
plt.tight_layout()

#Kenngrössen
Mean=1/n*np.sum(G*h) #Mittelwert 
Varianz1=1/n*np.sum((G-Mean)**2*h) #Stichprobenvarianz 
Varianz2=1/n*np.sum(G**2*h)-Mean**2 #Stichprobenvarianz alternative Formel 
StAbw=np.sqrt(Varianz1) #Standardabweichung 
kVarianz=1/(n-1)*np.sum((G-Mean)**2*h) #korrigierte Stichprobenvarianz
kStAbw=np.sqrt(kVarianz) #korrigierte Standardabweichung
