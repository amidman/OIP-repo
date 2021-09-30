import RPi.GPIO as GPIO
import time

DAC = [26, 19, 13, 6, 5, 11, 9, 10]
COMP = 4

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def dec2dac(value):
    bin = decimal2binary(value)
    for i in range(8):
        GPIO.output(DAC[i],bin[i])

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT)
GPIO.setup(COMP, GPIO.IN)

while True:
    for i in range(255):
        dec2dac(i)
        if(GPIO.input(COMP)):
            print(i)
            break
        #time.sleep(0.1)