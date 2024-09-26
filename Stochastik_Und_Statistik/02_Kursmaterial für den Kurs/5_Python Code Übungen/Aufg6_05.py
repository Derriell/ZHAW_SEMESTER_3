import numpy as np 
import matplotlib.pyplot as plt 

#Aufgabe 6.5
x=np.array([5,10,15,20,30])
y=np.array([720,540,430,380,335])
#Streudiagramm
plt.figure(1)
plt.plot(x,y,'o')
plt.xlabel('x')
plt.ylabel('y')

#Tranformation der y-Werte
ly=np.log(y-300)
#Neuer Plot
plt.figure(2)
m2,d2 = np.polyfit(x, ly, 1)
plt.plot(x,ly,'o',x,m2*x+d2,'r')
plt.xlabel('x')
plt.ylabel('ln(y)')
#Regression mit den logarithmierten y-Werten
n=x.size
Mx = 1/n*sum(x)
Mly = 1/n*sum(ly)
sxly=1/n*sum((x-Mx)*(ly-Mly))
sxx=1/n*np.sum(np.square(x-Mx))
lm3=sxly/sxx
ld3=Mly-lm3*Mx
#Rücktransformation der Werte
C=np.exp(ld3)
a=np.exp(lm3)
print('C=',C.round(3),',a=',a.round(3))

#Plot mit Regressionskurve
xber=np.arange(4,32,1)
yber=C*a**xber+300
plt.figure(3)
plt.plot(xber,yber)
plt.plot(x,y,'o')
plt.xlabel('x')
plt.ylabel('y')



