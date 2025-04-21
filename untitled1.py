# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 03:50:21 2025

@author: Emin
"""

import numpy as np
import matplotlib.pyplot as plt

# Parametreler
alpha = 0.97
omega = np.linspace(-np.pi, np.pi, 1000)  # -π ile π arasında 1000 nokta

# Teorik frekans tepkisi
H = 1 - alpha * np.exp(-1j * omega)  # Karmaşık değerler

# Genlik ve faz hesaplama
magnitude = np.abs(H)          # Genlik (lineer)
magnitude_dB = 20 * np.log10(magnitude)  # Genlik (dB)
phase_rad = np.angle(H)        # Faz (radyan)

# Grafik çizimi
plt.figure(figsize=(12, 6))

# Genlik Tepkisi (dB)
plt.subplot(2, 1, 1)
plt.plot(omega, magnitude_dB, 'b', linewidth=2)
plt.title('Teorik Genlik Tepkisi (α=0.97)')
plt.ylabel('Genlik [dB]')
plt.grid(True)
plt.axvline(0, color='k', linestyle='--')  # ω=0 çizgisi
plt.xlim([-np.pi, np.pi])

# Faz Tepkisi (radyan)
plt.subplot(2, 1, 2)
plt.plot(omega, phase_rad, 'r', linewidth=2)
plt.title('Teorik Faz Tepkisi')
plt.xlabel('Normalize Frekans [rad/örnek]')
plt.ylabel('Faz [rad]')
plt.grid(True)
plt.axvline(0, color='k', linestyle='--')
plt.xlim([-np.pi, np.pi])

plt.tight_layout()
plt.show()

# Genlik grafiğine işaretler ekle
plt.subplot(2, 1, 1)
plt.plot(0, 20 * np.log10(1 - alpha), 'ro')  # ω=0
plt.text(0, 20 * np.log10(1 - alpha) + 5, f'ω=0: {20 * np.log10(1 - alpha):.1f} dB', ha='center')
plt.plot(np.pi, 20 * np.log10(1 + alpha), 'go')  # ω=π
plt.text(np.pi, 20 * np.log10(1 + alpha) - 5, f'ω=π: {20 * np.log10(1 + alpha):.1f} dB', ha='center')

# Faz grafiğine işaretler ekle
plt.subplot(2, 1, 2)
plt.plot(np.pi, np.angle(1 - alpha * np.exp(-1j * np.pi)), 'go')
plt.text(np.pi, np.angle(1 - alpha * np.exp(-1j * np.pi)) - 0.5, 'ω=π', ha='center')

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           ['-π\n(-8 kHz)', '-π/2\n(-4 kHz)', '0\n(DC)', 'π/2\n(4 kHz)', 'π\n(8 kHz)'])

from scipy.signal import freqz

# Scipy ile frekans tepkisi
w_scipy, H_scipy = freqz([1, -alpha], worN=1000, whole=True)
w_scipy = w_scipy - np.pi  # [-π, π] aralığına kaydır

# Teorik ve Scipy sonuçlarını üst üste çiz
plt.figure()
plt.plot(omega, magnitude_dB, 'b', label='Teorik')
plt.plot(w_scipy, 20 * np.log10(np.abs(H_scipy)), 'r--', label='Scipy')
plt.legend()