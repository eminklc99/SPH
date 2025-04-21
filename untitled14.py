# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 09:06:41 2025

@author: Emin
"""

import numpy as np
import matplotlib.pyplot as plt

# Filtre katsayıları
b = [0.1 * 2, 0.1 * 1, 0, -0.1 * 1, -0.1 * 2]  # Pay katsayıları
a = [1, -0.98]  # Payda katsayıları

# Impulse cevabı
h = np.zeros(100)
x = np.zeros(100)
x[0] = 1  # delta[n]

for n in range(4, 100):
    h[n] = 0.98 * h[n-1] + 0.2 * x[n] + 0.1 * x[n-1] - 0.1 * x[n-3] - 0.2 * x[n-4]

# İlk 100 örneği çiz
plt.figure(figsize=(10, 4))
plt.stem(h[:100])
plt.title('Impulse Cevabı (İlk 100 Örnek)')
plt.xlabel('Zaman (n)')
plt.ylabel('Genlik')
plt.grid(True)
plt.show()