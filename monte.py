# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Sample data initialization
# parameter_values = np.linspace(0, 1, 100)
# data = np.random.rand(100, 50)  # 100 data points, each with 50 time steps

# # Create a figure and axis for the animation
# fig, ax = plt.subplots(figsize=(8, 6))
# line, = ax.plot(parameter_values, data[:, 0], label='Sample Data')
# ax.set_xlabel('Parameter Values')
# ax.set_ylabel('Outcomes')
# ax.set_title('Game Analysis Results')
# ax.legend()
# ax.grid(True)

# # Animation update function
# def update(frame):
#     line.set_ydata(data[:, frame])  # Update the y-data (outcomes) for the line plot
#     return line,

# # Create the animation
# num_frames = data.shape[1]
# ani = FuncAnimation(fig, update, frames=num_frames, repeat=False)

# # To display the animation in Jupyter Notebook, you can use the following line:
# # from IPython.display import HTML
# # HTML(ani.to_jshtml())

# # To save the animation as an animated GIF (you may need to install 'pillow' package):
# # ani.save('game_analysis_animation.gif', writer='pillow', fps=10)

# # To display the animation in a standalone window:
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Sample data initialization
theta = np.linspace(0, 2 * np.pi, 100)
data = np.random.rand(100, 50)  # 100 data points, each with 50 time steps

# Create a figure and axis for the animation with polar projection
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 6))

# Initialize the polar line plot
line, = ax.plot(theta, data[:, 0], label='Sample Data')

# Set the radial axis label
ax.set_rlabel_position(90)
ax.set_rticks([])  # Hide radial ticks
ax.set_xlabel('Parameter Values')
ax.set_title('Polar Plot of Game Analysis Results')

# Animation update function
def update(frame):
    line.set_ydata(data[:, frame])  # Update the y-data (outcomes) for the polar plot
    return line,

# Create the animation
num_frames = data.shape[1]
ani = FuncAnimation(fig, update, frames=num_frames, repeat=False)

# To display the animation in Jupyter Notebook, you can use the following line:
# from IPython.display import HTML
# HTML(ani.to_jshtml())

# To save the animation as an animated GIF (you may need to install 'pillow' package):
# ani.save('polar_game_analysis_animation.gif', writer='pillow', fps=10)

# To display the animation in a standalone window:
plt.show()
