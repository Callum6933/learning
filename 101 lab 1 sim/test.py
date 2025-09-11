import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')
plt.rcParams.update({
    'figure.facecolor': '#1a2233',
    'axes.facecolor':   '#1a2233',
    'axes.edgecolor':   '#86e1fc',
    'axes.labelcolor':  '#c7e9fb',
    'xtick.color':      '#c7e9fb',
    'ytick.color':      '#c7e9fb',
    'grid.color':       '#2a394f',
    'font.size':        13,
    'axes.titlesize':   15,
    'axes.labelsize':   13,
    'lines.linewidth':  2.5,
    'lines.markersize': 7,
})

x = np.linspace(0, 10, 25)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, color='#00fff7', marker='o', label='Sin(x)')
plt.plot(x, y2, color='#39ff14', marker='o', label='Cos(x)')

plt.fill_between(x, y1, y2, color='#00fff7', alpha=0.22)  # translucent fill for glow
plt.fill_between(x, y2, y1, color='#39ff14', alpha=0.22)

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.tight_layout()
plt.show()