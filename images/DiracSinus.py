import numpy as np
import matplotlib.pyplot as plt

# Diskrete Zeitbasis
n = np.arange(0, 20)          # 40 Abtastpunkte
f = 0.1                       # Frequenz des Sinus
x = np.sin(2 * np.pi * f * n) # diskreter Sinus

plt.figure(figsize=(6, 3))
plt.stem(n, x)  # <- ohne use_line_collection
plt.xlabel("n (Abtastindex)")
plt.ylabel("x[n]")
plt.title("Sinus als Dirac-Impulsfolge (stem-Plot)")
plt.grid(True)

plt.tight_layout()
plt.savefig("SinusDirac.png", dpi=300)
plt.show()