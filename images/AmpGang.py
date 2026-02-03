import numpy as np
import matplotlib.pyplot as plt

# Parameter des RC-Tiefpasses
R = 1e3        # 1 kΩ
C = 100e-9     # 100 nF

# Grenzfrequenz
fc = 1 / (2 * np.pi * R * C)

# Frequenzachse (logarithmisch)
f = np.logspace(1, 6, 1000)  # 10 Hz bis 1 MHz
w = 2 * np.pi * f

# Frequenzgang H(jw) = 1 / (1 + j w RC)
H = 1 / (1 + 1j * w * R * C)

# Amplitudengang in dB
H_dB = 20 * np.log10(np.abs(H))

# Plot
plt.figure(figsize=(8, 5))
plt.semilogx(f, H_dB, label="|H(jω)|")
plt.axvline(fc, color='red', linestyle='--', label=f"fg")

plt.title("Amplitudengang eines RC-Tiefpasses")
plt.xlabel("Frequenz [Hz]")
plt.ylabel("Amplitude [dB]")
plt.grid(True, which="both", ls=":")
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig("AmplitudenGang.png", dpi=300)