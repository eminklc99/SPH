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
    
    # Zaman domaini
    markerline, stemlines, baseline = ax1.stem(t[:200], signal[:200], basefmt=" ")
    plt.setp(stemlines, 'color', color)
    plt.setp(markerline, 'color', color, 'markersize', 5)
    
    ax1.set_title(f'{title} - Zaman Domaini', fontsize=12, pad=15)
    ax1.set_xlabel('Zaman (s)', fontsize=10)
    ax1.set_ylabel('Genlik', fontsize=10)
    ax1.set_xlim(0, 0.025)
    ax1.grid(True, linestyle=':', alpha=0.6)
    
    # Frekans domaini (dB)
    n = len(signal)
    window = np.hanning(n)
    yf = fft(signal * window)
    xf = fftfreq(n, 1/fs)[:n//2]
    magnitude = 20 * np.log10(np.abs(yf[:n//2]) + 1e-10)
    
    ax2.plot(xf, magnitude, color=color, linewidth=1.5)
    ax2.set_title(f'{title} - Frekans Domaini (dB)', fontsize=12, pad=15)
    ax2.set_xlabel('Frekans (Hz)', fontsize=10)
    ax2.set_ylabel('Genlik (dB)', fontsize=10)
    ax2.set_xlim(0, 1000)
    ax2.set_ylim(-80, 0)
    ax2.grid(True, which='both', linestyle=':', alpha=0.6)
    
    # Harmonik işaretleri
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

# Karşılaştırmalı spektrum
plt.figure(figsize=(14, 6))
n = len(male_speech)
window = np.hanning(n)
xf = fftfreq(n, 1/fs)[:n//2]

# Düzeltilmiş çizim formatı
plt.plot(xf, 20*np.log10(np.abs(fft(male_speech*window)[:n//2])+1e-10), 
         color='blue', label='Erkek (100Hz)', linewidth=1.5, alpha=0.8)
plt.plot(xf, 20*np.log10(np.abs(fft(female_speech*window)[:n//2])+1e-10), 
         color='red', label='Kadın (220Hz)', linewidth=1.5, alpha=0.8)

# Grafik düzenleme
plt.title('Karşılaştırmalı Frekans Spektrumu (dB)', fontsize=14, pad=20)
plt.xlabel('Frekans (Hz)', fontsize=12)
plt.ylabel('Genlik (dB)', fontsize=12)
plt.xlim(0, 1000)
plt.ylim(-80, 0)
plt.grid(True, which='both', linestyle=':', alpha=0.6)

# Harmonik işaretçiler
for f0, color in [(100, 'blue'), (220, 'red')]:
    for k in range(1, 6):
        freq = k * f0
        plt.axvline(freq, color=color, linestyle='--', alpha=0.3)
        if k == 1:
            plt.text(freq, -10, f'{f0}Hz', ha='center', color=color)

plt.legend(fontsize=12, framealpha=1)
plt.tight_layout()
plt.show()