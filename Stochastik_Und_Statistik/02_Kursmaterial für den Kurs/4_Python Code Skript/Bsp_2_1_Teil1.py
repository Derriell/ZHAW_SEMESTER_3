#Zwei kategorielle Merkmale
import pandas as pd
from statsmodels.graphics.mosaicplot import mosaic

df=pd.read_excel('Bsp_2_1.xlsx')
print (df.columns) #Bezeichnung der Datenreihen

#Kontingenztabelle
df['Kaufkraft'] = df['Kaufkraft'].astype('category').cat.set_categories(['tief','mittel','hoch','sehr hoch'])
table=pd.crosstab(df['Zivilstand'],df['Kaufkraft'])
print(table)

#Mosaikplot
mosaic(table.stack(),gap=0.01,title='Kaufkraft vs. Zivilstand')





