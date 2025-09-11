import numpy as np
import matplotlib.pyplot as plt

# ---- curve definition -------------------------------------------------
v_inf = 40        # terminal velocity  (m s^-1)
k     = 0.18      # rate constant     (s^-1)

t = np.linspace(0, 20, 400)
v = v_inf * (1 - np.exp(-k * t))     # analytical curve

# ---- tangent calculation ----------------------------------------------
t0 = 6.0                              # point where you want the tangent
v0 = v_inf * (1 - np.exp(-k * t0))    # point on the curve
m  = k * v_inf * np.exp(-k * t0)      # dv/dt at t0  -> slope of tangent
tangent = v0 + m * (t - t0)           # line eqn: y = v0 + m (t - t0)

# ---- plotting ----------------------------------------------------------
plt.plot(t, v, "k", label="v(t)")
plt.plot(t, tangent, "r--",
         label=f"tangent @ {t0:.1f} s (slope {m:.2f} m/s²)")
plt.scatter([t0], [v0], color="red", zorder=3)  # highlight the point
plt.xlim(0, 20); plt.ylim(0, 40)
plt.xlabel("Time t (s)"); plt.ylabel("Velocity v (m s⁻¹)")
plt.grid(True, linestyle=":", linewidth=0.5); plt.legend(); plt.tight_layout()
plt.show()
