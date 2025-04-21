# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 18:08:54 2025

@author: Emin
"""

import numpy as np
import matplotlib.pyplot as plt

# Orijinal sinyali oluşturma (16 nokta)
n_original = np.arange(16)
x_original = np.sin((3 * np.pi / 8) * n_original)

# 64 noktalı FFT için sinyali sıfır-padding ile uzatma
x_64 = np.zeros(64)
x_64[:16] = x_original  # İlk 16 noktaya orijinal sinyal, gerisi sıfır

# 64-noktalı FFT hesaplama
X_64 = np.fft.fft(x_64)
magnitude_64 = np.abs(X_64)  # Genlik spektrumu

# Frekans ekseni (Fs = 16 Hz olduğunu biliyoruz)
Fs = 16  # Örnekleme frekansı
freq_64 = np.fft.fftfreq(64, d=1/Fs)  # 64 nokta için frekans bileşenleri

# Genlik spektrumunu çizdirme
plt.figure(figsize=(14, 6))

# 64-noktalı FFT sonucu
plt.subplot(1, 2, 1)
plt.stem(freq_64[:32], magnitude_64[:32], linefmt='b-', markerfmt='bo', basefmt=' ')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.title('64-Noktalı FFT Genlik Spektrumu (0-8 Hz)')
plt.grid(True)
plt.xticks(np.arange(0, 9, 1))  # 0-8 Hz arası
plt.xlim(0, 8)  # Sadece pozitif frekansları göster

# Tüm spektrum (simetriyi göstermek için)
plt.subplot(1, 2, 2)
plt.stem(freq_64, magnitude_64, linefmt='b-', markerfmt='bo', basefmt=' ')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.title('64-Noktalı FFT Genlik Spektrumu (Tam Aralık)')
plt.grid(True)
plt.xticks(np.arange(-8, 9, 2))  # -8 Hz ile +8 Hz arası
plt.xlim(-8, 8)

plt.tight_layout()
plt.show()