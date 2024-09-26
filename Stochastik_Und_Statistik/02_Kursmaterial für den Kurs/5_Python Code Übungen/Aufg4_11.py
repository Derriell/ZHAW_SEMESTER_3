#Aufgabe 4.11

import numpy as np
import matplotlib.pyplot as plt

x=np.array([-1,0,1,2,3]) #Zufallsvariable
Px=np.array([0.1,0.3,0.4,0.15,0.05]) #pmf
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