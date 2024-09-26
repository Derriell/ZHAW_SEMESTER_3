import numpy as np 
import matplotlib.pyplot as plt 

##Aufgabe 2.1
x=np.array([5, 10, 20, 8, 4, 6, 12, 15])
y=np.array([27, 46, 73, 40, 30, 28, 47, 59])
#Streudiagramm
plt.figure(1)
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(20,80)
plt.title('Scatterplot')
#Ausgleichsgerade
plt.figure(2)
m,d = np.polyfit(x, y, 1)
plt.plot(x, y, 'o', x, m*x+d, '--r')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(20,80)
plt.title('Ausgleichsgerade')

#Korrelation Pearson
rxy_p=np.corrcoef(x,y)
print('Korrelationskoeffizient rxy_p = ',rxy_p[0,1])
#Berechnung über Mittelwerte
print(np.mean(x))
print(np.mean(y))
print(np.mean(x**2))
print(np.mean(y**2))
print(np.mean(x*y))
rxy_p_r=(np.mean(x*y)-np.mean(x)*np.mean(y))/(np.sqrt(np.mean(x**2)-np.mean(x)**2)*np.sqrt(np.mean(y**2)-np.mean(y)**2))
print(rxy_p_r)

#Korrelationskoeffizient Spearman
#Ränge bestimmen
rg_x=np.array(x).argsort().argsort() 
rg_y=np.array(y).argsort().argsort()
#Wie oben nur für die Ränge
rxy_s=np.corrcoef(rg_x,rg_y)
print('Korrelationskoeffizient rxy_s = ',rxy_s[0,1])

