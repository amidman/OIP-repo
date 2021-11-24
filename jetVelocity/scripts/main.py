import numpy as np
import matplotlib.pyplot as plt
import textwrap
import scipy
from scipy.signal import savgol_filter
from scipy.integrate import trapz

#reading txt files (ADC)
L_00 = (np.genfromtxt("общеинж/jetVelocity/P00.txt",comments="\n"))
L_10 = (np.genfromtxt("общеинж/jetVelocity/P10.txt",comments="\n"))
L_20 = (np.genfromtxt("общеинж/jetVelocity/P20.txt",comments="\n"))
L_30 = (np.genfromtxt("общеинж/jetVelocity/P30.txt",comments="\n"))
L_40 = (np.genfromtxt("общеинж/jetVelocity/P40.txt",comments="\n"))
L_50 = (np.genfromtxt("общеинж/jetVelocity/P50.txt",comments="\n"))
L_60 = (np.genfromtxt("общеинж/jetVelocity/P60.txt",comments="\n"))
L_70 = (np.genfromtxt("общеинж/jetVelocity/P70.txt",comments="\n"))


#reading txt files (ADC)
P_00 = np.average(np.genfromtxt("общеинж/jetVelocity/calatm.txt",comments="\n"))
P_110 = np.average(np.genfromtxt("общеинж/jetVelocity/caljet.txt",comments="\n"))

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

location = ['center', 'left', 'right']
myTitle = "Calibration factor"
ax1.set_title("\n".join(textwrap.wrap(myTitle, 80)), loc =location[0])
ax1.set_ylabel('Pressure, mmHg')
ax1.set_xlabel('n*Pressure + d, 1un.')

plt.scatter([P_00, P_110], [0, 110], color = 'darkblue')
n, d = np.linalg.lstsq([[P_00, 1], [P_110, 1]], [0, 110] , rcond=None)[0]
plt.plot([P_00, P_110], n*np.array([P_00, P_110]) + d, 'r', label = "lsqm")

plt.legend()

# add a grid
plt.minorticks_on()
plt.grid(which='major', color='lightgrey', linestyle='-', linewidth=1)
plt.grid(which='minor', color='lightgrey', linestyle='--', linewidth=0.5)

# add a text
plt.text(1800, 50,"n = {: .5f}".format(n))
plt.text(1800, 40,"d = {: .2f}".format(d))


plt.savefig('P_factor.png')
plt.show()


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

ax2.set_xlim([-10, 10])
location = ['center', 'left', 'right']
myTitle = "Pressure"
ax2.set_title("\n".join(textwrap.wrap(myTitle, 80)), loc =location[0])
ax2.set_ylabel('Pressure, Pa')
ax2.set_xlabel('distance, mm')

dist = np.linspace(start=-50, stop = 50, num = len(L_00))

plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_00, 53, 4)))],
         n*np.array(scipy.signal.savgol_filter(L_00, 53, 4))+d,
         color = 'darkblue',
         label = "l = 0mm")
plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_10, 53, 4)))],
         n*np.array(scipy.signal.savgol_filter(L_10, 53, 4))+d,
         color = 'darkred',
         label = "l = 10mm")
plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_20, 53, 4)))],
         n*np.array(scipy.signal.savgol_filter(L_20, 53, 4))+d,
         color = 'darkgreen',
         label = "l = 20mm")
plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_30, 53, 4)))],
         n*np.array(scipy.signal.savgol_filter(L_30, 53, 4))+d,
         color = 'violet',
         label = "l = 30mm")
plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_40, 53, 4)))],
         n*np.array(scipy.signal.savgol_filter(L_40, 53, 4))+d,
         color = 'orange',
         label = "l = 40mm")
plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_50, 53, 4)))],
         n*np.array(scipy.signal.savgol_filter(L_50, 53, 4))+d,
         color = 'green',
         label = "l = 50mm")
plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_60, 53, 4)))],
         n*np.array(scipy.signal.savgol_filter(L_60, 53, 4))+d,
         color = 'darkgrey',
         label = "l = 60mm")
plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_70, 53, 4)))],
         n*np.array(scipy.signal.savgol_filter(L_70, 53, 4))+d,
         color = 'red',
         label = "l = 70mm")
ax2.legend()

plt.minorticks_on()
plt.grid(which='major', color='lightgrey', linestyle='-', linewidth=1)
plt.grid(which='minor', color='lightgrey', linestyle='--', linewidth=0.5)



plt.savefig('Pressure.png')
plt.show()




fig3 = plt.figure()
ax3 = fig3.add_subplot(111)

ax3.set_xlim([-10, 10])
location = ['center', 'left', 'right']
myTitle = "Velocity"
ax3.set_title("\n".join(textwrap.wrap(myTitle, 80)), loc =location[0])
ax3.set_ylabel('Velocity, m/s')
ax3.set_xlabel('distance, mm')

dist = np.linspace(start=-32, stop = 32, num = len(L_00))

ro = 1.2754

a1 = 2 * 1000 * np.pi * ro *scipy.integrate.trapz( abs(dist/1000) * ((2*abs(n*np.array(scipy.signal.savgol_filter(L_00, 53, 4))+d)/ro)**0.5),
        x = None, dx = (dist[1]-dist[0])/10000)
a2 = 2 * 1000 * np.pi * ro *scipy.integrate.trapz( abs(dist/1000) * ((2*abs(n*np.array(scipy.signal.savgol_filter(L_10, 53, 4))+d)/ro)**0.5),
        x = None, dx = (dist[1]-dist[0])/10000)
a3 = 2 * 1000 * np.pi * ro *scipy.integrate.trapz( abs(dist/1000) * ((2*abs(n*np.array(scipy.signal.savgol_filter(L_20, 53, 4))+d)/ro)**0.5),
        x = None, dx = (dist[1]-dist[0])/10000)
a4 = 2 * 1000 * np.pi * ro *scipy.integrate.trapz( abs(dist/1000) * ((2*abs(n*np.array(scipy.signal.savgol_filter(L_30, 53, 4))+d)/ro)**0.5),
        x = None, dx = (dist[1]-dist[0])/10000)

plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_00, 53, 4)))],
         (2*abs(n*np.array(scipy.signal.savgol_filter(L_00, 53, 4))+d)/ro)**0.5,
         color = 'darkblue',
         label =  "Q(0) = {: .2f}".format(a1))
plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_10, 53, 4)))],
         (2*abs(n*np.array(scipy.signal.savgol_filter(L_10, 53, 4))+d)/ro)**0.5,
         color = 'darkred',
         label =  "Q(10) = {: .2f}".format(a2))
plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_20, 53, 4)))],
         (2*abs(n*np.array(scipy.signal.savgol_filter(L_20, 53, 4))+d)/ro)**0.5,
         color = 'darkgreen',
         label =  "Q(20) = {: .2f}".format(a3))
plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_30, 53, 4)))],
         (2*abs(n*np.array(scipy.signal.savgol_filter(L_30, 53, 4))+d)/ro)**0.5,
         color = 'violet',
         label =  "Q(30) = {: .2f}".format(a4))
plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_40, 53, 4)))],
         (2*abs(n*np.array(scipy.signal.savgol_filter(L_40, 53, 4))+d)/ro)**0.5,
         color = 'orange')
plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_50, 53, 4)))],
         (2*abs(n*np.array(scipy.signal.savgol_filter(L_50, 53, 4))+d)/ro)**0.5,
         color = 'green')
plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_60, 53, 4)))],
         (2*abs(n*np.array(scipy.signal.savgol_filter(L_60, 53, 4))+d)/ro)**0.5,
         color = 'darkgrey')
plt.plot(dist-dist[np.argmax((scipy.signal.savgol_filter(L_70, 53, 4)))],
         (2*abs(n*np.array(scipy.signal.savgol_filter(L_70, 53, 4))+d)/ro)**0.5,
         color = 'red')

ax3.legend()

plt.minorticks_on()
plt.grid(which='major', color='lightgrey', linestyle='-', linewidth=1)
plt.grid(which='minor', color='lightgrey', linestyle='--', linewidth=0.5)


plt.savefig('Velocity.png')
plt.show()

