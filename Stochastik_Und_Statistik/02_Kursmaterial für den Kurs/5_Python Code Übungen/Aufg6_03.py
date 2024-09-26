import numpy as np 
import matplotlib.pyplot as plt 

#Aufgabe 6.3
x=np.array([3, 8, 19, 22, 31, 42, 48, 52, 54]) #Anzahl Beschäftigte
y=np.array([2, 31, 49, 65, 84, 96, 117, 129, 146]) #Umsatz in Mio
#Streudiagramm
plt.figure(1)
plt.plot(x,y,'o')
plt.xlabel('Anzahl Beschäftigte')
plt.ylabel('Umsatz in Mio')
plt.title('Scatterplot')

#Regressionsgerade 3. Variante
m,d = np.polyfit(x, y, 1)
print('Steigung m = ',m, 'Achsabschnitt d = ',d)
plt.figure(2)
plt.plot(x,y,'o',x,m*x+d,'r')
plt.xlabel('Anzahl Beschäftigte')
plt.ylabel('Umsatz in Mio')
plt.title('Scatterplot mit Ausgleichsgerade')

#Korrelationskoeffizient und Bestimmtheitsmass
rxy=np.corrcoef(x,y)
R2=np.square(rxy[0,1])
print('Korrelationskoeffizient rxy = ',rxy[0,1], 'Bestimmtheitsmass R^2 = ',R2)

#Umsatz bei 200 Beschäftigten 
X=200
Yb=m*X+d
print('Der geschätzte Umsatz bei 200 Beschäftigten liegt bei',Yb.round(2), 'Mio')

#Varianzen
yb=m*x+d
n=x.size
Mx = 1/n*sum(x)
My = 1/n*sum(y)
Syy=sum(np.square(y-My))
Sybyb=sum(np.square(yb-My))
sybyb=1/(n-1)*Sybyb #erklärte Varianz
syy= 1/(n-1)*Syy #Gesamtvarianz
See=sum(np.square(y-yb)) #Summe der Residuenquadrate
print('erklärte Varianz', sybyb.round(2), ', Gesamtvarianz',syy.round(2),', Summe der Residuenquadrate', See.round(2))


