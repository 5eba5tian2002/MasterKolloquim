import numpy as np
import matplotlib.pyplot as plt

# RC-Parameter
R = 1.0
C = 1.0
tau = R * C

# Zeitachse
t_max = 10 * tau
N = 4000
t = np.linspace(0, t_max, N)
dt = t[1] - t[0]

# Impulsantwort h(t)
h = (1/tau) * np.exp(-t/tau)

# Eingangssignal: Sinus
f = 1.0  # Frequenz in Hz
omega = 2 * np.pi * f
x = np.sin(omega * t)

# Numerische Faltung
y = np.convolve(x, h, mode='full')[:N] * dt

# Plot
plt.figure(figsize=(8, 5))
plt.plot(t, x, label="Eingang x(t) = sin(ωt)")
plt.plot(t, y, label="Ausgang y(t) = x * h")
plt.xlabel("Zeit t")
plt.ylabel("Amplitude")
plt.title("Faltung eines RC-Tiefpasses mit einem Sinus-Eingang")
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()