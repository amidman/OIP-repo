import numpy as np
import matplotlib.pyplot as plt

data = []
TotalTime = 0
Period = 0
SampFreaq = 0


dataF = open('data.txt', 'r')
settingsF = open('settings.txt', 'r')

while True:
    line = dataF.readline()
    if not line:
        break
    else:
        data.append(float(line)*3.3/255)
dataF.close()

TotalTime = float(settingsF.readline())
Period = float(settingsF.readline())
SampFreaq = float(settingsF.readline())
settingsF.close()

markX = np.linspace(0,len(data), num = 20, endpoint=False).astype(int)
markers = []
for i in markX:
    markers.append(data[i])

tCh = np.argmax(data)*Period
tDis = TotalTime-tCh
print(tCh)
print(tDis)

t = np.linspace(0, TotalTime, num = len(data))

fig, ax = plt.subplots()

ax.plot(t, data, color = 'blue', lw = 0.5)
ax.plot(markX/len(data)*TotalTime, markers, 'o-', color = 'blue', linestyle = ' ', label = 'V(t)')

#plt.axis([0, 10, 0, 10])
ax.minorticks_on()
plt.grid(which='major', axis = 'both', linewidth = 1.0)
plt.grid(which='minor', axis = 'both', linewidth = 0.5)

plt.text(50,2,'Время зарядки '+f'{tCh:.2f}')
plt.text(50,1.5,'Время разрядки '+f'{tDis:.2f}')

ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение, В')
ax.set_title('Процесс заряда и разряда конденсатора в RC цепочке', wrap = True)
ax.legend(loc = 'upper right')
fig.tight_layout()

plt.show()