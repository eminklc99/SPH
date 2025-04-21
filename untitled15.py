# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 09:10:56 2025

@author: Emin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Süzgeç katsayıları
b = [0.2, 0.1, 0, -0.1, -0.2]  # Pay (0.1*[2,1,0,-1,-2])
a = [1, -0.98]                  # Payda

# Impulse sinyali oluştur (delta[n])
impulse = np.zeros(100)
impulse[0] = 1  # n=0'da 1, diğerleri 0

# Süzgeç uygula (impulse cevabını hesapla)
h = signal.lfilter(b, a, impulse)

# Grafik çiz
plt.figure(figsize=(12, 6))
plt.stem(np.arange(100), h, linefmt='blue', markerfmt='bo', basefmt=' ')
plt.title('Nedensel Süzgecin Impulse Cevabı (İlk 100 Örnek)')
plt.xlabel('Zaman Örnekleri (n)')
plt.ylabel('Genlik')
plt.grid(True)
plt.xlim(0, 100)
plt.show()