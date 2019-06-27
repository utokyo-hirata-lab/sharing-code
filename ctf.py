import numpy as np
import matplotlib.pyplot as plt

#input-------------------------
E  = float(input("E  : "))   #[kV]
Cs = float(input("Cs : "))   #[mm]
Cc = float(input("Cc : "))   #[mm]
dE = float(input("dE : "))   #[eV]
#HF-3000-----------------------
#E  = 300   #[kV]
#Cs = 0.8   #[mm]
#Cc = 1.45  #[mm]
#dE = 0.3   #[eV]
#JEM-4010----------------------
#E  = 400   #[kV]
#Cs = 0.7   #[mm]
#Cc = 1.6   #[mm]
#dE = 2     #[eV]
#------------------------------
m = 9.10938356*(10**-31)    #[kg]
e = 1.60217662*(10**-19)    #[C]
h = 6.62607004*(10**-34)    #[Js]
E = E * (10**3)             #[V]
dII = 1.0 * (10**-6)        #ArbUnit
dVV = 1.0 * (10**-6)        #ArbUnit
Energy = E * e              #[J]
v = np.sqrt(2.0*Energy/m)   #[m/s]
s  = Cc*(10**6) * ((dE/E)**2 + dVV**2 + (2*dII)**2)**(1/2) #[sigma]
#wl = h/(m*v)*10**9          #[nm]
wl = 1230/np.sqrt(E*(1+E*9.78*(10**-7))) #[pm]
delta = 0.65 * (Cs * 0.001)**(1/4) * (wl*(10**(-12)))**(3/4) * (10**9)
focus = 1.20 * (Cs * 0.001)**(1/2) * (wl*(10**(-12)))**(1/2) * (10**9)
dfocus = np.sqrt((4/3) * (Cs*(10**-3)) * (wl*(10**(-12)))) * (10**9)
print("wavelength          = ",'{0:.3f}'.format(wl)," [pm]")
print("scherzer resolution = ",'{0:.3f}'.format(delta)," [nm]")
print("scherzer Focus      = ",'{0:.3f}'.format(focus),"[nm]")
print("scherzer Defocus    = ",'{0:.3f}'.format(dfocus),"[nm]")

list_q,list_y,list_z = [],[],[]
for i in range(10001):
    q  = i * 0.001
    f  = np.sqrt((4/3) * (Cs * 0.001) * (wl*(10**(-12)))) * (10**9) #[nm]
    y  = np.sin(np.pi * (f * (wl*0.001) * (q**2) - 0.5 * (Cs*(10**6)) * ((wl*0.001)**3) * (q**4)))
    ex = np.exp(-((np.pi**2) * ((wl*0.001)**2) * (q**4) * (s**2)))
    z = y * ex
    list_q.append(q)
    list_y.append(y)
    list_z.append(z)

#plot
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 12
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.width'] = 1.0
plt.rcParams['ytick.major.width'] = 1.0
plt.rcParams['lines.linewidth'] = 0.8
plt.plot(list_q,list_y,color='black')
plt.plot(list_q,list_z,color='red')
plt.xlabel(r"$q [nm^{-1}]$")
plt.ylabel(r"$\sin 2\pi \chi (q)$")
plt.xlim(0,10)
plt.ylim(-1.2,1.2)
plt.title('JEM-4010 $LaB_6$')
plt.legend(['CTF','Phase-CTF'])
plt.plot([0,10],[0,0],color='black')
plt.grid(which='major',color='lightgray',linestyle='-')
plt.grid(which='minor',color='lightgray',linestyle='-')
plt.show()
