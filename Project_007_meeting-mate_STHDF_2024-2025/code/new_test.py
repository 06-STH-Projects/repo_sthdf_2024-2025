import belay

# Replace with your Pico's correct serial port
DEVICE_NAME = '/dev/tty.usbmodem113301'  # Change to your Pico's serial port

try:
    # Create a Device object to connect to the board
    device = belay.Device(DEVICE_NAME)
    print("Connected to Pico!")

    # Function to set the color of the NeoPixel ring
    @device.task()
    def set_led_color(color):
        import neopixel

        LED_PIN = Pin(0)  # GP0 pin for NeoPixel data line
        NUM_LEDS = 12  # Adjust according to the number of LEDs in your ring
        led_ring = neopixel.NeoPixel(LED_PIN, NUM_LEDS)

        # Fill the ring with the specified color
        if color == "red":
            led_ring.fill((255, 0, 0))  # Red
        elif color == "green":
            led_ring.fill((0, 255, 0))  # Green
        elif color == "blue":
            led_ring.fill((0, 0, 255))  # Blue
        else:
            print("Unknown color. Please use 'red', 'green', or 'blue'.")
            return
        led_ring.write()  # Update the LED ring

    # Command loop
    while True:
        command = input("Enter color (red/green/blue): ")
        if command in ["red", "green", "blue"]:
            set_led_color(command)  # Set the NeoPixel color based on input
        else:
            print("Unknown command. Please enter 'red', 'green', or 'blue'.")

except belay.ConnectionFailedError:
    print("Failed to connect to the Pico. Check the device name and try again.")
except Exception as e:
    print(f"An error occurred: {e}")
