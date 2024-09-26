#Occasionsfahrzeuge
import pandas as pd
import matplotlib.pyplot as plt

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
