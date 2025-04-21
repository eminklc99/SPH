# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 08:19:52 2025

@author: Emin
"""

import numpy as np
import matplotlib.pyplot as plt

# Parametreler
beta_values = [0.5, 0.9, 1.2]  # β değerleri
n = np.arange(100)  # İlk 100 örnek

plt.figure(figsize=(15, 5))

for i, beta in enumerate(beta_values):
    # Impuls cevabını hesapla: h[n] = β^n
    h = beta**n
    
    # Kararsız sistemler için sınırlama (β=1.2)
    if beta == 1.2:
        h[h > 1e6] = np.nan  # Aşırı büyük değerleri gösterme
    
    plt.subplot(1, 3, i+1)
    markerline, stemlines, baseline = plt.stem(n, h, linefmt='b-', markerfmt='bo', basefmt=' ')
    plt.setp(stemlines, 'linewidth', 1)
    plt.setp(markerline, 'markersize', 3)
    
    plt.title(f'Impuls Cevabı (β={beta})')
    plt.xlabel('Örnek [n]')
    plt.ylabel('h[n]')
    plt.grid(True)
    
    # Eksen sınırlarını ayarla
    y_max = 1.1 if beta < 1 else 100 if beta == 1.2 else 5
    plt.ylim(-0.1, y_max)

plt.tight_layout()
plt.show()