#Programmlaufzeiten
import numpy as np
import matplotlib.pyplot as plt

x=np.array([400, 399, 398, 400, 398, 399, 397, 400, 402, 399, 401, 399, 400, 402, 398, 400, 399, 401, 399, 399])
x_min=np.min(x)
x_max=np.max(x)
n=np.size(x)
A=np.unique(x, return_counts=True)[0] #Mögliche Ergebnisse
#X=np.array(x_min,(x_max+1),1) # Mögliche Ergebnisse
h=np.unique(x, return_counts=True)[1] #Absolute Häufigkeiten
f=h/n # relative Häufigkeiten 
 
plt.figure(1) 
plt.subplot(2,1,1)
plt.stem(A,h,use_line_collection=True) 
plt.ylabel('Absolute Häufigkeit') 
plt.xlabel('Laufzeit')
plt.title('Absolute Häufigkeitsfunktion - Stabdiagramm') 
 
plt.subplot(2,1,2)
plt.bar(A,h,0.3) 
plt.ylabel('Absolute Häufigkeit')
plt.xlabel('Laufzeit')
plt.title('Absolute Häufigkeitsfunktion - Säulendiagramm') 
plt.tight_layout()

plt.figure(2) 
plt.subplot(2,1,1)
plt.stem(A,f,linefmt='red',markerfmt='ro',use_line_collection=True) 
plt.ylabel('Relative Häufigkeit') 
plt.xlabel('Laufzeit')
plt.title('Relative Häufigkeitsfunktion - Stabdiagramm') 
 
plt.subplot(2,1,2)
plt.bar(A,f,0.3,color='red') 
plt.ylabel('Relative Häufigkeit') 
plt.xlabel('Laufzeit')
plt.title('Relative Häufigkeitsfunktion - Säulendiagramm')
plt.tight_layout()