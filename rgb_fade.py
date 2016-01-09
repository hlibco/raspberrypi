#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Turns ON and OFF a single RGB LED with many colors and interval of 1.5 seconds.
'''
import RPi.GPIO as GPIO
import time
import math
print GPIO.VERSION

# RGB CONFIG - Set GPIO Ports
RGB_RED = 11
RGB_BLUE = 15
RGB_GREEN = 13
RGB_CYAN = [RGB_GREEN, RGB_BLUE]
RGB_WHITE = [RGB_RED, RGB_GREEN, RGB_BLUE]
RGB_YELLOW = [RGB_RED, RGB_GREEN]
RGB_MAGENTA = [RGB_RED, RGB_BLUE]

# Available colors
RGBS = [RGB_RED, RGB_GREEN, RGB_BLUE,
        RGB_CYAN, RGB_WHITE, RGB_YELLOW, RGB_MAGENTA]

# Frequency
FREQ = 100

# Set up colors using PWM so we can control individual brightness
RED = GPIO.PWM(RGB_RED, FREQ)
BLUE = GPIO.PWM(RGB_BLUE, FREQ)
GREEN = GPIO.PWM(RGB_GREEN, FREQ)
RED.start(0)
BLUE.start(0)
GREEN.start(0)

def setup():
  # Set up the wiring
  GPIO.setmode(GPIO.BOARD)
  # Setup Ports
  for pin_id in RGB_WHITE:
    GPIO.setup(pin_id, GPIO.OUT)
  clear()

# Reset pins to default state
def clear():
  gpiocontrol(RGB_WHITE, 0)

def cleanup():
  clear()

  # Stop all the PWM objects
  RED.stop()
  GREEN.stop()
  BLUE.stop()

  # Release GPIO
  GPIO.cleanup()

# Control the state of a single or multiple pins in a list
def gpiocontrol(pins, state):
  # Determine if "pins" is a single integer or not
  if isinstance(pins, int):
    # Single integer - reference directly
    GPIO.output(pins, state)
  else:
    # If not, then cycle through the "pins" list
    for i in pins:
      GPIO.output(i, state)

def colour(R, G, B, delay):
  # Colour brightness range is 0-100
  RED.ChangeDutyCycle(R)
  GREEN.ChangeDutyCycle(G)
  BLUE.ChangeDutyCycle(B)
  time.sleep(delay)

  # Turn everything off
  RED.ChangeDutyCycle(0)
  GREEN.ChangeDutyCycle(0)
  BLUE.ChangeDutyCycle(0)

def PosSinWave(amplitude, angle, frequency):
  # Angle in degrees
  # Creates a positive sin wave between 0 and amplitude*2
  return amplitude + (amplitude * math.sin(math.radians(angle)*frequency) )

# This function will run if the file is executed directly
def main():
  setup()

  try:
    while 1:
      for i in range(0, 720, 5):
        colour(PosSinWave(50, i, 0.5),
               PosSinWave(50, i, 1),
               PosSinWave(50, i, 2),
               0.1)
  except KeyboardInterrupt:
    pass

  cleanup()

if __name__=='__main__':
  main()
