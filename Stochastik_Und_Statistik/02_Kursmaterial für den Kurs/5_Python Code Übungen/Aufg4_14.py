#Aufgabe 4.14

import numpy as np
import matplotlib.pyplot as plt

x_in=np.arange(1,7) 
x=10*((x_in-3)/x_in) #Zufallsvariable
Px=np.ones(6)*1/6 #pmf
Fx=np.cumsum(Px) #cdf
 
plt.figure(1)
plt.subplot(121)
plt.stem(x,Px,linefmt ='red',markerfmt='ro',use_line_collection='true')
plt.xlabel('x') 
plt.ylabel('P(X=x)')
plt.title('PMF')
plt.ylim(ymin=0)

plt.subplot(122)
plt.step(np.append(x[0],x),np.append([0],Fx),color='red',where='post') 
plt.ylabel('P(X<=x)') 
plt.xlabel('x')
plt.title('CDF') 
plt.ylim(ymin=0,ymax=1)
plt.tight_layout()

#Erwartungswert
E=np.sum(x*Px)

#Varianz
V=np.sum(x**2*Px)-E**2

#Standardabweichung
S=V**0.5