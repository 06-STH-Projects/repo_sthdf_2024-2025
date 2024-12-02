import sounddevice as sd
import numpy as np

# Audio parameters
SAMPLE_RATE = 44100  # Sample rate in Hz
BLOCK_SIZE = 2048     # Number of audio samples per block
THRESHOLD = 0.01      # Threshold for detecting sound (adjust as necessary)

def audio_callback(indata, outdata, frames, time, status):
    """Callback function to process audio input and output."""
    if status:
        print(status)

    # Calculate the RMS (Root Mean Square) to measure audio intensity
    rms = np.sqrt(np.mean(np.square(indata)))

    # Check if the microphone is active
    microphone_active = rms > THRESHOLD

    # Output the current microphone status
    if microphone_active:
        print("Microphone is active! RMS level:", rms)
    else:
        print("Microphone is inactive. RMS level:", rms)

    # Pass the input audio to the output
    outdata[:] = indata

try:
    print("Starting virtual sound card...")
    with sd.Stream(callback=audio_callback,
                   samplerate=SAMPLE_RATE,
                   blocksize=BLOCK_SIZE,
                   channels=1):  # Mono audio
        print("Press Ctrl+C to stop.")
        while True:
            sd.sleep(1000)  # Sleep to keep the stream alive
except KeyboardInterrupt:
    print("\nStopping virtual sound card...")
except Exception as e:
    print(f"Error: {e}")
finally:
    sd.stop()
