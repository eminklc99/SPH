import numpy as np
import matplotlib.pyplot as plt

# Sinyal oluşturma
n = np.arange(16)  # n = 0, 1, ..., 15
x = np.sin((3 * np.pi / 8) * n)  # x[n] = sin(3πn/8)

# FFT hesaplama
X = np.fft.fft(x)  # Hızlı Fourier Dönüşümü
magnitude = np.abs(X)  # Genlik spektrumu

# Frekans ekseni (Fs = 16 Hz olduğunu biliyoruz)
Fs = 16  # Örnekleme frekansı
freq = np.fft.fftfreq(len(x), d=1/Fs)  # Frekans bileşenleri

# Genlik spektrumunu çizdirme
plt.figure(figsize=(12, 6))
plt.stem(freq, magnitude, linefmt='b-', markerfmt='bo', basefmt=' ')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.title('x[n] Sinyalinin Genlik Spektrumu')
plt.grid(True)
plt.xticks(np.arange(-Fs/2, Fs/2 + 1, 1))  # Frekans eksenini 1 Hz aralıklarla göster
plt.xlim(-Fs/2, Fs/2)  # -8 Hz ile +8 Hz arasını göster
plt.show()