import numpy as np 
import matplotlib.pyplot as plt 

#Aufgabe 6.6
x=np.array([10000, 18000, 26000, 37000, 45000, 60000, 75000])
y=np.array([9500, 7000, 5600, 5200, 4500, 4000, 3500])
#Streudiagramm
plt.figure(1)
m1,d1 = np.polyfit(x, y, 1)
plt.plot(x,y,'o',x,m1*x+d1,'r')
plt.xlabel('x')
plt.ylabel('y')

#Tranformation der y-Werte
ly=np.log(y)
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
Sxly=sum((x-Mx)*(ly-Mly))
Sxx=np.sum(np.square(x-Mx))
lm3=Sxly/Sxx
ld3=Mly-lm3*Mx
#Rücktransformation der Werte
m3=np.exp(lm3)
d3=np.exp(ld3)

#Tranformation der x- und y-Werte
lx=np.log(x)
#Neuer Plot
plt.figure(3)
m4,d4 = np.polyfit(lx, ly, 1)
plt.plot(lx,ly,'o',lx,m4*lx+d4,'r')
plt.xlabel('ln(x)')
plt.ylabel('ln(y)')
#Regression mit den logarithmierten Werten
n=x.size
Mlx = 1/n*sum(lx)
#Mly = 1/n*sum(ly)
Sxly=sum((lx-Mx)*(ly-Mly))
Slxlx=sum(np.square(lx-Mlx))
m5=Sxly/Slxlx
ld5=Mly-m5*Mlx
#Rücktransformation der Werte
m5
d5=np.exp(ld5)

