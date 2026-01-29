import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# RC-Parameter
R = 1e3      # 1 kΩ
C = 1e-6     # 1 µF
tau = R * C  # Zeitkonstante

# Grenzfrequenz
wc = 1 / (R * C)

# Übertragungsfunktion H(s) = 1 / (1 + sRC)
num = [1]
den = [R*C, 1]
system = signal.TransferFunction(num, den)

# Frequenzbereich (logarithmisch)
w = np.logspace(1, 6, 1000)  # 10 Hz bis 1 MHz
w, mag, phase = signal.bode(system, w=w)

# Plot
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Betragsgang
axs[0].semilogx(w, mag, color='blue')
axs[0].axvline(wc, color='black', linestyle='--', linewidth=1)
axs[0].plot(wc, -3, 'ko')  # -3 dB Punkt
axs[0].text(wc, -3, "  ωg = -3dB", verticalalignment='bottom')
axs[0].set_title("Bode-Diagramm eines RC-Tiefpasses (1. Ordnung)")
axs[0].set_ylabel("Betrag [dB]")
axs[0].grid(True, which="both", ls="--")

# Phasengang
axs[1].semilogx(w, phase, color='red')
axs[1].axvline(wc, color='black', linestyle='--', linewidth=1)
axs[1].plot(wc, -45, 'ko')  # -45° Punkt
axs[1].text(wc, -45, "  -45° bei ωg", verticalalignment='bottom')
axs[1].set_xlabel("Frequenz [rad/s]")
axs[1].set_ylabel("Phase [°]")
axs[1].grid(True, which="both", ls="--")

plt.tight_layout()
plt.savefig("BodediagrammRC_markiert.png", dpi=300)
plt.show()