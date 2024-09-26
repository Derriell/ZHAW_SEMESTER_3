#Verschiedene Scatterplots
import numpy as np
import matplotlib.pyplot as plt

#gleichsinniger Zusammenhang
x=np.array([163,165,166,169,170,171,171,173,174,175,177,177,179,180,185])
y1=np.array([59,62,65,69,65,69,76,73,75,73,80,71,82,84,81])

#ohne Zusammenhang
y2=np.array([2900,1100,3600,2300,4000,5600,2100,5100,3400,1800,2100,2600,4600,3600,2300])

#gegensinniger Zusammenhang
y3=np.array([2.0,1.8,1.7,1.9,1.8,1.5,1.9,1.3,1.7,1.5,1.4,1.7,1.1,1.5,1.4])

#Regression
m1,d1 = np.polyfit(x, y1, 1)
m2,d2 = np.polyfit(x, y2, 1)
m3,d3 = np.polyfit(x, y3, 1)

#Berechnete y-Werte
y1b=m1*x+d1
y2b=m2*x+d2
y3b=m3*x+d3

#Residuen
R1=y1-y1b
R2=y2-y2b
R3=y3-y3b

plt.figure(1)
plt.subplot(121)
plt.plot(x,y1,'o',x,m1*x+d1,'r')
plt.xlim(160,190)
plt.ylim(55,85)
plt.xlabel('Grösse')
plt.ylabel('Gewicht')
plt.subplot(122)
plt.plot(y1b,R1,'o',[60, 90],[0, 0],'k')
plt.xlim(60,90)
plt.xlabel('Gewicht')
plt.ylim(-15,15)
plt.tight_layout()

plt.figure(2)
plt.subplot(121)
plt.plot(x,y2,'o',x,m2*x+d2,'r')
plt.ylim(1000,6000)
plt.xlabel('Grösse')
plt.ylabel('Einkommen')
plt.subplot(122)
plt.plot(y2b,R2,'o',[3000, 3300],[0, 0],'k')
plt.xlim(3000,3300)
plt.ylim(-2500,2500)
plt.xlabel('Einkommen')
plt.tight_layout()

plt.figure(3)
plt.subplot(121)
plt.plot(x,y3,'o',x,m3*x+d3,'r')
plt.xlabel('Grösse')
plt.ylabel('Laufzeit')
plt.ylim(1,2)
plt.subplot(122)
plt.plot(y3b,R3,'o',[1, 2],[0, 0],'k')
plt.xlabel('Laufzeit')
plt.xlim(1.2,2)
plt.ylim(-0.5,0.5)
plt.tight_layout()