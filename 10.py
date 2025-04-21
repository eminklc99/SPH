# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 19:04:04 2025

@author: Emin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Parametreler
N = 31  # Pencere uzunluğu
fs = 10000  # Örnekleme frekansı (10 kHz)
n_fft = 1024  # FFT nokta sayısı
freq_limit = 4 * fs / N  # 4fs/N frekans sınırı ≈ 1290.32 Hz

# Pencere fonksiyonları oluşturma
n = np.arange(N)
rectangular = np.ones(N)
hamming = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
hanning = 0.5 - 0.5 * np.cos(2 * np.pi * n / (N - 1))

# FFT hesaplama ve normalizasyon fonksiyonu
def compute_normalized_fft(window, n_fft):
    fft_result = fft(window, n_fft)
    magnitude = np.abs(fft_result) / np.max(np.abs(fft_result))  # Maksimum 1 olacak şekilde normalize
    freq = np.linspace(0, fs/2, n_fft//2)  # 0'dan fs/2'ye frekans ekseni
    return freq, magnitude[:n_fft//2]  # Sadece tek taraflı spektrum

# FFT hesaplamaları
freq, rect_mag = compute_normalized_fft(rectangular, n_fft)
_, hamm_mag = compute_normalized_fft(hamming, n_fft)
_, hann_mag = compute_normalized_fft(hanning, n_fft)

# Tüm pencereleri aynı grafikte çizme
plt.figure(figsize=(12, 6))
plt.plot(freq, rect_mag, label='Rectangular Pencere', linewidth=2)
plt.plot(freq, hamm_mag, label='Hamming Pencere', linewidth=2)
plt.plot(freq, hann_mag, label='Hanning Pencere', linewidth=2)

# Grafik özelleştirme
plt.title(f'Pencere Fonksiyonlarının Genlik Spektrumları [0, 4fs/N] Aralığında\nN={N}, fs={fs/1000} kHz, 4fs/N ≈ {freq_limit:.2f} Hz')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Normalize Genlik (Maksimum=1)')
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.xlim(0, freq_limit)  # 0-4fs/N aralığı
plt.ylim(0, 1.1)  # Genlik 0-1 arası
plt.legend(loc='upper right')

# Önemli frekans çizgileri
plt.axvline(fs/N, color='gray', linestyle=':', alpha=0.5, label='fs/N')
plt.axvline(2*fs/N, color='gray', linestyle=':', alpha=0.5, label='2fs/N')
plt.axvline(3*fs/N, color='gray', linestyle=':', alpha=0.5, label='3fs/N')
plt.axvline(4*fs/N, color='gray', linestyle=':', alpha=0.5, label='4fs/N')

plt.legend(loc='upper right', bbox_to_anchor=(1, 0.85))
plt.tight_layout()
plt.show()