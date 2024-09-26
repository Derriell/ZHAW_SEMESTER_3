import numpy as np 
import matplotlib.pyplot as plt 

## Aufgabe 1.12
Miete = np.array([274, 281, 310, 435, 475, 480, 483, 490, 510, 515, 520, 530, 
                  560, 565, 570, 580, 584, 589, 600, 605, 614, 625, 628, 639,
                  650, 672, 675, 677, 695, 731, 749, 772, 775, 800, 825, 840,
                  850, 855, 857, 860, 870, 876, 880, 895, 896, 900, 907, 914, 
                  920, 950, 955, 970, 974, 980, 990, 1000, 1008, 1020, 1025, 
                  1035, 1037, 1040, 1042, 1050, 1070, 1080, 1085, 1095, 1096, 
                  1120, 1204, 1220, 1225, 1226, 1245, 1250, 1260, 1275, 1301, 
                  1305, 1320, 1325, 1343, 1375, 1395, 1398, 1430, 1460, 1470, 
                  1480, 1481, 1485, 1510, 1547, 1552, 1554, 1555, 1560, 1565, 
                  1570, 1595, 1645, 1660, 1679, 1725, 1730, 1745, 1750, 1770, 
                  1825, 1830, 1835, 1920, 1930, 1945, 2000, 2130, 2345, 2520, 
                  2730, 3130, 3575, 4230, 4725])
hi = np.array([1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 
              1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 4, 1, 
              1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 4, 1, 
              1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
              1, 1, 1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
Stichprobe=[] 
for k in range (0,Miete.size): 
    Stichprobe=np.append([Stichprobe], np.ones(hi[k])*[Miete[k]]) #Rohdaten werden generiert 
print(Stichprobe)
#Boxplot machen
plt.figure()
plt.boxplot(Stichprobe)
plt.xlabel('Mietwohnungen')
plt.ylabel('Monatsmiete')
plt.figure()
plt.boxplot(Stichprobe,vert=False)
plt.ylabel('Mietwohnungen')
plt.xlabel('Monatsmiete')
#Datenanalyse
Median=np.median(Stichprobe)
Q1=np.percentile(Stichprobe,25)
Q3=np.percentile(Stichprobe,75)
IntQ=Q3-Q1
Anto=Q3+1.5*IntQ
Antu=Q1-1.5*IntQ
