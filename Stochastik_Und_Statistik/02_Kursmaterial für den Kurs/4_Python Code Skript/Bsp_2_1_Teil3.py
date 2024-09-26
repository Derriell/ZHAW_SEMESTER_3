#Zwei metrische Merkmale
import pandas as pd

df=pd.read_excel('Bsp_2_1.xlsx')
print (df.columns) #Bezeichnung der Datenreihen

#Scatterplot
df.plot.scatter(x='Einkauf', y='Alter')

#Subset der Daten
df_=df.loc[df['Zivilstand'] == 'Ledig',:]
df_.plot.scatter(x='Einkauf', y='Alter')





