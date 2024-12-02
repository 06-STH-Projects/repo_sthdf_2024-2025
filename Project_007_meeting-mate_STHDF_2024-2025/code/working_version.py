import sounddevice as sd
import numpy as np
import logging
import time
import belay
import os
import sys


LOG_LEVEL = logging.INFO
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')


def get_raspbery_pico_conenction():
    try:
        # command for MAC systems
        usb_modem_devices = os.popen("ls /dev/tty.usbmodem*").read().split('\n')
        return usb_modem_devices[0]
    except IndexError:
        logging.error("No Pico device found. Please connect your Pico and try again.")
        return None

# Get the serial port of the Raspberry Pi Pico
DEVICE_NAME = get_raspbery_pico_conenction()


# Function to check microphone activity
def is_microphone_active(device_index):
    try:
        with sd.InputStream(device=device_index, channels=1, samplerate=44100) as stream:
            logging.debug("Monitoring microphone...")
            for _ in range(5):
                data = stream.read(1024)[0]
                if np.abs(data).mean() > 0:
                    logging.debug(f"Microphone {device_index} is actively capturing audio.")
                    return True
    except Exception as e:
        logging.error(f"Error while monitoring microphone {device_index}: {e}")
    logging.debug(f"Microphone {device_index} is not actively capturing audio.")
    return False


def list_microphones_and_check_if_active():
    devices = sd.query_devices()
    logging.debug("Available Input Devices (Microphones):")
    is_in_use = False

    for index, device in enumerate(devices):
        if device['max_input_channels'] > 0 and index == 3:
            logging.debug(f"{index}: {device['name']} (Input Channels: {device['max_input_channels']})")
            if is_microphone_active(index):
                logging.debug(f"Microphone {device['name']} is actively capturing audio.")
                is_in_use = True
            else:
                logging.debug(f"Microphone {device['name']} is not actively capturing audio.")
    return is_in_use


# Raspberry pi pico connection
if DEVICE_NAME:
    device = belay.Device(DEVICE_NAME)
    logging.info("Connected to Pico!")
else:
    print("Failed to connect to the Pico. Check the device name and try again.")
    logging.error("Failed to connect to the Pico. Check the device name and try again.")
    sys.exit(0)

# task to be executed on the pico
@device.task()
def set_led_color(mic_in_use):
    import neopixel

    LED_PIN = Pin(0)  # GP0 pin for NeoPixel data line
    NUM_LEDS = 12  # Adjust according to the number of LEDs in your ring
    led_ring = neopixel.NeoPixel(LED_PIN, NUM_LEDS)

    # Fill the ring with the specified color
    if mic_in_use:
        led_ring.fill((50, 0, 0))  # Red
    else:
        led_ring.fill((0, 50, 0))  # Green
    led_ring.write()  # Update the LED ring


while True:
    microphones_in_use = list_microphones_and_check_if_active()
    logging.info(f"Any microphone in use: {microphones_in_use}")

    set_led_color(microphones_in_use)

    time.sleep(2)  # Adjust as necessary
