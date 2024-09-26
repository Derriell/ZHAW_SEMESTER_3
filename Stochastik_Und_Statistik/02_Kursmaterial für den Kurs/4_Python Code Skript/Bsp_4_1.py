#Augensumme: Stabdiagramm von PMF und 
#CDF als Treppenfunktion 
import numpy as np 
import matplotlib.pyplot as plt 

X=np.arange(2,13)
PMFx=1/36*np.concatenate((np.arange(1,6),np.array([6]),np.arange(5,0,-1)),axis=0)
CDFx=np.cumsum(PMFx)


plt.figure(1)
plt.subplot(121)
plt.stem(X,PMFx,use_line_collection='true')
plt.title('PMF von X: f(x)=P(X=x)') 
plt.xlabel('Augensumme X') 
plt.ylabel('Wahrscheinlichkeit')
plt.xticks([i for i in range(0,13)])
plt.grid(b=True, color='gray', linestyle='--')
plt.xlim(0,13)
plt.ylim(0,0.2)

plt.subplot(122)
plt.step(np.append(X,[12]),np.append([0],CDFx))
plt.title('CDF von X: F(x)=P(X<=x)') 
plt.xlabel('Augensumme X') 
plt.ylabel('Wahrscheinlichkeit')
plt.xticks([i for i in range(0,13)])
plt.yticks([i/10 for i in range(0,10)])
plt.grid(b=True, color='gray', linestyle='--')
plt.xlim(0,13)
plt.ylim(0,1)
plt.tight_layout()
