import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# Transfer fonksiyonu katsayıları
alpha = 0.97
b = [0.2, 0.1, 0, -0.1, -0.2]  # Pay katsayıları: 0.2z^4 + 0.1z^3 - 0.1z - 0.2
a = [1, -0.97, 0, 0, 0]         # Payda katsayıları: z^4 - 0.97z^3

# Impuls girişi oluştur (delta fonksiyonu)
impuls = np.zeros(100)
impuls[0] = 1  # δ[0] = 1, diğerleri 0

# Süzgeç uygula
impuls_cevabi = lfilter(b, a, impuls)

# Çizim
plt.figure(figsize=(12, 6))
plt.stem(impuls_cevabi, basefmt='C0-')
plt.title('Süzgecin Impuls Cevabı (İlk 100 Örnek)')
plt.xlabel('Zaman [n]')
plt.ylabel('Genlik')
plt.grid(True)
plt.xlim([-1, 100])
plt.show()