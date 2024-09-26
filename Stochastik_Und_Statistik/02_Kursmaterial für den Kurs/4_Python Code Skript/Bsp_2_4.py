#Empirische Kenngrössen
import pandas as pd

df=pd.DataFrame({'x':[1,2,3],'y':[4,-1,2]})

#arithm.Mittel
m_x,m_y=df.mean()

#Varianzen (korr.),(nicht korrigiert ddof=0)
v_x,v_y=df.var()

#Standardabweichungen (korr.)
s_x,s_y=df.std()

#Kovarianz (korr.)
#Es wird eine Matrix erstellt mit den Elementen 
#v_x,s_xy,
#s_xy,v_y
s_xy=df.cov().values[0,1]

#Korr.koeffizient
r_xy_1=s_xy/(s_x*s_y)
#Es wird eine Matrix erstellt mit den Elementen
#r_xx,r_xy,
#r_xy,r_yy
r_xy_2=df.corr().values[0,1]