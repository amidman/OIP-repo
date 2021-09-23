import RPi.GPIO as GPIO

AUX = 2

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(AUX, GPIO.OUT)

    p = GPIO.PWM(AUX, 1000)
    p.start(0)
    while True:
        dutycycle = input()
        if dutycycle == 'Q' or dutycycle == 'q':
            print("Exit")
            break
        try:
            dutycycle = int(dutycycle)
        except BaseException:
            print("Error")
        else:
            if (dutycycle >= 0) and (dutycycle <= 100):
                p.ChangeDutyCycle(dutycycle)
            else:
                print("Invalid value")
finally:
    p.stop()
    GPIO.cleanup()