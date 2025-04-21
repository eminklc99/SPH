# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 19:58:43 2025

@author: Emin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

def pulse_train(F0, fs, T):
    """
    Periyodik darbe treni oluşturur
    Parametreler:
        F0 (Hz): Temel frekans
        fs (Hz): Örnekleme frekansı
        T (s): Sinyal süresi
    Çıktı:
        t: Zaman vektörü
        pt: Darbe treni sinyali
    """
    t = np.arange(0, T, 1/fs)
    T0 = 1/F0
    pt = np.zeros_like(t)
    pulse_indices = np.round(np.arange(0, T, T0) * fs).astype(int)
    pulse_indices = pulse_indices[pulse_indices < len(t)]
    pt[pulse_indices] = 1
    return t, pt

def plot_time_and_frequency(t, signal, fs, title, color):
    """Zaman ve frekans domaininde çizim yapar"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Zaman domaini
    ax1.stem(t[:200], signal[:200], linefmt=f'{color}-', markerfmt=f'{color}o', basefmt=' ')
    ax1.set_title(f'{title} - Zaman Domaini (İlk 25 ms)')
    ax1.set_xlabel('Zaman (s)')
    ax1.set_ylabel('Genlik')
    ax1.set_xlim(0, 0.025)
    ax1.grid(True, linestyle=':', alpha=0.7)
    
    # Frekans domaini (FFT)
    n = len(signal)
    yf = fft(signal)
    xf = fftfreq(n, 1/fs)[:n//2]
    
    # Hanning penceresi uygula
    window = np.hanning(n)
    yf_windowed = fft(signal * window)
    
    ax2.stem(xf, 2/n * np.abs(yf_windowed[:n//2]), linefmt=f'{color}-', markerfmt=f'{color}o', basefmt=' ')
    ax2.set_title(f'{title} - Frekans Domaini')
    ax2.set_xlabel('Frekans (Hz)')
    ax2.set_ylabel('Genlik')
    ax2.set_xlim(0, 1000)
    ax2.grid(True, linestyle=':', alpha=0.7)
    
    # Temel frekans ve harmonikleri işaretle
    F0 = 1/(t[np.where(signal==1)[0][1]] - t[np.where(signal==1)[0][0]])
    for k in range(1, 6):
        ax2.axvline(k*F0, color='gray', linestyle='--', alpha=0.5)
        ax2.text(k*F0, 0.8*max(2/n * np.abs(yf_windowed[:n//2])), 
                f'{k}F0', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()

# Parametreler
fs = 8000
duration = 0.05

# Sinyalleri oluştur ve çiz
t_male, male_speech = pulse_train(100, fs, duration)
t_female, female_speech = pulse_train(220, fs, duration)

plot_time_and_frequency(t_male, male_speech, fs, 'Erkek Ses Simülasyonu (F0=100Hz)', 'b')
plot_time_and_frequency(t_female, female_speech, fs, 'Kadın Ses Simülasyonu (F0=220Hz)', 'r')

# Karşılaştırmalı spektrum
plt.figure(figsize=(12, 5))
n = len(male_speech)
window = np.hanning(n)

# Erkek ses spektrumu
yf_male = fft(male_speech * window)
xf = fftfreq(n, 1/fs)[:n//2]
plt.stem(xf, 2/n * np.abs(yf_male[:n//2]), linefmt='b-', markerfmt='bo', basefmt=' ', label='Erkek (100Hz)')

# Kadın ses spektrumu
yf_female = fft(female_speech * window)
plt.stem(xf, 2/n * np.abs(yf_female[:n//2]), linefmt='r-', markerfmt='ro', basefmt=' ', label='Kadın (220Hz)')

plt.title('Karşılaştırmalı Frekans Spektrumu')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.xlim(0, 1000)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

def pulse_train(F0, fs, T):
    t = np.arange(0, T, 1/fs)
    T0 = 1/F0
    pt = np.zeros_like(t)
    pulse_indices = np.round(np.arange(0, T, T0) * fs).astype(int)
    pulse_indices = pulse_indices[pulse_indices < len(t)]
    pt[pulse_indices] = 1
    return t, pt

def plot_time_frequency_dB(t, signal, fs, title, color):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # Zaman domaini (orijinal)
    ax1.stem(t[:200], signal[:200], linefmt=f'{color}-', markerfmt=f'{color}o', basefmt=' ')
    ax1.set_title(f'{title} - Zaman Domaini', fontsize=12, pad=15)
    ax1.set_xlabel('Zaman (s)', fontsize=10)
    ax1.set_ylabel('Genlik', fontsize=10)
    ax1.set_xlim(0, 0.025)
    ax1.grid(True, linestyle=':', alpha=0.6)
    
    # Frekans domaini (dB cinsinden)
    n = len(signal)
    window = np.hanning(n)
    yf = fft(signal * window)
    xf = fftfreq(n, 1/fs)[:n//2]
    
    # dB'ye dönüşüm (referans 1.0)
    magnitude = 20 * np.log10(np.abs(yf[:n//2]) + 1e-10)  # 1e-10 ile log(0) hatası önlenir
    
    ax2.plot(xf, magnitude, color=color, linewidth=1.5)
    ax2.set_title(f'{title} - Frekans Domaini (dB Scale)', fontsize=12, pad=15)
    ax2.set_xlabel('Frekans (Hz)', fontsize=10)
    ax2.set_ylabel('Genlik (dB)', fontsize=10)
    ax2.set_xlim(0, 1000)
    ax2.set_ylim(-80, 0)  # dB sınırları
    ax2.grid(True, which='both', linestyle=':', alpha=0.6)
    
    # Temel frekans ve harmonikleri işaretle
    F0 = 1/(t[np.where(signal==1)[0][1]] - t[np.where(signal==1)[0][0]])
    for k in range(1, 6):
        freq = k * F0
        ax2.axvline(freq, color='gray', linestyle='--', alpha=0.4)
        ax2.text(freq, 5, f'{k}F0', ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.show()

# Parametreler ve sinyal üretimi
fs = 8000
duration = 0.05
t_male, male_speech = pulse_train(100, fs, duration)
t_female, female_speech = pulse_train(220, fs, duration)

# Grafikleri çiz
plot_time_frequency_dB(t_male, male_speech, fs, 'Erkek Ses (F0=100Hz)', 'blue')
plot_time_frequency_dB(t_female, female_speech, fs, 'Kadın Ses (F0=220Hz)', 'red')

