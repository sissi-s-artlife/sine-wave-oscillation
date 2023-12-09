import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the time range
t = np.linspace(0, 10, 1000)  # Time from 0 to 10 seconds

# Define the frequency and amplitude of the sine wave
frequency = 1  # Oscillation frequency (1 cycle per second)
amplitude = 1  # Amplitude of the wave

# Create a figure and axis
fig, ax = plt.subplots()
line, = ax.plot(t, amplitude * np.sin(2 * np.pi * frequency * t))

# Function to update the plot in each frame of the animation
def update(frame):
    phase_increment = 0.1 * (frame % 20)  # Vary the phase increment for back-and-forth motion
    line.set_ydata(amplitude * np.sin(2 * np.pi * frequency * t + phase_increment))
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sine Wave Oscillation Animation')
plt.grid(True)
plt.show()

