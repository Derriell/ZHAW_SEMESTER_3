#W�rfeln
import numpy as np
import matplotlib.pyplot as plt
 
A=np.arange(1,7,1) #M�gliche Ergebnisse
h=np.array([4, 3, 4, 0, 6, 3]) #Absolute H�ufigkeiten 
f=h/20 #relative H�ufigkeiten 
 
plt.figure(1) 
plt.subplot(2,1,1)
plt.stem(A,h, use_line_collection=True) 
plt.ylabel('Absolute H�ufigkeit') 
plt.xlabel('W�rfelergebnisse')
plt.title('Absolute H�ufigkeitsfunktion - Stabdiagramm') 

plt.subplot(2,1,2)
plt.bar(A,h,0.4) 
plt.ylabel('Absolute H�ufigkeit') 
plt.xlabel('W�rfelergebnisse')
plt.title('Absolute H�ufigkeitsfunktion - S�ulendiagramm') 
plt.tight_layout()

plt.figure(2) 
plt.subplot(2,1,1)
plt.stem(A,f, linefmt='red',markerfmt='ro', use_line_collection=True) 
plt.ylabel('Relative H�ufigkeit')
plt.xlabel('W�rfelergebnisse')
plt.title('Relative H�ufigkeitsfunktion - Stabdiagramm') 
 
plt.subplot(2,1,2)
plt.bar(A,f, 0.4,color="red") 
plt.ylabel('Relative H�ufigkeit')
plt.xlabel('W�rfelergebnisse')
plt.title('Relative H�ufigkeitsfunktion - S�ulendiagramm')
plt.tight_layout()