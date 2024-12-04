import os
import sys
import logging
import tkinter as tk
from tkinter import ttk
import time
import belay
import threading
import AVFoundation
import CoreAudio
import struct
import re

from constants import RED, GREEN, BLACK

logging.basicConfig(level=logging.INFO)


def get_raspberry_pico_connection():
    try:
        usb_modem_devices = os.popen("ls /dev/tty.usbmodem*").read().split('\n')
        return usb_modem_devices[0]
    except IndexError:
        logging.error("No Pico device found. Please connect your Pico and try again.")
        return None


# Try to connect to Raspberry Pi Pico
DEVICE_NAME = get_raspberry_pico_connection()
if DEVICE_NAME:
    device = belay.Device(DEVICE_NAME)
    logging.info("Connected to meeting_mate!")
else:
    logging.error("Failed to connect to the Pico. Check the device name and try again.")
    sys.exit(0)


@device.task()
def set_led_color(color):
    import neopixel

    led_pin = Pin(0)  # GP0 pin for NeoPixel data line
    num_of_leds = 12  # Adjust according to the number of LEDs in your ring
    led_ring = neopixel.NeoPixel(led_pin, num_of_leds)

    # Fill the ring with the specified color
    led_ring.fill(color)
    led_ring.write()  # Update the LED ring


class MeetingMate:
    def __init__(self):
        self.monitoring = False
        self.selected_mic_index = None
        self.sound_devices = []
        self.mic_ids = {
            mic.connectionID(): mic
            for mic in AVFoundation.AVCaptureDevice.devicesWithMediaType_(
                AVFoundation.AVMediaTypeAudio
            )
        }

        self.opa = CoreAudio.AudioObjectPropertyAddress(
            CoreAudio.kAudioDevicePropertyDeviceIsRunningSomewhere,
            CoreAudio.kAudioObjectPropertyScopeGlobal,
            CoreAudio.kAudioObjectPropertyElementMaster
        )
        for mic_id in self.mic_ids:
            match = re.search(r"\[([^\]]+)\]\[", str(self.mic_ids[mic_id]))
            self.sound_devices.append({"id": mic_id, "name": match.group(1)})

    def start_monitoring(self):
        if self.selected_mic_index is None:
            logging.error("No microphone selected!")
            return
        self.monitoring = True
        logging.info("Starting monitoring...")
        thread = threading.Thread(target=self.monitor_microphone, daemon=True)
        thread.start()

    def stop_monitoring(self):
        self.monitoring = False
        time.sleep(1)
        set_led_color(color=BLACK)
        logging.info("Stopping monitoring...")

    def monitor_microphone(self):
        while self.monitoring:
            # Replace with actual logic to check microphone activity
            mic_in_use = self.check_microphone_activity()
            logging.info(f"Is microphone {self.sound_devices[self.selected_mic_index]['name']} in use: {mic_in_use}")
            if mic_in_use:
                set_led_color(color=RED)
            else:
                set_led_color(color=GREEN)
            time.sleep(2)

    def check_microphone_activity(self):
        try:
            response = CoreAudio.AudioObjectGetPropertyData(self.sound_devices[self.selected_mic_index]['id'],
                                                            self.opa, 0, [], 4, None)
            return bool(struct.unpack('I', response[2])[0])
        except Exception as e:
            logging.error(f"Error while monitoring microphone {self.selected_mic_index}: {e}")
        logging.debug(f"Microphone {self.selected_mic_index} is not actively capturing audio.")
        return False

    def run(self):
        set_led_color(color=BLACK)
        mic_names = [device["name"] for device in self.sound_devices]

        # GUI Setup
        root = tk.Tk()
        root.title("Meeting Mate")

        tk.Label(root, text="Select a microphone:").pack(pady=10)

        mic_selector = ttk.Combobox(root, values=mic_names, state="readonly")
        mic_selector.pack(pady=10)

        def select_microphone():
            try:
                self.selected_mic_index = mic_selector.current()
                logging.info(f"Selected Microphone Index: {self.selected_mic_index}")
            except ValueError:
                logging.error("Invalid microphone selection")

        mic_selector.bind("<<ComboboxSelected>>", lambda event: select_microphone())

        # Start and Stop Buttons
        tk.Button(root, text="Start Monitoring", command=self.start_monitoring).pack(pady=10)
        tk.Button(root, text="Stop Monitoring", command=self.stop_monitoring).pack(pady=10)

        # Status Label
        status_label = tk.Label(root, text="", font=("Arial", 12))
        status_label.pack(pady=20)

        def update_status():
            if self.monitoring:
                status_label.config(text="Monitoring is running", fg="green")
            else:
                status_label.config(text="Monitoring is stopped", fg="red")
            root.after(500, update_status)
        update_status()

        # Run the GUI event loop
        root.mainloop()
