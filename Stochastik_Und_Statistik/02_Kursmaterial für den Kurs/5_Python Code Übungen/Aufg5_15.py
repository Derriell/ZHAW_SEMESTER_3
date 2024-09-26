import scipy.stats as ss
 
#Aufgabe 15
M=1.55
S=0.2
N=2000
n=ss.norm(M,S)
print('Lösung a) P(X<1)=', n.cdf(1), ' Damit sind das', n.cdf(1)*N, 'Schüler') 
print('Lösung b) P(1.2<=X<=1.3)=', n.cdf(1.3)-n.cdf(1.2),' Damit sind das', (n.cdf(1.3)-n.cdf(1.2))*N, 'Schüler')
print('Lösung c) P(X>2)=', 1-n.cdf(2), ' Damit sind das', ( 1-n.cdf(2))*N, 'Schüler')

