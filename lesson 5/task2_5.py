import RPi.GPIO as GPIO
import time

DAC = [26, 19, 13, 6, 5, 11, 9, 10]
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
    print(bin)
    time.sleep(0.1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT)

GPIO.setup(COMP, GPIO.IN)



while True:
    binary()