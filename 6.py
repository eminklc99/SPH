import numpy as np
import matplotlib.pyplot as plt

# Sinyal oluşturma
x = np.zeros(16)
x[0] = 1  # Birim darbe

# FFT hesaplama
X = np.fft.fft(x)
magnitude = np.abs(X)  # Genlik spektrumu

# Frekans ekseni
Fs = 16  # Örnekleme frekansı (örnek sayısı = Fs varsayımıyla)
freq = np.fft.fftfreq(len(x), d=1/Fs)

# Genlik spektrumunu çizdirme
plt.figure(figsize=(12, 6))
plt.stem(freq, magnitude, linefmt='b-', markerfmt='bo', basefmt=' ')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.title('Birim Darbenin Genlik Spektrumu (16-Noktalı FFT)')
plt.grid(True)
plt.xticks(np.arange(-8, 9, 1))
plt.xlim(-8, 8)
plt.show()