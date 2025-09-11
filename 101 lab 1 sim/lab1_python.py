import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Style
plt.style.use('dark_background')

plt.rcParams.update({
    # Figure and axes
    'figure.facecolor':   '#1a2233',     # Very dark blue background
    'axes.facecolor':     '#1a2233',
    'axes.edgecolor':     '#86e1fc',     # Neon cyan for axes
    'axes.labelcolor':    '#c7e9fb',     # Pale cyan text
    'xtick.color':        '#c7e9fb',
    'ytick.color':        '#c7e9fb',
    'grid.color':         '#2a394f',
    'axes.titleweight':   'bold',
    'axes.labelweight':   'bold',

    # Lines and markers
    'lines.linewidth':    2.5,
    'lines.markersize':   7,

    # Font
    'font.size':          13,
    'axes.titlesize':     15,
    'axes.labelsize':     13,
})

# Data
percent_dye = np.array([10, 5, 1, 0.1])
reading1 = np.array([0.447, 0.243, 0.033, 0.045])
reading2 = np.array([0.450, 0.242, 0.04, 0.03])
reading3 = np.array([0.449, 0.238, 0.037, 0.035])

# Calculate mean and std dev at each % dye
readings = np.vstack([reading1, reading2, reading3])
mean_absorbace = readings.mean(axis=0) # mean absorbance
stddev_absorbance = readings.std(axis=0, ddof=1) # std dev absorbance

# Create plot
plt.scatter(percent_dye, reading1, label="Reading 1")
plt.scatter(percent_dye, reading2, label="Reading 2")
plt.scatter(percent_dye, reading3, label="Reading 3")


# Linear regression (fit to means)
X = percent_dye.reshape(-1, 1)
y = mean_absorbace
model = LinearRegression().fit(X, y)
y_prediction = model.predict(X)
plt.plot(percent_dye, y_prediction, color='black', label='Linear fit')

# R^2 annotation
r2 = r2_score(y, y_prediction)
plt.text(0.55 * percent_dye.max(), 0.9 * mean_absorbace.max(), f"R2 = {r2:.2f}", fontsize=12)

plt.xlabel("Percentage Concentration")
plt.ylabel("Absorbance at 422nm")
plt.legend()
plt.title("Dye concentration and absorbance at 422nm")
plt.tight_layout()

plt.show()