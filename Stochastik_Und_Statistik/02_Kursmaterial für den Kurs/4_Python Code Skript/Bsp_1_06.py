# Beispiel: Programmlaufzeiten
# Teil2
import numpy as np
import matplotlib.pyplot as plt

A=np.arange(397,403) # M�gliche Ergebnisse
h=np.array([1, 3, 7, 5, 2, 2]) # Absolute H�ufigkeiten 
f=h/np.sum(h) # relative H�ufigkeiten 
F=np.cumsum(f) # kummulative kumulative Verteilungsfunktion
 
plt.figure(1) 
plt.subplot(2,1,1)
plt.stem(A,h,use_line_collection=True) 
plt.ylabel('Absolute H�ufigkeit')
plt.xlabel('Laufzeit')
plt.title('Absolute H�ufigkeitsfunktion - Stabdiagramm') 
 
plt.subplot(2,1,2)
plt.bar(A,h,0.3) 
plt.ylabel('Absolute H�ufigkeit')
plt.xlabel('Laufzeit')
plt.title('Absolute H�ufigkeitsfunktion - S�ulendiagramm') 
plt.tight_layout()

plt.figure(2) 
plt.subplot(2,1,1)
plt.stem(A,f,linefmt='red',markerfmt='ro',use_line_collection=True) 
plt.ylabel('Relative H�ufigkeit') 
plt.xlabel('Laufzeit')
plt.title('Relative H�ufigkeitsfunktion - Stabdiagramm') 
 
plt.subplot(2,1,2)
plt.bar(A,f,0.3,color='r') 
plt.ylabel('Relative H�ufigkeit')
plt.xlabel('Laufzeit')
plt.title('Relative H�ufigkeitsfunktion - S�ulendiagramm') 
plt.tight_layout()

plt.figure(3) 
plt.subplot(1,2,1)
plt.stem(A, f,linefmt='red',markerfmt='ro',use_line_collection=True)
plt.ylabel('Anteil')
plt.xlabel('Laufzeit')
plt.title('Relative H�ufigkeit')

plt.subplot(1,2,2)
A_p=np.concatenate((np.array([A[0]-1]),A,np.array([A[-1]+1])),axis=0)
F_p=np.concatenate((np.array([0]),F,np.array([1])),axis=0)
plt.step(A_p,F_p,color='red',where='post')
plt.title('Kumulative Verteilungsfunktion')
plt.xlabel('Laufzeit')
plt.ylabel('Anteil')
plt.tight_layout()