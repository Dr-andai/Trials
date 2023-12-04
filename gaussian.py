import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Create random data for initial "Difference in percentage healed" values
np.random.seed(0)
initial_difference_percentage_healed = np.random.randint(-40, 61, 100)

# Define the number of frames and the data update function
num_frames = 100
frame_interval = 100  # Milliseconds between frames

def update(frame):
    ax.clear()
    
    # Simulate changes in the "Difference in percentage healed" values
    difference_percentage_healed = initial_difference_percentage_healed + (frame - num_frames / 2)
    
    # Plot the horizontal line at difference = 20
    ax.axhline(y=20, color='black', linestyle='--', label='Difference = 20')

    # Plot vertical lines with points for each study
    for study_number, diff in enumerate(difference_percentage_healed, start=1):
        marker = 'o' if diff >= 20 else 'x'
        color = 'green' if diff >= 20 else 'red'
        ax.plot([study_number, study_number], [diff, diff], color=color, marker=marker, markersize=6)

    # Identify studies with open diamond symbols
    open_diamond_studies = [7, 14, 27, 48, 62, 89]  # Replace with the actual studies that should have open diamonds
    for study_number in open_diamond_studies:
        diff = difference_percentage_healed[study_number - 1]
        ax.plot(study_number, diff, 'D', markerfacecolor='none', markeredgecolor='blue', markersize=6)

    # Set labels and ticks
    ax.set_xlabel('Study number')
    ax.set_ylabel('Difference in percentage healed')
    ax.set_xticks(np.arange(0, 101, 10))
    ax.set_yticks(np.arange(-40, 61, 20))

    # Add a legend
    ax.legend(loc='upper right')

    # Set the title
    ax.set_title(f'Vertical Forest Plot (Frame {frame})')

    # Add a grid
    ax.grid(True)

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=frame_interval, repeat=False)

# Show the animated plot
plt.show()
