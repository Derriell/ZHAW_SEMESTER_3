import numpy as np 
import matplotlib.pyplot as plt 

#Aufgabe, 6.2
x=np.array([3, 4, 6, 5, 9, 15])
y=np.array([2, 4, 1, 2, 6, 45])
#Streudiagramm
plt.figure(1)
plt.plot(x,y,'o')
plt.title('Scatterplot')
plt.xlabel('x')
plt.ylabel('y')

#Regressionsgerade mit Ausreisser
n1=x.size
Mx1 = 1/n1*sum(x)
My1 = 1/n1*sum(y)
Sxy1=sum((x-Mx1)*(y-My1))
Sxx1=sum(np.square(x-Mx1))
m1=Sxy1/Sxx1
d1=My1-m1*Mx1

#Regressionsgerade ohne Ausreisser
xneu=x[0:-1]
yneu=y[0:-1]
n2=xneu.size;
Mx2 = 1/n2*sum(xneu)
My2 = 1/n2*sum(yneu)
Sxy2=sum((xneu-Mx2)*(yneu-My2))
Sxx2=sum(np.square(xneu-Mx2))
m2=Sxy2/Sxx2
d2=My2-m2*Mx2

#Grafik mit beiden Regressionsgeraden
plt.figure(2)
plt.plot(x,y,'o')
plt.plot(x,m1*x+d1,'r',label='mit Ausreisser')
plt.plot(x,m2*x+d2,'g',label='ohne Ausreisser')
plt.legend(loc='lower right')
plt.title('Mit Ausgleichsgeraden')
plt.xlabel('x')
plt.ylabel('y')