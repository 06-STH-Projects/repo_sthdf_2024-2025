import machine
import neopixel
import time

# Configure the pin for the LED ring's data line
LED_PIN = machine.Pin(0)  # GP0 pin, change if connected to a different pin

# Define the number of LEDs in the ring
NUM_LEDS = 12  # Adjust according to the number of LEDs in your ring

# Create a NeoPixel object
led_ring = neopixel.NeoPixel(LED_PIN, NUM_LEDS)

# Function to turn on LEDs with different colors
def cycle_colors():
    for i in range(NUM_LEDS):
        led_ring[i] = (255, 0, 0)  # Red
        led_ring.write()
        time.sleep(0.1)
        led_ring[i] = (0, 255, 0)  # Green
        led_ring.write()
        time.sleep(0.1)
        led_ring[i] = (0, 0, 255)  # Blue
        led_ring.write()
        time.sleep(0.1)
        led_ring[i] = (0, 0, 0)

# Turn off all LEDs
led_ring.fill((0, 0, 0))
led_ring.write()

# Cycle through colors
while True:
    cycle_colors()


