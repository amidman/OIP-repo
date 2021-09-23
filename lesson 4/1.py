import RPi.GPIO as GPIO

DAC = [26, 19, 13, 6, 5, 11, 9, 10]

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def dec2dac(value):
    bin = decimal2binary(value)
    for i in range(8):
        GPIO.output(DAC[i],bin[i])

try:
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(DAC, GPIO.OUT)
    while True:
        value = input()
        if value == 'Q' or value == 'q':
            print("Exit")
            break
        try:
            value = int(value)
        except BaseException:
            print("Error")
        else:
            if (value >= 0) and (value <= 255):
                dec2dac(value)
            else:
                print("Invalid value")
finally:
    GPIO.cleanup()