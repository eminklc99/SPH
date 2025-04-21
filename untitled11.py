# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 08:40:14 2025

@author: Emin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

# Ses dosyasını yükle
sample_rate, audio = wavfile.read('should.wav')

# Eğer stereo ise mono'ya çevir
if len(audio.shape) > 1:
    audio = audio.mean(axis=1)

# Spektrogram parametreleri
window_size = 1024  # Geniş band için daha küçük pencere
overlap = 512       

# Geniş band spektrogram
frequencies, times, spectrogram = signal.spectrogram(
    audio,
    fs=sample_rate,
    window='hann',
    nperseg=window_size,
    noverlap=overlap,
    mode='magnitude'
)

plt.figure(figsize=(12, 8))
plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram), shading='gouraud')
plt.colorbar(label='Güç (dB)')
plt.title('Geniş Band Spektrogram')
plt.ylabel('Frekans (Hz)')
plt.xlabel('Zaman (s)')
plt.ylim(0, 5000)  # Geniş band için daha yüksek frekansları göster
plt.show()

# Dar band spektrogram (daha büyük pencere boyutu)
window_size_narrow = 4096  # Dar band için daha büyük pencere
overlap_narrow = 3072     # Daha fazla örtüşme

frequencies_narrow, times_narrow, spectrogram_narrow = signal.spectrogram(
    audio,
    fs=sample_rate,
    window='hann',
    nperseg=window_size_narrow,
    noverlap=overlap_narrow,
    mode='magnitude'
)

plt.figure(figsize=(12, 8))
plt.pcolormesh(times_narrow, frequencies_narrow, 10 * np.log10(spectrogram_narrow), shading='gouraud')
plt.colorbar(label='Güç (dB)')
plt.title('Dar Band Spektrogram')
plt.ylabel('Frekans (Hz)')
plt.xlabel('Zaman (s)')
plt.ylim(0, 2000)  # Dar band için daha düşük frekanslara odaklan
plt.show()