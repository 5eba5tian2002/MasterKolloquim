import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# --- Parameter ---
fs = 1000          # Abtastrate [Hz]
T = 1              # Dauer [s]
t = np.linspace(0, T, fs*T, endpoint=False)

f0 = 5             # Sinusfrequenz [Hz]
noise_level = 0.5  # Rauschstärke

# --- Originales Sinussignal ---
x_clean = np.sin(2 * np.pi * f0 * t)

# --- Rauschen hinzufügen ---
noise = noise_level * np.random.randn(len(t))
x_noisy = x_clean + noise

# --- Tiefpassfilter (Butterworth) ---
fc = 10  # Grenzfrequenz [Hz]
order = 4

b, a = butter(order, fc / (fs / 2), btype='low')
x_filtered = filtfilt(b, a, x_noisy)

# --- Plot ---
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x_noisy, label="Verrauschtes Signal", color="gray")
plt.plot(t, x_clean, label="Originaler Sinus", color="blue", alpha=0.7)
plt.title("Verrauschtes Sinussignal")
plt.xlabel("Zeit [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, x_filtered, label="Gefiltertes Signal (Tiefpass)", color="red")
plt.title("Tiefpass-gefiltertes Ausgangssignal")
plt.xlabel("Zeit [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("FilterungTP.png", dpi=300)
plt.show()