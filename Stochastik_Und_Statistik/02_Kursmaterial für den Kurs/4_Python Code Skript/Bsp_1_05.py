#Anzahl Flugreisen
#Stichprobe bei 30 Haushalten
import numpy as np
import matplotlib.pyplot as plt
 
A=np.array([1, 2, 3, 4, 5]) #Anzahl der Flugreisen 
h=np.array([9, 8, 5, 7, 1]) #Absolute Häufigkeit 
n=np.sum(h) #Grösse der Stichprobe
f=h/n #relative Häufigkeit
H=np.cumsum(h) #absolute Summenhäufigkeit
F=np.cumsum(f) #relative Summenhäufigkeit, kumulative Verteilungsfunktion(CDF) 

#Anpassung der Arrays, damit der Plot schöner wird
A_p=np.concatenate((np.array([0]),A,np.array([6])),axis=0)
h_p=np.concatenate((np.array([0]),h,np.array([0])),axis=0)
H_p=np.concatenate((np.array([0]),H,np.array([n])),axis=0)
f_p=h_p/n
F_p=np.cumsum(f_p)

plt.figure(1) 
plt.subplot(1,2,1)
plt.bar(A_p, h_p)
plt.title('Absolute Häufigkeit')
plt.xlabel('Anzahl Flugreisen')
plt.ylabel('Anzahl Haushalte')
plt.xlim(0,6) 
plt.ylim(0,30)

plt.subplot(1,2,2)
plt.step(A_p, H_p,where='post')
plt.title('Absolute Summenhäufigkeit')
plt.xlabel('Anzahl Flugreisen')
plt.ylabel('Anzahl Haushalte') 
plt.xlim(0,6) 
plt.ylim(0,30)
plt.tight_layout()

plt.figure(2) 
plt.subplot(1,2,1)
plt.bar(A_p, f_p, color='red')
plt.title('Relative Häufigkeit')
plt.xlabel('Anzahl Flugreisen')
plt.ylabel('Anteil')
plt.xlim(0,6) 
plt.ylim(0,1) 
 
plt.subplot(1,2,2)
plt.step(A_p, F_p,where='post', color='red')
plt.title('Kumulative Verteilungsfunktion')
plt.xlabel('Anzahl Flugreisen')
plt.ylabel('Anteil')
plt.xlim(0,6) 
plt.ylim(0,1) 
plt.tight_layout()
