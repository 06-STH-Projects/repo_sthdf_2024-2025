import pyaudio
import numpy as np
import librosa
import librosa.display
import pygame
from pygame.locals import QUIT
from collections import deque

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (160, 130, 240)

# Mapping frequency to y-coordinate
def frequency_to_y(frequency):
    """Convert a frequency in Hz to a y-coordinate on the sheet."""
    if frequency <= 0:
        return None
    A4 = 440.0  # Reference pitch
    y = WINDOW_HEIGHT // 2 - int(70 * np.log2(frequency / A4)) + 20
    return max(0, min(WINDOW_HEIGHT, y))

pitch_window = deque(maxlen=5)  # Stores the last 5 pitch values

def smooth_pitch(pitch):
    pitch_window.append(pitch)
    return np.mean(pitch_window)

pyaudio_format = pyaudio.paInt16
channels = 1
rate = 44100
buffer_size = 4096

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio_format,
                channels=channels,
                rate=rate,
                input=True,
                frames_per_buffer=buffer_size)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Real-time audio visualization")
clock = pygame.time.Clock()

# Main loop
running = True
line_points = []  # Store points for the visualized line
last_pitch = None
pitch_tolerance = 5.0  # Hz tolerance for detecting pitch changes
magnitude_threshold = 0.1  # Minimum magnitude to consider a pitch valid

try:
    while running:
        # Get audio data
        audio_data = stream.read(buffer_size, exception_on_overflow=False)
        samples = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32)

        # Estimate pitch using librosa
        try:
            # pitches, magnitudes = librosa.piptrack(y=samples, sr=rate, fmin=85.0, fmax=1100.0)
            # pitch = 0
            # if pitches.any():
            pitches, magnitudes = librosa.piptrack(y=samples, sr=rate, fmin=85.0, fmax=1100.0)
            pitch_idx = magnitudes.argmax(axis=0)
            pitch = pitches[pitch_idx, np.arange(pitches.shape[1])].mean()  # Average pitch
            magnitude = magnitudes.max()
        except Exception as e:
            pitch = 0
            magnitude = 0

        # Valid pitch
        # if pitch > 0:
        if pitch > 0 and magnitude > magnitude_threshold:
            pitch = smooth_pitch(pitch)
            y = frequency_to_y(pitch)
            if y is not None:
                # Scroll points left
                line_points = [(x - 5, y_coord) for x, y_coord in line_points if x - 5 > 0]

                # Add a new point or extend the last point
                if last_pitch is None or abs(pitch - last_pitch) > pitch_tolerance:
                    line_points.append((WINDOW_WIDTH, y))
                elif line_points:
                    line_points[-1] = (WINDOW_WIDTH, line_points[-1][1])

        last_pitch = pitch

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Draw the blank sheet music
        screen.fill(WHITE)
        for i in range(5):
            pygame.draw.line(screen, BLACK, (0, 100 + i * 40), (WINDOW_WIDTH, 100 + i * 40), 2)

        # Draw the visualization line
        if len(line_points) >= 2:
            pygame.draw.lines(screen, PURPLE, False, line_points, 3)

        pygame.display.flip()
        clock.tick(30)

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
    pygame.quit()