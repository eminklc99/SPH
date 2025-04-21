import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Parametreler
N = 31  # Pencere uzunluğu
fs = 10000  # Örnekleme frekansı (10 kHz)
n_fft = 1024  # FFT nokta sayısı

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
plt.title('Pencere Fonksiyonlarının Karşılaştırmalı Genlik Spektrumları\nN=31, fs=10 kHz, 1024-nokta FFT')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Normalize Genlik (Maksimum=1)')
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.xlim(0, fs/2)  # 0-5 kHz aralığı
plt.ylim(0, 1.1)  # Genlik 0-1 arası (biraz üst boşluk bıraktık)
plt.legend(loc='upper right')
plt.tight_layout()

# Ana lob ve yan lobları daha iyi görebilmek için x ekseni sınırlarını daraltabiliriz
plt.figure(figsize=(12, 6))
plt.plot(freq, rect_mag, label='Rectangular Pencere', linewidth=2)
plt.plot(freq, hamm_mag, label='Hamming Pencere', linewidth=2)
plt.plot(freq, hann_mag, label='Hanning Pencere', linewidth=2)

plt.title('Pencere Fonksiyonlarının Yakınlaştırılmış Genlik Spektrumları\n(0-2000 Hz Aralığı)')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Normalize Genlik (Maksimum=1)')
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.xlim(0, 2000)  # 0-2 kHz aralığına yakınlaştırma
plt.ylim(0, 1.1)
plt.legend(loc='upper right')
plt.tight_layout()

plt.show()