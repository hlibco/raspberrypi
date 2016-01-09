#!/usr/bin/python
import RPi.GPIO as GPIO
import time
print GPIO.VERSION

# LED CONFIG - Set GPIO Ports
LED_1 = 26

# LED Pool
LEDS = [LED_1]

def setup():
  # Set up the wiring
  GPIO.setmode(GPIO.BOARD)
  # Setup Ports
  for led_id in LEDS:
    GPIO.setup(led_id, GPIO.OUT)

def clear():
  for led_id in LEDS:
    GPIO.output(led_id, 0)

def magic():
  switch = False
  delays = [1,2,3,4,5]

  for delay in delays:
      switch = not switch
      GPIO.output(LED1, switch)
      time.sleep(delay)

def main():
  setup()
  clear()
  magic()
  clear()
  GPIO.cleanup()
