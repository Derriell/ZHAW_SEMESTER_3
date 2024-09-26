import numpy as np 
import matplotlib.pyplot as plt 

#Aufgabe 2.3
x=np.array([3, 8, 19, 22, 31, 42, 48, 52, 54]) #Anzahl Beschäftigte
y=np.array([2, 31, 49, 65, 84, 96, 117, 129, 146]) #Umsatz in Mio
#Streudiagramm
plt.figure(1)
plt.plot(x,y,'o')
plt.xlabel('Anzahl Beschäftigte')
plt.ylabel('Umsatz in Mio')
plt.title('Scatterplot')

#Regressionsgerade (lernen wir später)
m,d = np.polyfit(x, y, 1)
print('Steigung m = ',m, 'Achsabschnitt d = ',d)
plt.figure(2)
plt.plot(x,y,'o',x,m*x+d,'r')
plt.xlabel('Anzahl Beschäftigte')
plt.ylabel('Umsatz in Mio')
plt.title('Scatterplot mit Ausgleichsgerade')

#Korrelationskoeffizient
rxy=np.corrcoef(x,y)
print('Korrelationskoeffizient rxy = ',rxy[0,1])
