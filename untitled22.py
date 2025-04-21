# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 20:15:15 2025

@author: Emin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import librosa
import librosa.display
import soundfile as sf

# Ses dosyasını yükle
y, fs = librosa.load('should.wav', sr=None)  # Orijinal örnekleme hızıyla yükle

# 1. Kendi Spektrogram Hesaplamamız
def custom_spectrogram(y, fs, nperseg, noverlap, mode='psd'):
    f, t, Sxx = signal.spectrogram(y, fs=fs, nperseg=nperseg, noverlap=noverlap, mode=mode)
    return f, t, 10 * np.log10(Sxx)  # dB cinsinden

# Dar bant spektrogram (uzun pencere)
f_narrow, t_narrow, Sxx_narrow = custom_spectrogram(y, fs, nperseg=1024, noverlap=512)

# Geniş bant spektrogram (kısa pencere)
f_wide, t_wide, Sxx_wide = custom_spectrogram(y, fs, nperseg=256, noverlap=128)

# 2. Librosa STFT ile Spektrogram
D = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft=1024, hop_length=512, win_length=1024)), ref=np.max)
t_librosa = librosa.frames_to_time(np.arange(D.shape[1]), sr=fs, hop_length=512)
f_librosa = librosa.fft_frequencies(sr=fs, n_fft=1024)

# Görselleştirme
plt.figure(figsize=(18, 12))

# Dar bant spektrogram
plt.subplot(3, 1, 1)
plt.pcolormesh(t_narrow, f_narrow, Sxx_narrow, shading='auto', cmap='viridis')
plt.colorbar(label='Güç (dB)')
plt.title('Dar Bant Spektrogram (1024 nokta FFT)')
plt.ylabel('Frekans (Hz)')
plt.ylim(0, 4000)

# Geniş bant spektrogram
plt.subplot(3, 1, 2)
plt.pcolormesh(t_wide, f_wide, Sxx_wide, shading='auto', cmap='viridis')
plt.colorbar(label='Güç (dB)')
plt.title('Geniş Bant Spektrogram (256 nokta FFT)')
plt.ylabel('Frekans (Hz)')
plt.ylim(0, 4000)

# Librosa STFT spektrogram
plt.subplot(3, 1, 3)
librosa.display.specshow(D, sr=fs, hop_length=512, x_axis='time', y_axis='linear', cmap='viridis')
plt.colorbar(label='dB')
plt.title('Librosa STFT Spektrogram (1024 nokta FFT)')
plt.ylim(0, 4000)

plt.tight_layout()
plt.show()

# Karşılaştırma Analizi
print("\nKarşılaştırma Sonuçları:")
print(f"Dar Bant Çözünürlük: Frekans {fs/1024:.1f} Hz, Zaman {1024/(2*fs):.3f} s")
print(f"Geniş Bant Çözünürlük: Frekans {fs/256:.1f} Hz, Zaman {256/(2*fs):.3f} s")
print(f"Librosa Çözünürlük: Frekans {fs/1024:.1f} Hz, Zaman {512/fs:.3f} s")