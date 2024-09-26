#Kovarianz und KorrKoeff
import pandas as pd
import matplotlib.pyplot as plt

df=pd.DataFrame({'x':[1,2,3,4,5],
                 'y_a':[5,7,9,11,13],'y_b':[5,7,8,11,12],
                 'y_c':[6,3,8,5,6],'y_d':[6,3,8,5,4],
                 'y_e':[9,8,7,4,2],'y_f':[10,8,6,4,2]})

#Kovarianz (korr.)
s_xy=df.cov()

#Korr.koeffizient
r_xy=df.corr()

#Kennwerte
KW=pd.concat([s_xy.loc['y_a':'y_f','x'],r_xy.loc['y_a':'y_f','x']], 
              axis=1, keys=['s_xy', 'r_xy'])
print(KW)

plt.figure(1)
fig, axs = plt.subplots(2)
df.plot.scatter(x='x', y='y_a',ax=axs[0],xlim=[0,6],ylim=[0,15])
df.plot.scatter(x='x', y='y_b',ax=axs[1],xlim=[0,6],ylim=[0,15])
plt.tight_layout()

plt.figure(2)
fig, axs = plt.subplots(2)
df.plot.scatter(x='x', y='y_c',ax=axs[0],xlim=[0,6],ylim=[0,15])
df.plot.scatter(x='x', y='y_d',ax=axs[1],xlim=[0,6],ylim=[0,15])
plt.tight_layout()

plt.figure(3)
fig, axs = plt.subplots(2)
df.plot.scatter(x='x', y='y_e',ax=axs[0],xlim=[0,6],ylim=[0,15])
df.plot.scatter(x='x', y='y_f',ax=axs[1],xlim=[0,6],ylim=[0,15])
plt.tight_layout()