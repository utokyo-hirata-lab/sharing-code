import numpy as np
from matplotlib import pyplot as plt

h = 6.62607004*10**(-34) #planck const / m^2 kg / s
k = 1.38064852*10**(-23) #Boltzmann const / m^2 kg /s^2 / K
m = h/k # / K s
eV = 1.60218*10**(-19) #1eVとJの変換

#O2 molecule
nyu = 4.4672*10**13 #/ 1/s vibrational const of 16O-17O
dnyu = 0.2707*10**13 #/ 1/s the difference of vibrational const between 16O-17O and 16O-16O
xe = 11.98/1580.19 #unharmonicity(振動子の非調和性)

#分配関数比
def q_vib(n, dn, t): #振動の寄与
    return m*dn/t/2 + np.log((1-np.exp(-(n+dn)*m/t))/(1-np.exp(-n*m/t)))
def q_rot(n, dn): #回転の寄与
    return np.log(n/(n+dn))

tpoints = np.arange(1, 7000) #list of temperature / K
#print((1-np.exp(-(nyu+dnyu)*m/100)))
#print((1-np.exp(-(nyu)*m/100)))


def vib_unharmonic(v, n, x): #振動子の非調和性を考慮したエネルギー準位
#    return np.exp(-((v+1/2)+x*(v+1/2)**2)*n*m/t)
    return ((v+1/2)-x*((v+1/2)**2))*n*h
def vib_harmonic(v, n, x): #調和振動子のエネルギー準位
#    return np.exp(-(v+1/2)*n*m/t)
    return (v+1/2)*n*h


q_harmonic = 0
q_unharmonic = 0

q_harmonic_prime = 0
q_unharmonic_prime = 0

#非調和性を考慮した振動子の分配関数
for i in range(65):
#    q_harmonic = q_harmonic + np.exp(-vib_harmonic(i, nyu, xe)/k/300)
    q_unharmonic = q_unharmonic + np.exp(-vib_unharmonic(i, nyu, xe)/k/300)
    q_unharmonic_prime = q_unharmonic_prime + np.exp(-vib_unharmonic(i, (nyu+dnyu), xe)/k/300)

#調和振動子の分配関数
for i in range(100000):
    q_harmonic = q_harmonic + np.exp(-vib_harmonic(i, nyu, xe)/k/300)
    q_harmonic_prime = q_harmonic_prime + np.exp(-vib_harmonic(i, (nyu+dnyu), xe)/k/300)

#div_q = q_harmonic/q_harmonic_prime
#div_q_unharmonic = q_unharmonic/q_unharmonic_prime
#print(q_harmonic, q_unharmonic)
#print(q_harmonic_prime, q_unharmonic_prime)
#print(div_q, div_q_unharmonic)
#print(np.log(div_q), np.log(div_q_unharmonic))
#print(q_vib(nyu, dnyu, 300))


#非調和性を考慮した場合としない場合のエネルギー準位の差の比較
#ls4 = []
#ls5 = []
#vpoints = []

#for i in range(65):
#    vpoints.append(i)
#    ls4.append(vib_harmonic(i, nyu, xe)/eV)
#    ls5.append(vib_unharmonic(i, nyu, xe)/eV)
#    print(vib_harmonic(i, nyu, xe)/eV, vib_unharmonic(i, nyu, xe)/eV)
#    print(vib_harmonic(i+1, nyu, xe)/eV-, vib_unharmonic(i, nyu, xe)/eV)
#plt.plot(ls4, vpoints)
#plt.plot(ls5, vpoints)
#plt.show()
#print(vib_harmonic(0, nyu, xe)/eV, vib_unharmonic(0, nyu, xe)/eV)
#print(vib_harmonic(33, nyu, xe)/eV, vib_unharmonic(33, nyu, xe)/eV)

ls1 = [] #同位体分別係数への振動の寄与
ls2 = [] #同位体分別係数への回転の寄与
ls3 = [] #トータルの同位体分別係数
ls6 = [] #非調和性を考慮した場合の同位体分別係数

#各温度における同位体分別係数
for item in tpoints:
    ls1.append(1000*q_vib(nyu, dnyu, item))
    ls2.append(1000*q_rot(nyu,dnyu))
    ls3.append(1000*(q_vib(nyu, dnyu, item)+q_rot(nyu,dnyu)))

    q_unharmonic = 0
    q_unharmonic_prime = 0
    for i in range(65):
    #    q_harmonic = q_harmonic + np.exp(-vib_harmonic(i, nyu, xe)/k/300)
        q_unharmonic = q_unharmonic + np.exp(-vib_unharmonic(i, nyu, xe)/k/item)
        q_unharmonic_prime = q_unharmonic_prime + np.exp(-vib_unharmonic(i, (nyu+dnyu), xe)/k/item)
#    print(q_unharmonic)
    div_q_unharmonic = q_unharmonic/q_unharmonic_prime
    ls6.append(np.log(div_q_unharmonic)*1000)

#print(ls6)

#横軸を1/T^2に変換
x_axis = []
for item in tpoints:
    x_axis.append(1/item/item)

#print(x_axis)
#plt.plot(tpoints, ls1)
#plt.plot(tpoints, ls2)
plt.plot(tpoints, ls3)

plt.xlabel("Temperature / K")
plt.ylabel("1000 ✕ $lnf_{O_2}$")
#plt.plot(tpoints, ls6)
#plt.xlim(200,1000)

#plt.plot(x_axis, ls1)
#plt.plot(x_axis, ls2)
#plt.plot(x_axis, ls3)
#plt.plot(x_axis, ls6)
plt.ylim(0,200)
#plt.xlim(1/6000/6000, 1/300/300)
plt.show()
