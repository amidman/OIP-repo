import RPi.GPIO as GPIO
import time

DAC = [26, 19, 13, 6, 5, 11, 9, 10]
LEDS = [21,20,16,12,7,8,25,24]
COMP = 4
TROYKA = 17

def binary():
    bin = [0,0,0,0,0,0,0,0]
    for i in range(8):
        bin[i] = 1
        for j in range(8):
            GPIO.output(DAC[j],bin[j])
        time.sleep(0.01)
        if(not GPIO.input(COMP)):
            bin[i] = 0
    s = ''
    for i in range(8):
        s = s + str(bin[i])
    return s

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT)
GPIO.setup(LEDS, GPIO.OUT)
GPIO.setup(COMP, GPIO.IN)


while True:
    val = (int(binary(), 2))
    print(val)
    val = int(val/64*8)
    print(val)
    for i in range(8):
        if i < val:
            GPIO.output(LEDS[i],1)
        else:
            GPIO.output(LEDS[i],0)