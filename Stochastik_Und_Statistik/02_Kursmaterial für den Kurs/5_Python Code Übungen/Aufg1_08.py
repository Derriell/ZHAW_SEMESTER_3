import numpy as np 

## Aufgabe 1.8
#Wir vergleichen die CDF WErte der beiden Springer für die beiden Weiten
RKLGr=np.array([720, 740, 760, 780, 800, 820])
print('Rechte Klassengrenzen = ',RKLGr)  #Rechte Klassengrenzenn 
ha= np.array([19, 24, 26, 27, 10, 5]) 
print('abs. Häufigkeit Springer A = ',ha) #absolute Häufigkeiten Springer A 
hb= np.array([4, 8, 52, 40, 32, 24]) 
print('abs. Häufigkeiten Springer B = ',hb) # absolute Häufigkeiten Springer B
CDFA= np.cumsum(ha)/np.sum(ha)
print('CDF Werte Springer A = ', CDFA) # CDF WErte von A 
CDFB=np.cumsum(hb)/np.sum(hb) 
print('CDF Werte Springer B = ', CDFB)# CDF WErte von B 
#Bewertung der Ergebnisse durch Interpolation
WeiteA=730  
WeiteB=750
#Obere und untere Klassen festlegen und dann interpolieren für A
Ua=np.where(RKLGr<WeiteA)[0]
Oa=np.where(RKLGr>=WeiteA)[0]
qa=(WeiteA-RKLGr[Ua[-1]])/(RKLGr[Oa[0]]-RKLGr[Ua[-1]])*(CDFA[Oa[0]]-CDFA[Ua[-1]])+CDFA[Ua[-1]]
print('qa = ',qa)
#Obere und untere Klassen festlegen und dann interpolieren für B
Ub=np.where(RKLGr<WeiteB)[0]
Ob=np.where(RKLGr>=WeiteB)[0]
print(CDFB[Ub[-1]])
qb=(WeiteB-RKLGr[Ub[-1]])/(RKLGr[Ob[0]]-RKLGr[Ub[-1]])*(CDFB[Ob[0]]-CDFB[Ub[-1]])+CDFB[Ub[-1]]
print('qb = ',qb)
