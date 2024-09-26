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