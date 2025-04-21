import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import librosa
import librosa.display

def plot_comparison(scipy_spec, librosa_spec, times_scipy, times_librosa, 
                   freqs_scipy, freqs_librosa, title1, title2, ylim, 
                   sample_rate, hop_length):
    plt.figure(figsize=(15, 6))
    
    plt.subplot(1, 2, 1)
    plt.pcolormesh(times_scipy, freqs_scipy, 10 * np.log10(scipy_spec), 
                  shading='gouraud', cmap='magma')
    plt.colorbar(label='Güç (dB)')
    plt.title(title1)
    plt.ylabel('Frekans (Hz)')
    plt.xlabel('Zaman (s)')
    plt.ylim(ylim)
    
    plt.subplot(1, 2, 2)
    librosa.display.specshow(librosa_spec, sr=sample_rate, 
                           hop_length=hop_length, x_axis='time', 
                           y_axis='linear', cmap='magma')
    plt.colorbar(format='%+2.0f dB')
    plt.title(title2)
    plt.ylim(ylim)
    
    plt.tight_layout()
    plt.show()

# Ses dosyasını yükle (scipy için)
sample_rate, audio_scipy = wavfile.read('should.wav')
if len(audio_scipy.shape) > 1:
    audio_scipy = audio_scipy.mean(axis=1)

# Ses dosyasını yükle (librosa için)
audio_librosa, _ = librosa.load('should.wav', sr=sample_rate, mono=True)

# Geniş band parametreleri
window_size = 1024
overlap = 512
n_fft_wide = 1024
hop_length_wide = 256

# Geniş band spektrogramlar
f_wide_scipy, t_wide_scipy, S_wide_scipy = signal.spectrogram(
    audio_scipy, fs=sample_rate, window='hann',
    nperseg=window_size, noverlap=overlap, mode='magnitude')

D_wide_librosa = librosa.stft(audio_librosa, n_fft=n_fft_wide, 
                             hop_length=hop_length_wide)
S_wide_librosa = librosa.amplitude_to_db(np.abs(D_wide_librosa), ref=np.max)

# Dar band parametreleri
window_size_narrow = 4096
overlap_narrow = 3072
n_fft_narrow = 4096
hop_length_narrow = 1024

# Dar band spektrogramlar
f_narrow_scipy, t_narrow_scipy, S_narrow_scipy = signal.spectrogram(
    audio_scipy, fs=sample_rate, window='hann',
    nperseg=window_size_narrow, noverlap=overlap_narrow, mode='magnitude')

D_narrow_librosa = librosa.stft(audio_librosa, n_fft=n_fft_narrow, 
                              hop_length=hop_length_narrow)
S_narrow_librosa = librosa.amplitude_to_db(np.abs(D_narrow_librosa), ref=np.max)

# Karşılaştırmaları çiz
print("GENİŞ BAND KARŞILAŞTIRMASI")
plot_comparison(S_wide_scipy, S_wide_librosa, t_wide_scipy, None,
               f_wide_scipy, None, 'Scipy Geniş Band', 'Librosa Geniş Band',
               (0, 5000), sample_rate, hop_length_wide)

print("\nDAR BAND KARŞILAŞTIRMASI")
plot_comparison(S_narrow_scipy, S_narrow_librosa, t_narrow_scipy, None,
               f_narrow_scipy, None, 'Scipy Dar Band', 'Librosa Dar Band',
               (0, 2000), sample_rate, hop_length_narrow)

# Librosa sprenk sınırları