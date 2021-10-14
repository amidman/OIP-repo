import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

#init pins

LEDS = [21, 20, 16, 12, 7, 8, 25, 23]
DAC = [26, 19, 13, 6, 5, 11, 9, 10]
COMP = 4
troykaVoltage = 17

#init functions
#for adc
def binary():
    value = 0
    up = True
    for i in range(8):
        delta = 2 ** (7 - i)
        value = value + delta * (1 if up else -1)
        num2pins(DAC, value)
        time.sleep(0.0011)
        up = bool(GPIO.input(COMP))
    return value
#for show value in pins
def num2pins(pins, value):
    GPIO.output(pins, [int(i) for i in bin(value)[2:].zfill(8)])

#pins setting
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT)
GPIO.setup(LEDS, GPIO.OUT)
GPIO.setup(COMP, GPIO.IN)
GPIO.setup(troykaVoltage, GPIO.OUT)

#main
try:
    #declare values
    data = []
    value = 0
    start = time.time()
    
    #start charging
    GPIO.output(troykaVoltage, 1)
    
    while value < 245:
        value = binary()
        print(binary(),"Charge")
        num2pins(LEDS, value)
        data.append(value)

    #start discharging
    GPIO.output(troykaVoltage, 0)

    while value > 1:
        value = binary()
        print(binary(),"Discharge")
        num2pins(LEDS, value)
        data.append(value)

    #calculate some params
    finish = time.time()

    Total = finish - start
    Period = Total / len(data)
    samplingFrequency = int(1 / Period)

    #write data to file
    f = open("data.txt", 'w')
    for i in range(len(data)):
        f.write(str(data[i])+'\n')
    f.close()

    #write settinga to file
    f = open("settings.txt", 'w')
    f.write("Total Time: "+str(Total)+'\n')
    f.write("Period: "+str(Period)+'\n')
    f.write("Sampling Frequency: "+str(samplingFrequency)+'\n')
    f.close()

    #print params on screen
    print("Total Time: "+str(Total)+'\n')
    print("Period: "+str(Period)+'\n')
    print("Sampling Frequency: "+str(samplingFrequency)+'\n')

    #plot grafiki
    plt.plot(data)
    plt.show()

finally:
    #cleanup pins
    GPIO.cleanup()
    print('GPIO cleanup completed.')