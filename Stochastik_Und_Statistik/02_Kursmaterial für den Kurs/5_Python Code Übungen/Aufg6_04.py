import numpy as np 
import matplotlib.pyplot as plt 

#Aufgabe 6.4
x=np.array([2, 5, 8, 12, 15])
y=np.array([4, 6, 15, 21, 35])
#Streudiagramm
plt.figure(1)
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')

plt.figure(2)
m1,d1 = np.polyfit(x, y, 1)
plt.plot(x,y,'o',x,m1*x+d1,'r')
plt.xlabel('x')
plt.ylabel('y')

#Tranformation der y-Werte
ly=np.log(y)
#Neuer Plot
plt.figure(3)
m2,d2 = np.polyfit(x, ly, 1)
plt.plot(x,ly,'o',x,m2*x+d2,'r')
plt.xlabel('x')
plt.ylabel('ln(y)')

#Regression mit den logarithmierten Werten
n=x.size
Mx = 1/n*sum(x)
Mly = 1/n*sum(ly)
Sxly=sum((x-Mx)*(ly-Mly))
Sxx=sum(np.square(x-Mx))
lm=Sxly/Sxx
ld=Mly-lm*Mx
#Rücktransformation der Werte
m3=np.exp(lm)
d3=np.exp(ld)



