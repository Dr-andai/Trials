import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd

#infertility data
data = {
    'year'  : [1989, 1993, 1998, 2003, 2009, 2014, 2015, 2020, 2022],
    'rural' : [7.1, 5.8, 5.2, 5.4, 5.2, 4.5, 4.5, 3.6, 3.9],
    'total' : [6.7, 5.4, 4.7, 4.9, 4.6, 3.9, 3.7, 3.3, 3.4],
    'urban' : [4.5, 3.4, 3.1, 3.3, 2.9, 3.1, 2.8, 2.7, 2.8]
}
df = pd.DataFrame(data)

# create initial plot
fig, ax = plt.subplots()
plt.title('TFR for the 3 years before each survey')

#lines = [ax.plot([], [], marker= 's', lw=1)[0] for _ in range(3)]
lines = [
    ax.plot([], [], lw=1, marker='o')[0],  # 'o' marker for rural
    ax.plot([], [], lw=1, marker='s')[0],  # 's' marker for total
    ax.plot([], [], lw=1, marker='^')[0]   # '^' marker for urban
]
ax.set_xlim(1985, 2023)
ax.set_ylim(0, 8)

ax.legend(['rural', 'total', 'urban'])

# Define custom tick formatter for the x-axis
from matplotlib.ticker import FuncFormatter

def year_formatter(x, pos):
    return str(int(x))

ax.xaxis.set_major_formatter(FuncFormatter(year_formatter))

# Define the initialization function and animation update function
def init():
    for line in lines:
        line.set_data([], [])
    return lines 

def animate(i):
    for j, line in enumerate(lines):
        x = df['year'][:i+1]
        y = df.iloc[:i+1, j+1]  # Select the j-th column for total values
        line.set_data(x, y)

        # Add annotations for each data point with y-axis value
        y_annotation = y.iloc[-1]
        annotation_text = f'{y_annotation:.1f}' # to one decimal point
        ax.annotate(annotation_text, (x.iloc[-1], y_annotation), textcoords="offset points", xytext=(0,10), ha='center')

    return lines

# Create the animation using FuncAnimation
ani = FuncAnimation(fig, animate, init_func=init, frames=len(df), repeat=False, blit=False)


# Display the animation
#plt.show()
plt.close()

from matplotlib.animation import PillowWriter
 #Save the animation as an animated GIF
ani.save("lines_04_animation.gif", dpi=300,
           writer=PillowWriter(fps=1))

