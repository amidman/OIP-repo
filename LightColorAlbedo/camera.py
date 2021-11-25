from picamera import PiCamera
import time

camera = PiCamera()

camera.start_preview ()
time.sleep(5)
camera.capture("green.jpeg")
camera.stop_preview()