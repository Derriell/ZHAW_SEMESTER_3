#Zufallsvariable Gewinnspiel 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import special as sp

G=np.array([-1,0,4,8,10,20])
Total=6**5 #Anzahl Möglichkeiten
M=np.zeros(6)
M[1]=sp.binom(5,3)*6*5*4
M[2]=sp.binom(5,3)*6*5
M[3]=2*sp.factorial(5)
M[4]=sp.binom(5,4)*6*5
M[5]=6
M[0]=Total-np.sum(M)
PMF=1/Total*M #PMF des Gewinns
CDF=np.cumsum(PMF) #CDF des Gewinns

E=np.sum(G*PMF) #Erwartungswert
S2=np.sum(G**2*PMF)-E**2 #Varianz
S=np.sqrt(S2) #Standardabweichung


plt.figure(1)
plt.stem(G,PMF,use_line_collection='true',basefmt='None')
plt.title('PMF des Gewinns: 5 Würfel')
plt.xlabel('Gewinn G')
plt.ylabel('Wahrscheinlichkeit')
plt.xticks([i for i in range(-2,22)])
plt.yticks([i/10 for i in range(0,11)])
plt.grid(b=True, color='gray', linestyle='--')
plt.xlim(-2,21)
plt.ylim(0,1)

plt.figure(2)
plt.step(np.append(G,[21]),np.append([0],CDF))
plt.title('CDF des Gewinns: 5 Würfel') 
plt.xlabel('Gewinn G') 
plt.ylabel('Wahrscheinlichkeit')
plt.xticks([i for i in range(-2,22)])
plt.yticks([i/10 for i in range(0,11)])
plt.grid(b=True, color='gray', linestyle='--')
plt.xlim(-2,21)
plt.ylim(0,1)


plt.figure(3)
plt.plot([E,E],[0,1],'g--',label='E=-0.15')
plt.plot([-1,-1],[0,1],'y--',label='Median,Modus=-1')
plt.plot([E-S,E+S],[0,0],'ro-', label='S=2.36')
plt.stem(G,PMF,use_line_collection='true',basefmt='None')
plt.legend()
plt.title('PMF und Kenngrössen des Gewinns') 
plt.ylabel('Rel. Häufigkeit')
plt.xlim(-4,21)
plt.ylim(0,1)

