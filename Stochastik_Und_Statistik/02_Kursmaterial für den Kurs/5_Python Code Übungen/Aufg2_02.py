import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats as ss

#Aufgabe, 2.2
x=np.array([3, 4, 6, 5, 9, 15])
y=np.array([2, 4, 1, 2, 6, 45])
n=np.size(x)
#Streudiagramm
plt.figure(1)
plt.plot(x,y,'o')
plt.title('Scatterplot')
plt.xlabel('x')
plt.ylabel('y')

#Daten ohne Ausreisser
xneu=x[0:-1]
yneu=y[0:-1]
nneu=np.size(yneu)

#Korrelationskoeffizient Pearson
rxy_p=np.corrcoef(x,y)
print('Korr.koef. mit Ausreisser rxy_p = ',rxy_p[0,1])
rxy_p_neu=np.corrcoef(xneu,yneu)
print('Korr.koef. ohne Ausreisser rxy_p = ',rxy_p_neu[0,1])

#Korrelationskoeffizient Spearman (Achtung verbundene Ränge anpassen)
rg_x=np.array(x).argsort().argsort() 
rg_y=np.array(y).argsort().argsort()
rg_y=rg_y.astype(float)
for k in range(0,n-1):
        for j in range(0,n-1):
            if y[k]==y[j]:
                rg_y[k]=(rg_y[k]+rg_y[j])/2
                rg_y[j]=rg_y[k]
rxy_s=np.corrcoef(rg_x,rg_y)
print('Korr.koef. mit Ausreisser rxy_s = ',rxy_s[0,1])

rg_xneu=np.array(xneu).argsort().argsort() 
rg_yneu=np.array(yneu).argsort().argsort()
rg_yneu=rg_yneu.astype(float)
for k in range(0,nneu-1):
        for j in range(0,nneu-1):
            if yneu[k]==yneu[j]:
                rg_yneu[k]=(rg_yneu[k]+rg_yneu[j])/2
                rg_yneu[j]=rg_yneu[k]
rxy_s_neu=np.corrcoef(rg_xneu,rg_yneu)
print('Korr.koef. ohne Ausreisser rxy_s = ',rxy_s_neu[0,1])

#mit Scipy-Funktionen
rg_x_n=ss.rankdata(x)
rg_y_n=ss.rankdata(y)
rxy_s_n1=np.corrcoef(rg_x_n,rg_y_n)
print('Korr.koef. mit Ausreisser Scipy Var.1', rxy_s_n1[0,1])
rxy_s_n2=ss.spearmanr(x,y)
print('Korr.koef. mit Ausreisser Scipy Var.2', rxy_s_n2[0])

#Regressionsgerade mit Ausreisser (das lernen wir später)
m1,d1 = np.polyfit(x, y, 1)

#Regressionsgerade ohne Ausreisser (das lernen wir später)
m2,d2= np.polyfit(xneu, yneu, 1)

#Grafik mit beiden Regressionsgeraden
plt.figure(2)
plt.plot(x,y,'o')
plt.plot(x,m1*x+d1,'r',label='mit Ausreisser')
plt.plot(x,m2*x+d2,'g',label='ohne Ausreisser')
plt.legend(loc='lower right')
plt.title('Mit Ausgleichsgeraden')
plt.xlabel('x')
plt.ylabel('y')