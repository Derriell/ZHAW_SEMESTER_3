import numpy as np 
import matplotlib.pyplot as plt 

##Aufgabe 6.1
x=np.array([5, 10, 20, 8, 4, 6, 12, 15])
y=np.array([27, 46, 73, 40, 30, 28, 46, 59])
#Streudiagramm
plt.figure(1)
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(20,80)
plt.title('Scatterplot')
#Ausgleichsgerade
plt.figure(2)
m,d = np.polyfit(x, y, 1)
plt.plot(x, y, 'o', x, m*x+d, '--r')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(20,80)
plt.title('Ausgleichsgerade')

#Regressionsgerade 1. Variante
n=x.size
Mx = 1/n*sum(x)
My = 1/n*sum(y)
sx=np.sqrt(1/(n-1)*sum(np.square(x-Mx)))
sy=np.sqrt(1/(n-1)*sum(np.square(y-My)))
sxy=1/(n-1)*(sum((x-Mx)*(y-My)))
rxy1=sxy/(sx*sy)
m1=rxy1*sy/sx
d1=My-m*Mx
print('Variante 1')
print('Steigung m = ',m1, 'Achsabschnitt d = ',d1)
#Regressionsgerade 2. Variante
n=x.size
Mx = 1/n*sum(x)
My = 1/n*sum(y)
Sxy=sum((x-Mx)*(y-My))
Sxx=sum(np.square(x-Mx))
m2=Sxy/Sxx
d2=My-m*Mx
print('Variante 2')
print('Steigung m = ',m2, 'Achsabschnitt d = ',d2)
#Regressionsgerade 3. Variante
m3,d3 = np.polyfit(x, y, 1)
print('Variante 3')
print('Steigung m = ',m3, 'Achsabschnitt d = ',d3)

#Bestimmtheitmass und Korrelation 1. Variante
R21=np.square(rxy1)
print('Variante 1')
print('Korrelationskoeffizient rxy = ',rxy1, 'Bestimmtheitsmass R^2 = ',R21)
#Bestimmtheitsmass und Korrelation 2. Variante
yb=m2*x+d2
Syy=sum(np.square(y-My))
Sybyb=sum(np.square(yb-My))
R22=Sybyb/Syy
rxy2=np.sqrt(R22)
print('Variante 2')
print('Korrelationskoeffizient rxy = ',rxy2, 'Bestimmtheitsmass R^2 = ',R22)

#Bestimmtheitsmass und Korrelation 3. Variante
rxy3=np.corrcoef(x,y)
R23=np.square(rxy3[0,1])
print('Variante 3')
print('Korrelationskoeffizient rxy = ',rxy3[0,1], 'Bestimmtheitsmass R^2 = ',R23)

#Residuen
Res=y-yb;
#Plot der Residuen
plt.figure(3)
plt.plot(y,Res,'b*',[20,80],[0,0],'r')
plt.xlim(20,80)
plt.ylim(-20,20)
plt.title('Residualplot')
plt.grid()