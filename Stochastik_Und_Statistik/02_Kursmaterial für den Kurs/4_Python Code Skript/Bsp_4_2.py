#Zufallsvariable Klassen 
import numpy as np 
import matplotlib.pyplot as plt 

X=np.arange(0,6)
K1=np.array([1,3,2,7,3,4])
K2=np.array([0,1,5,9,5,0])
PMF1=1/np.sum(K1)*K1
PMF2=1/np.sum(K2)*K2
print(PMF1)
print(PMF2)

#Kennwerte
mu1=1/np.sum(K1)*np.sum(K1*X)
mu2=1/np.sum(K2)*np.sum(K2*X)
s12=1/np.sum(K1)*np.sum(K1*(X-mu1)**2)
s22=1/np.sum(K2)*np.sum(K2*(X-mu2)**2)
s1=np.sqrt(s12)
s2=np.sqrt(s22)


plt.figure(1)
plt.subplot(211)
plt.stem(X,PMF1,use_line_collection='true',basefmt='None')
plt.plot([mu1-s1,mu1+s1],[0,0],'ro-', label='s1=1.45')
plt.plot([mu1],[0],'go', label='mu1=3')
plt.legend()
plt.title('Punkteverteilung Klasse 1') 
plt.ylabel('Rel. Häufigkeit')
plt.xlim(0,5)
plt.ylim(0,0.5)

plt.subplot(212)
plt.stem(X,PMF2,use_line_collection='true',basefmt='None')
plt.plot([mu2-s2,mu2+s2],[0,0],'ro-',label='s2=0.83' )
plt.plot([mu2],[0],'go', label='mu2=2.9')
plt.legend()
plt.title('Punkteverteilung Klasse 2') 
plt.ylabel('Rel. Häufigkeit')
plt.xlim(0,5)
plt.ylim(0,0.5)
plt.tight_layout()
