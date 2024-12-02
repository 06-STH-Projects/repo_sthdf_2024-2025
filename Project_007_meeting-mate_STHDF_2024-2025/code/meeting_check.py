import pyaudio
import numpy as np
import time

# Parameters for audio input
CHUNK = 2048  # Number of audio samples per frame
RATE = 44100  # Sampling rate (samples per second)
THRESHOLD = 500  # Threshold for detecting sound (adjust as necessary)

# Initialize PyAudio
audio = pyaudio.PyAudio()

try:
    # Open a stream to the default microphone
    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Monitoring microphone usage... Press Ctrl+C to stop.")

    while True:
        # Read audio data from the stream
        data = stream.read(CHUNK, exception_on_overflow=False)

        # Convert the byte data to numpy array
        audio_data = np.frombuffer(data, dtype=np.int16)

        # Calculate the RMS (Root Mean Square) to measure audio intensity
        rms = np.sqrt(np.mean(np.square(audio_data)))

        # Check if the microphone is active
        if rms > THRESHOLD:
            print("Microphone is active! Sound level (RMS):", rms)
        else:
            print("Microphone is inactive. Sound level (RMS):", rms)

        time.sleep(0.5)  # Add a short delay to avoid flooding output

except KeyboardInterrupt:
    print("\nTerminating microphone monitoring...")

finally:
    # Stop the stream and terminate the audio interface
    if stream.is_active():
        stream.stop_stream()
    stream.close()
    audio.terminate()
