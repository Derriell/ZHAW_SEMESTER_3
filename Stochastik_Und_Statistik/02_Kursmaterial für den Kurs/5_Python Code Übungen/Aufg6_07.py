import numpy as np 
import matplotlib.pyplot as plt 

#Aufgabe 6.7
#Gaspreis
gasv=np.array([10, 10.6, 10.4, 11.1, 11.9, 13.8, 13.7, 13.7, 12.2, 12.9, 13.6, 13.8, 13.6, 13.6, 13.8])
#Gaspreis
gpr=np.array([0.92, 1.04, 1.15, 1.11, 1.08, 1.11, 1.05, 0.84, 0.80, 0.80, 0.82, 0.85, 0.83, 0.80, 0.78])
#Fernwärmepreis
fpr=np.array([0.90, 1.04, 1.08, 1.11, 1.10, 1.11, 1.14, 1.07, 1.02, 1.00, 1.01, 1.02, 1.00, 0.97, 0.95 ])
#Darstellung der Daten
fig1=plt.figure(1)
ax = fig1.add_subplot(111, projection='3d')
for k in range(0, gasv.size,1):
    ax.scatter(gpr[k],fpr[k],gasv[k],c='b', marker='o')

#Lineare Regression 3d
#minimize Sum((gasv[i] - (a*gpr[i] + b*fpr[i] + c))^2)
#then this is a standard linear algebra problem.
A = np.column_stack([gpr, fpr, np.ones_like(gpr)])
abc, residuals, rank, s = np.linalg.lstsq(A, gasv, rcond=-1)
a=abc[0]
b=abc[1]
c=abc[2]

#Prognostizierte Preise
Bergasv=a*gpr+b*fpr+c
Res=gasv-Bergasv
columns = ("Gasverbrauch", "BerechneterVerbrauch", "Residuen")
cellText=np.column_stack([gasv, Bergasv.round(3), Res.round(3)])
plt.figure(2)
plt.axis('off')
plt.table(cellText=cellText,colLabels=columns,loc='center' )

#Residuenplot
plt.figure(3)
plt.plot(Bergasv,Res,'g*')
plt.xlim([10,15])
plt.ylim([-2.5,2.5])
plt.plot([10,15],[0,0],'k')

fig4=plt.figure(4)
ax = fig4.add_subplot(111, projection='3d')
for k in range(0, gasv.size,1):
    ax.scatter(gpr[k],fpr[k],gasv[k],c='b', marker='o')
X = np.arange(0.7, 1.2, 0.05)
Y = np.arange(0.7, 1.2, 0.05)
X,Y=np.meshgrid(X, Y)
Z= a*X+b*Y+c
ax.plot_wireframe(X,Y,Z)


