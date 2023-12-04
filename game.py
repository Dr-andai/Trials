# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm

# # Settings
# mu = 0           # Mean under H0
# sigma = 1        # Standard deviation
# alpha = 0.05     # Significance level

# # Set up the figure
# plt.figure(figsize=(10, 6))

# # Generate values for the x-axis (from -3*sigma to 3*sigma)
# x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)

# # Plot the normal distribution
# plt.plot(x, norm.pdf(x, mu, sigma), label='Null Hypothesis ($H_0$)')

# # Calculate critical value for one-tailed test
# critical_value = norm.ppf(1 - alpha, mu, sigma)

# # Fill area under curve for Type I error
# x_fill = np.linspace(critical_value, mu + 3*sigma, 1000)
# y_fill = norm.pdf(x_fill, mu, sigma)
# plt.fill_between(x_fill, y_fill, color='red', alpha=0.5, label='Type I Error Area (α)')

# # Add critical value line
# plt.axvline(x=critical_value, color='grey', linestyle='dashed', label=f'Critical Value (z={critical_value:.2f})')

# # Add labels and legend
# plt.xlabel('Values of Test Statistic')
# plt.ylabel('Probability Density')
# plt.title(f'Visualization of Type I Error (α = {alpha})')
# plt.legend()

# # Show plot
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Function to calculate O'Brien-Fleming boundary
def obrien_fleming(alpha, analysis):
    return norm.ppf(1 - alpha / 2 / (analysis ** 2))

# Function to calculate Pocock boundary
def pocock(alpha, num_analyses):
    return norm.ppf(1 - alpha / 2 / num_analyses)

# Parameters
num_analyses = 4  # Number of interim analyses
alpha = 0.05      # Overall Type I error rate

# Calculate boundaries
obf_boundaries = [obrien_fleming(alpha, i) for i in range(1, num_analyses + 1)]
pocock_boundaries = [pocock(alpha, num_analyses)] * num_analyses

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_analyses + 1), obf_boundaries, marker='o', linestyle='-', color='blue', label='O’Brien-Fleming')
plt.plot(range(1, num_analyses + 1), pocock_boundaries, marker='o', linestyle='-', color='green', label='Pocock')
plt.xticks(range(1, num_analyses + 1))
plt.xlabel('Interim Analysis Number')
plt.ylabel('Z-score Boundary')
plt.title('Comparison of O’Brien-Fleming and Pocock Boundaries')
plt.legend()
plt.grid(True)
plt.show()
