#Programmlaufzeiten
import numpy as np
import matplotlib.pyplot as plt

x=np.array([400, 399, 398, 400, 398, 399, 397, 400, 402, 399, 401, 399, 400, 402, 398, 400, 399, 401, 399, 399])
x_min=np.min(x)
x_max=np.max(x)
n=np.size(x)
A=np.unique(x, return_counts=True)[0] #M�gliche Ergebnisse
#X=np.array(x_min,(x_max+1),1) # M�gliche Ergebnisse
h=np.unique(x, return_counts=True)[1] #Absolute H�ufigkeiten
f=h/n # relative H�ufigkeiten 
 
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
plt.bar(A,f,0.3,color='red') 
plt.ylabel('Relative H�ufigkeit') 
plt.xlabel('Laufzeit')
plt.title('Relative H�ufigkeitsfunktion - S�ulendiagramm')
plt.tight_layout()