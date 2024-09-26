import numpy as np 
import matplotlib.pyplot as plt 

#Aufgabe 2.4
x=np.array([36,44,40,49,38,34,34,45]) #Schuhgrösse
y=np.array([41910,53860,37360,73450,46720,39560,20470,69040]) #Einkommen
n=np.size(x)
#Streudiagramm
plt.figure(1)
plt.plot(x,y,'o')
plt.xlabel('Schuhgrösse')
plt.ylabel('Einkommen')
plt.title('Scatterplot')

#Regressionsgerade (lernen wir später)
m,d = np.polyfit(x, y, 1)
print('Steigung m = ',m, 'Achsabschnitt d = ',d)
plt.figure(2)
plt.plot(x,y,'o',x,m*x+d,'r')
plt.xlabel('Schuhgrösse')
plt.ylabel('Einkommen')
plt.title('Scatterplot mit Ausgleichsgerade')

#Korrelationskoeffizient Pearson
rxy=np.corrcoef(x,y)
print('Korrelationskoeffizient rxy = ',rxy[0,1])


#Alternativ Pearson
s_x=np.sqrt(np.mean(np.square(x-np.mean(x))))
s_y=np.sqrt(np.mean(np.square(y-np.mean(y))))
s_xy=np.mean((x-np.mean(x))*(y-np.mean(y)))
rxy_2=s_xy/(s_x*s_y)

#Korrelationskoeffizient Spearman
#Ränge bestimmen
rg_x=np.array([3,6,5,8,4,1.5,1.5,7])
rg_y=np.array(y).argsort().argsort()+1
#Wie oben nur für die Ränge
rxy_s=np.corrcoef(rg_x,rg_y)
print('Korrelationskoeffizient rxy_s = ',rxy_s[0,1])

#Alternativ Spearman
S_rx=np.sqrt(np.sum(np.square(rg_x-np.mean(rg_x))))
S_ry=np.sqrt(np.sum(np.square(rg_y-np.mean(rg_y))))
S_rxy=np.sum((rg_x-np.mean(rg_x))*(rg_y-np.mean(rg_y)))
rxy_s2=S_rxy/(S_rx*S_ry)