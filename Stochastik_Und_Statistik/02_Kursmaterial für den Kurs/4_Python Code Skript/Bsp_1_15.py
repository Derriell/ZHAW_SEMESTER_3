#Boxplots mehrerer Stichproben zum Vergleich 
import numpy as np
import pandas as pd

X1=np.array([4, 4, 0, 3, 5, 3, 1]) #Stichprobe X1
X2=np.array([-2, 1, 5, 7]) #Stichprobe X2
X3=np.array([-7, -2, -1, -1, 1, 1, 3, 8]) #Stichprobe X3 

#Arbeiten mit Pandas, da mehrere Datenreihen verwendet
#Fehlende Daten werden mit NaN aufgefüllt
df=pd.DataFrame((X1,X2,X3),index=['X1', 'X2', 'X3'])
df=df.transpose()
df.boxplot()

#Darstellung der Quartile
Q11=np.quantile(X1,0.25)
Q12=np.quantile(X1,0.5)
Q13=np.quantile(X1,0.75)
Q21=np.quantile(X2,0.25)
Q22=np.quantile(X2,0.5)
Q23=np.quantile(X2,0.75)
Q31=np.quantile(X3,0.25)
Q32=np.quantile(X3,0.5)
Q33=np.quantile(X3,0.75)
df_q=pd.DataFrame(([Q11,Q12,Q13],[Q21,Q22,Q23],[Q31,Q32,Q33]),index=['X1', 'X2', 'X3'],columns=['Q1', 'Q2', 'Q3'])
print(df_q)

