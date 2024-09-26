#Zusammenhang Grösse Gewicht
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Scatterplot gleichsinniger Zusammenhang
x=np.array([163,165,166,169,170,171,171,173,174,175,177,177,179,180,185])
y=np.array([59,62,65,69,65,69,76,73,75,73,80,71,82,84,81])

plt.figure(1)
plt.plot(x,y,'o')
plt.xlabel('Grösse')
plt.ylabel('Gewicht')

#Kennwerte korr.
m_x=np.mean(x)
m_y=np.mean(y)
s_x=np.std(x,ddof=1)
s_y=np.std(y,ddof=1)
s_xy=np.cov([x,y])[1,0]
r_xy=np.corrcoef([x,y])[1,0]

#Kennwerte df1
k1=pd.DataFrame([m_x,m_y,s_x,s_y,s_xy,r_xy],
                index=['Mittelw.x','Mittelw.y','St.abw.x','St.abw.y','Kovarianz','Korr.Koeff.'])
print(k1)

#Regressionsgerade Variante 1
m1=s_xy/s_x**2
d1=m_y-m_x*m1

#Regressionsgerade Variante 2 mit numpy
m2,d2 = np.polyfit(x, y, 1)

#Scatterplot mit Ausgleichsgerade
plt.figure(2)
plt.plot(x,y,'o',x,m2*x+d2,'r')
plt.xlabel('GrÃ¶sse')
plt.ylabel('Gewicht')
