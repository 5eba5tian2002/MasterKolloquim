import numpy as np
import matplotlib.pyplot as plt

# Zeitachse
t = np.linspace(0, 0.01, 1000)

# RC-Tiefpass Parameter
R = 1e3      # 1 kΩ
C = 1e-6     # 1 µF
tau = R * C  # Zeitkonstante

# Dirac-Impuls (approximiert als sehr kurzer Spike)
dirac = np.zeros_like(t)
dirac[0] = 1 / (t[1] - t[0])  # sehr hoher Wert auf einem Sample

# Impulsantwort eines RC-Tiefpasses: h(t) = (1/RC) * exp(-t/RC)
h = (1/tau) * np.exp(-t/tau)

# Plot
fig, axs = plt.subplots(1, 2, figsize=(8, 3))

# Dirac-Impuls
axs[0].plot(t, dirac, color='red')
axs[0].set_title("Dirac-Impuls (approximiert)")
axs[0].set_xlabel("Zeit [s]")
axs[0].set_ylabel("Amplitude")
axs[0].set_xlim(-0.0005, 0.002)

# Impulsantwort RC-Tiefpass
axs[1].plot(t, h, color='red')
axs[1].set_title("Impulsantwort eines RC-Tiefpasses")
axs[1].set_xlabel("Zeit [s]")
axs[1].set_ylabel("Amplitude")

plt.tight_layout()
plt.savefig("ImpulsantwortRC.png", dpi=300)