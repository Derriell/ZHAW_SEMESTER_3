import numpy as np  

## Aufgabe 1.10
X=np.array([ 2.1,  2.4,  2.8,  3.1,  4.2,  4.9,  5.1,  6.0,  6.4,  7.3, 10.8,  
   12.5,  13.0,  13.7,  14.8,  17.6,  19.6,  23.0,  25.0,  35.2,  39.6]) 
Med=np.median(X) # Median 10.8
Mittel=1/X.size*np.sum(X) # Mittelwert 12.81
Var=1/X.size*np.sum(np.square(X))-np.square(Mittel) # Varianz 108.62
St=np.sqrt(Var) # Standardabweichung 10.42
kVar=X.size/(X.size-1)*Var  # korrigierte Varianz 114.04
kSt=np.sqrt(kVar) # korrigierte Standardabweichung 10.68
S=np.std(X)
