#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Turns ON and OFF a single RGB LED with many colors and interval of 1.5 seconds.
'''
import RPi.GPIO as GPIO
import time
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

def magic():
  for pin_id in RGBS:
      gpiocontrol(pin_id, 1)
      time.sleep(1.5)
      gpiocontrol(pin_id, 0)

# This function will run if the file is executed directly
def main():
  setup()
  magic()
  clear()
  # Release GPIO
  GPIO.cleanup()

if __name__=='__main__':
  main()
