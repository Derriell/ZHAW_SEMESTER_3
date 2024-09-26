import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

#Aufgabe 2.12
#Gaspreis
gasv=np.array([10, 10.6, 10.4, 11.1, 11.9, 13.8, 13.7, 13.7, 12.2, 12.9, 13.6, 13.8, 13.6, 13.6, 13.8])
#Gaspreis
gpr=np.array([0.92, 1.04, 1.15, 1.11, 1.08, 1.11, 1.05, 0.84, 0.80, 0.80, 0.82, 0.85, 0.83, 0.80, 0.78])
#Fernwärmepreis
fpr=np.array([0.90, 1.04, 1.08, 1.11, 1.10, 1.11, 1.14, 1.07, 1.02, 1.00, 1.01, 1.02, 1.00, 0.97, 0.95 ])

#Zusammenführung der Daten in ein DataFrame
df=pd.DataFrame({'gasv':gasv,'gpr':gpr,'fpr':fpr})

#Korr.koeffizient
r_xy=df.corr()
print(r_xy)

#Matrix von Streudiagrammen
plt.figure(1)
pd.plotting.scatter_matrix(df, alpha=1)
plt.show()

plt.figure(2)
ax = plt.axes(projection='3d')
ax.plot3D(df['gasv'], df['gpr'],df['fpr'],'bo')
ax.set_xlabel('Gasverbrauch')
ax.set_ylabel('Gaspreis')
ax.set_zlabel('Fernwärmepreis')
