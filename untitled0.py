import numpy as np
from scipy.signal import freqz
import matplotlib.pyplot as plt

alpha = 0.97
b = [1, -alpha]  # Pay (x[n] ve x[n-1] katsayıları)
a = [1]          # Payda (IIR kısmı yok)
# Scipy ile hesaplama (whole=False varsayılan olarak [0, π] aralığı verir)
omega_scipy, H_scipy = freqz(b=b, a=a, worN=2000, whole=True)  # whole=True ile [0, 2π]

# [-π, π] aralığına kaydırma
omega_scipy = omega_scipy - np.pi
H_scipy = np.fft.fftshift(H_scipy)  # Frekansları merkezleme
magnitude_dB_scipy = 20 * np.log10(np.abs(H_scipy))
phase_rad_scipy = np.angle(H_scipy)
# Manuel hesaplama (analitik çözüm)
omega_manual = np.linspace(-np.pi, np.pi, 2000)
H_manual = 1 - alpha * np.exp(-1j * omega_manual)
magnitude_dB_manual = 20 * np.log10(np.abs(H_manual))
phase_rad_manual = np.angle(H_manual)

plt.figure(figsize=(14, 10))

# Genlik Tepkisi Karşılaştırması
plt.subplot(2, 2, 1)
plt.plot(omega_scipy, magnitude_dB_scipy, 'b', label='Scipy freqz')
plt.plot(omega_manual, magnitude_dB_manual, 'r--', linewidth=2, label='Manuel')
plt.title('Genlik Tepkisi Karşılaştırması')
plt.ylabel('Genlik [dB]')
plt.grid(True)
plt.legend()

# Faz Tepkisi Karşılaştırması
plt.subplot(2, 2, 2)
plt.plot(omega_scipy, phase_rad_scipy, 'b', label='Scipy freqz')
plt.plot(omega_manual, phase_rad_manual, 'r--', linewidth=2, label='Manuel')
plt.title('Faz Tepkisi Karşılaştırması')
plt.ylabel('Faz [rad]')
plt.grid(True)
plt.legend()

# Hata Analizi
plt.subplot(2, 2, 3)
plt.plot(omega_manual, magnitude_dB_manual - magnitude_dB_scipy, 'k')
plt.title('Genlik Hatası (Manuel - Scipy)')
plt.xlabel('Normalize Frekans [rad/örnek]')
plt.ylabel('Hata [dB]')
plt.grid(True)
plt.ylim([-1e-10, 1e-10])  # Sayısal hata ölçeği

plt.subplot(2, 2, 4)
plt.plot(omega_manual, phase_rad_manual - phase_rad_scipy, 'k')
plt.title('Faz Hatası (Manuel - Scipy)')
plt.xlabel('Normalize Frekans [rad/örnek]')
plt.ylabel('Hata [rad]')
plt.grid(True)
plt.ylim([-1e-10, 1e-10])

plt.tight_layout()
plt.show()