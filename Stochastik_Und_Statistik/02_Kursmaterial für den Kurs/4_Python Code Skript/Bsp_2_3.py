#Verschiedene Scatterplots
import pandas as pd

#Scatterplot gleichsinniger Zusammenhang
df1=pd.DataFrame({'Groesse':[163,165,166,169,170,171,171,173,174,175,177,177,179,180,185],
                  'Gewicht':[59,62,65,69,65,69,76,73,75,73,80,71,82,84,81]})
df1.plot.scatter(x='Groesse',y='Gewicht')

#Scatterplot ohne Zusammenhang
df2=pd.DataFrame({'Groesse':[163,165,166,169,170,171,171,173,174,175,177,177,179,180,185],
                  'Einkommen':[2900,1100,3600,2300,4000,5600,2100,5100,3400,1800,2100,2600,4600,3600,2300]})
df2.plot.scatter(x='Groesse',y='Einkommen')

#Scatterplot gegensinniger Zusammenhang
df3=pd.DataFrame({'Groesse':[163,165,166,169,170,171,171,173,174,175,177,177,179,180,185],
                  'Laufzeit':[2.0,1.8,1.7,1.9,1.8,1.5,1.9,1.3,1.7,1.5,1.4,1.7,1.1,1.5,1.4]})
df3.plot.scatter(x='Groesse',y='Laufzeit')

#Kennwerte korr.
df=pd.concat([df1,df2.loc[:,'Einkommen'],df3.loc[:,'Laufzeit']],axis=1)

m_x=df.mean()[0]
m_y1=df.mean()[1]
m_y2=df.mean()[2]
m_y3=df.mean()[3]
s_x=df.std()[0]
s_y1=df.std()[1]
s_y2=df.std()[2]
s_y3=df.std()[3]
s_xy1=df.cov().values[0,1]
s_xy2=df.cov().values[0,2]
s_xy3=df.cov().values[0,3]
r_xy1=df.corr().values[0,1]
r_xy2=df.corr().values[0,2]
r_xy3=df.corr().values[0,3]

#Kennwerte df1
k1=pd.DataFrame([m_x,m_y1,s_x,s_y1,s_xy1,r_xy1],
                index=['Mittelw.x','Mittelw.y','St.abw.x','St.abw.y','Kovarianz','Korr.Koeff.'])
print(k1)

#Kennwerte df1
k2=pd.DataFrame([m_x,m_y2,s_x,s_y2,s_xy2,r_xy2],
                index=['Mittelw.x','Mittelw.y','St.abw.x','St.abw.y','Kovarianz','Korr.Koeff.'])
print(k2)

#Kennwerte df1
k3=pd.DataFrame([m_x,m_y3,s_x,s_y3,s_xy3,r_xy3],
                index=['Mittelw.x','Mittelw.y','St.abw.x','St.abw.y','Kovarianz','Korr.Koeff.'])
print(k3)

#Zusammengefasst
k=pd.concat([df.mean(),df.std(),df.cov().loc['Groesse',:]],keys=['Mittelw.','Stand.abw','Kovarianz'],axis=1)
print(k)


#Korrelationskoeffizient pandas-Funktion
df=pd.concat([df1,df2.loc[:,'Einkommen'],df3.loc[:,'Laufzeit']], 
              axis=1)
print(df)

r_xy=df.corr()
print(r_xy)