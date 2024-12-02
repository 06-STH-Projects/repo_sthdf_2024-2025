import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

time.sleep(2)  # Wait for the device to be recognized by the PC

# Simulate Win + R to open Run dialog on Windows
kbd.press(Keycode.WINDOWS, Keycode.R)
kbd.release_all()

time.sleep(0.5)  # Small delay before typing

# Type the name of the program (e.g., "notepad") and press Enter
kbd.write("notepad")
kbd.press(Keycode.ENTER)
kbd.release_all()


# basically make the pico a keyboard to run an app
