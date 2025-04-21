# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 18:42:31 2025

@author: Emin
"""

import numpy as np
import matplotlib.pyplot as plt

N = 31  # Pencere uzunluğu
n = np.arange(N)

# Pencere fonksiyonları
rectangular = np.ones(N)
hamming = np.hamming(N)
hanning = np.hanning(N)

# Grafik çizimi
plt.figure(figsize=(12, 6))
plt.plot(n, rectangular, 'r-', label='Rectangular', linewidth=2)
plt.plot(n, hamming, 'g--', label='Hamming', linewidth=2)
plt.plot(n, hanning, 'b-.', label='Hanning', linewidth=2)
plt.title('Pencere Fonksiyonlarının Karşılaştırması (N=31)')
plt.xlabel('Örnek Indisi (n)')
plt.ylabel('Genlik')
plt.legend()
plt.grid(True)
plt.xticks(np.arange(0, N, 5))
plt.show()

# Frekans tepkilerini hesapla
def plot_frequency_response(w, label):
    fft_result = np.abs(np.fft.fft(w, 1024))  # 1024-noktalı FFT
    fft_db = 20 * np.log10(fft_result / np.max(fft_result))
    freq = np.fft.fftfreq(1024, d=1/N)
    plt.plot(freq[:512], fft_db[:512], label=label)

plt.figure(figsize=(12, 6))
plot_frequency_response(rectangular, 'Rectangular')
plot_frequency_response(hamming, 'Hamming')
plot_frequency_response(hanning, 'Hanning')
plt.title('Pencere Fonksiyonlarının Frekans Tepkisi (dB)')
plt.xlabel('Normalleştirilmiş Frekans')
plt.ylabel('Genlik (dB)')
plt.ylim(-100, 5)
plt.legend()
plt.grid(True)
plt.show()