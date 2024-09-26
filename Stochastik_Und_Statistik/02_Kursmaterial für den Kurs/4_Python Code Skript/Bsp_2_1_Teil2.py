#Kategorielles und metrisches Merkmal
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_excel('Bsp_2_1.xlsx')
print (df.columns) #Bezeichnung der Datenreihen

#Auswertung für 
t=df.loc[df['Kaufkraft'] == 'tief',:]
m_t=t['Einkauf'].mean()
s_t=t['Einkauf'].std()
m=df.loc[df['Kaufkraft'] == 'mittel',:]
m_m=m['Einkauf'].mean()
s_m=m['Einkauf'].std()
h=df.loc[df['Kaufkraft'] == 'hoch',:]
m_h=h['Einkauf'].mean()
s_h=h['Einkauf'].std()
s=df.loc[df['Kaufkraft'] == 'sehr hoch',:]
m_s=s['Einkauf'].mean()
s_s=s['Einkauf'].std()
KW=pd.DataFrame(([m_t,s_t],[m_m,s_m],[m_h,s_h],[m_s,s_s]),index=['tief','mittel','hoch','sehr hoch'], columns=['Mittelwert','Standardabweichung'])
print(KW)

#Boxplot
plt.figure()
plt.subplot(2,2,1)
df_=pd.DataFrame(([t['Einkauf'],m['Einkauf'],h['Einkauf'],s['Einkauf']]),index=['tief', 'mittel', 'hoch','sehr hoch'])
df_=df_.transpose()
sns.boxplot( data=df_)  #df_.boxplot() Alternativ mit Pandas
plt.ylabel('Einkaufsbetrag')
plt.xlabel('Kaufkraft')

#Stripplot
plt.subplot(2,2,2)
sns.stripplot( data=df_,size=0.8)
plt.xlabel('Kaufkraft')
plt.tight_layout()