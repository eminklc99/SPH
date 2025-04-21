import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Parametreler
L = 15
h = np.ones(L)/L  # Impuls cevabı [0.0667, 0.0667, ...]
omega = np.linspace(-np.pi, np.pi, 1000)  # -π ile π arasında 1000 nokta

# 1. Manuel DTFT Hesaplama
H_manual = np.zeros(len(omega), dtype=complex)
for n in range(L):
    H_manual += h[n] * np.exp(-1j * omega * n)

# 2. freqz ile Hesaplama (tam aralıkta)
w_freqz, H_freqz = freqz(h, worN=2000, whole=True)
w_freqz = np.fft.fftshift(w_freqz) - np.pi  # [-π, π] aralığına kaydır
H_freqz = np.fft.fftshift(H_freqz)

# Faz hesaplama fonksiyonu (daha hassas)
def correct_phase(H):
    phase = np.angle(H)
    return np.unwrap(phase, discont=np.pi, period=2*np.pi)

# Grafikler
plt.figure(figsize=(14, 8))

# Genlik Cevabı
plt.subplot(2, 1, 1)
plt.plot(omega, np.abs(H_manual), 'b-', linewidth=2, label='Manuel DTFT')
plt.plot(w_freqz, np.abs(H_freqz), 'r--', label='freqz')
plt.title(f'Genlik Cevabı Karşılaştırması (L={L})')
plt.xlabel('Frekans (ω) [rad/örnek]')
plt.ylabel('|H(ω)|')
plt.grid(True)
plt.xlim(-np.pi, np.pi)
plt.legend()

# Faz Cevabı (Düzeltilmiş)
plt.subplot(2, 1, 2)
plt.plot(omega, correct_phase(H_manual), 'b-', linewidth=2, label='Manuel DTFT')
plt.plot(w_freqz, correct_phase(H_freqz), 'r--', label='freqz')
plt.title(f'Faz Cevabı Karşılaştırması (L={L})')
plt.xlabel('Frekans (ω) [rad/örnek]')
plt.ylabel('∠H(ω) [radyan]')
plt.grid(True)
plt.xlim(-np.pi, np.pi)
plt.legend()

plt.tight_layout()
plt.show()