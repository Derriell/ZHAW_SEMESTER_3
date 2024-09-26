#KQM mehrere Merkmale
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

#Occasionsfahrzeuge
#Preis

df=pd.DataFrame({'Preis':[28500,31500,28900,29500,24500,25500,38800,25400,23900,29800,22500],
                 'Jg':[2017,2019,2019,2017,2019,2018,2019,2016,2017,2019,2016],
                 'Km':[28100,28200,28000,36200,41300,36600,22500,66000,92000,16000,8400],})

#Kovarianz (korr.)
s_xy=df.cov()

#Korr.koeffizient
r_xy=df.corr()
print(r_xy)

#Matrix von Streudiagrammen
plt.figure(1)
pd.plotting.scatter_matrix(df, alpha=1)

#Lineare Regression
#Minimieren Sum((Preis[i] - (a*Jg[i] + b*Km[i] + c))^2)
#Standard lineare Algebra Problem 
#Es gibt auch noch diverse andere Herangehensweisen
Preis=df.iloc[:,0]
Jg=df.iloc[:,1]
Km=df.iloc[:,2]
X = np.column_stack([Jg, Km, np.ones_like(Jg)])
abc, residuals, rank, s = np.linalg.lstsq(X, Preis, rcond=-1)
a=abc[0]
b=abc[1]
c=abc[2]

#Prognostizierte Preise
Preis_b=a*Jg+b*Km+c
Res=Preis-Preis_b
columns = ("Preis", "Berechneter Preis", "Residuen")
cellText=np.column_stack([Preis, Preis_b, Res])

plt.figure(3)
plt.axis('off')
plt.table(cellText=cellText,colLabels=columns,loc='center' )

#Residuenplot
plt.figure(4)
plt.plot(Preis_b,Res,'g*',[23000,33000],[0,0],'k')
plt.xlim(23000,32000)
plt.ylim(-10000,10000)



