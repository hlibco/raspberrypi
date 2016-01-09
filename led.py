import RPi.GPIO as GPIO
import time

print GPIO.VERSION

GPIO.setmode(GPIO.BOARD)


GPIO.setup(26, GPIO.OUT)

switch = False

delays = [1,2,3,4,5]
for delay in delays:
  switch = not switch
  GPIO.output(26, switch)
  time.sleep(delay)

GPIO.cleanup()
