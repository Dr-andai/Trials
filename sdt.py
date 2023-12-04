import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

signal_present = np.random.rand(1000) > .5

sns.heatmap(signal_present.reshape(25, 40), linewidths=0, xticklabels=False, yticklabels=False);