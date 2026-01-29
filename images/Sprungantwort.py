import numpy as np
import matplotlib.pyplot as plt

# Zeitachse
t = np.linspace(0, 0.01, 1000)

# RC-Tiefpass Parameter
R = 1e3      # 1 kΩ
C = 1e-6     # 1 µF
tau = R * C  # Zeitkonstante

# Eingangssprung (von 0 auf 1)
#step = np.ones_like(t)

T_r = 0.0005  # Anstiegszeit 0.5 ms
step = np.clip(t / T_r, 0, 1)


# Sprungantwort eines RC-Tiefpasses: y(t) = 1 - exp(-t/RC)
y = 1 - np.exp(-t/tau)

# Plot
fig, axs = plt.subplots(1, 2, figsize=(8, 3))

# Eingangssprung
axs[0].plot(t, step, color='blue')
axs[0].set_title("Eingangssprung")
axs[0].set_xlabel("Zeit [s]")
axs[0].set_ylabel("Amplitude")
axs[0].set_ylim(-0.1, 1.2)

# Sprungantwort RC-Tiefpass
axs[1].plot(t, y, color='blue')
axs[1].set_title("Sprungantwort eines RC-Tiefpasses")
axs[1].set_xlabel("Zeit [s]")
axs[1].set_ylabel("Amplitude")
axs[1].set_ylim(-0.1, 1.2)

plt.tight_layout()
plt.savefig("SprungantwortRC.png", dpi=300)
plt.show()