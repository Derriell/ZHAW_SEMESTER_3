#Würfeln
import numpy as np
import matplotlib.pyplot as plt
 
A=np.arange(1,7,1) #Mögliche Ergebnisse
h=np.array([4, 3, 4, 0, 6, 3]) #Absolute Häufigkeiten 
f=h/20 #relative Häufigkeiten 
 
plt.figure(1) 
plt.subplot(2,1,1)
plt.stem(A,h, use_line_collection=True) 
plt.ylabel('Absolute Häufigkeit') 
plt.xlabel('Würfelergebnisse')
plt.title('Absolute Häufigkeitsfunktion - Stabdiagramm') 

plt.subplot(2,1,2)
plt.bar(A,h,0.4) 
plt.ylabel('Absolute Häufigkeit') 
plt.xlabel('Würfelergebnisse')
plt.title('Absolute Häufigkeitsfunktion - Säulendiagramm') 
plt.tight_layout()

plt.figure(2) 
plt.subplot(2,1,1)
plt.stem(A,f, linefmt='red',markerfmt='ro', use_line_collection=True) 
plt.ylabel('Relative Häufigkeit')
plt.xlabel('Würfelergebnisse')
plt.title('Relative Häufigkeitsfunktion - Stabdiagramm') 
 
plt.subplot(2,1,2)
plt.bar(A,f, 0.4,color="red") 
plt.ylabel('Relative Häufigkeit')
plt.xlabel('Würfelergebnisse')
plt.title('Relative Häufigkeitsfunktion - Säulendiagramm')
plt.tight_layout()