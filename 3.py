import numpy as np
import matplotlib.pyplot as plt

L = 5
omega = np.linspace(-np.pi, np.pi, 1000)
H_phase = -omega * (L-1)/2  # Teorik faz (sarmalanmamış)

# Düzeltme: Faz sarmalamayı aç
H_phase_unwrapped = np.unwrap(H_phase)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(omega, H_phase, 'r--', label='Sarmalanmış Faz')
plt.plot(omega, H_phase_unwrapped, 'b', label='Düzeltilmiş Faz')
plt.title('Faz Cevabı Karşılaştırması')
plt.xlabel('ω [rad/örnek]')
plt.ylabel('Faz [rad]')
plt.legend()
plt.grid(True)

# Genlik cevabı (orijinal kod)
H_magnitude = np.abs(np.sin(omega * L/2) / (L * np.sin(omega/2 + 1e-10)))
plt.subplot(1, 2, 2)
plt.plot(omega, H_magnitude)
plt.title('Genlik Cevabı')
plt.xlabel('ω [rad/örnek]')
plt.ylabel('|H(e^{jω})|')
plt.grid(True)

plt.tight_layout()
plt.show()