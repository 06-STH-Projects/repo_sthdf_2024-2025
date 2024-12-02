import sounddevice as sd
import numpy as np
import logging
import time
import belay

# Replace with your Pico's correct serial port
# /dev/tty.usbmodem1132401
# /dev/tty.usbmodem113301


import os

# Run the command to list tty devices and split by new lines
tty_devices = os.popen('ls /dev/tty.*').read().split('\n')

# Filter for device containing '/dev/tty.usbmodem'
usbmodem_devices = [device for device in tty_devices if 'tty.usbmodem' in device]

print(usbmodem_devices)

