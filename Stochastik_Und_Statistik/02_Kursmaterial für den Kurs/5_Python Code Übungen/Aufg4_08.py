#Aufgabe 4.8
#Geburtstagsproblem berechnet
n=30
pr=1
for j in range(1,n):
    pr= pr*((365-j)/365)
    print('n = ', j+1, ', p = ', 1-pr)  
        




