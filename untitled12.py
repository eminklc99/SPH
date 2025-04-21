# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 08:43:11 2025

@author: Emin
"""

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# Ses dosyasını yükle
audio, sample_rate = librosa.load('should.wav', sr=None, mono=True)

# Spektrogram parametreleri
n_fft_wide = 1024  # Geniş band için küçük FFT boyutu
hop_length_wide = 256  # Geniş band için küçük adım boyutu

n_fft_narrow = 4096  # Dar band için büyük FFT boyutu
hop_length_narrow = 1024  # Dar band için büyük adım boyutu

# Geniş band spektrogram
D_wide = librosa.stft(audio, n_fft=n_fft_wide, hop_length=hop_length_wide)
S_db_wide = librosa.amplitude_to_db(np.abs(D_wide), ref=np.max)

plt.figure(figsize=(12, 6))
librosa.display.specshow(S_db_wide, sr=sample_rate, hop_length=hop_length_wide, 
                         x_axis='time', y_axis='linear')
plt.colorbar(format='%+2.0f dB')
plt.title('Geniş Band Spektrogram (Librosa)')
plt.ylim(0, 5000)  # Üst frekans sınırı
plt.tight_layout()
plt.show()

# Dar band spektrogram
D_narrow = librosa.stft(audio, n_fft=n_fft_narrow, hop_length=hop_length_narrow)
S_db_narrow = librosa.amplitude_to_db(np.abs(D_narrow), ref=np.max)

plt.figure(figsize=(12, 6))
librosa.display.specshow(S_db_narrow, sr=sample_rate, hop_length=hop_length_narrow, 
                         x_axis='time', y_axis='linear')
plt.colorbar(format='%+2.0f dB')
plt.title('Dar Band Spektrogram (Librosa)')
plt.ylim(0, 2000)  # Daha düşük frekans aralığı
plt.tight_layout()
plt.show()