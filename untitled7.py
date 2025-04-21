import numpy as np
import matplotlib.pyplot as plt

# Süzgeç parametreleri
beta_values = [0.5, 0.9, 1.2]  # β değerleri
n = np.arange(100)  # İlk 100 örnek

plt.figure(figsize=(15, 5))

for i, beta in enumerate(beta_values):
    # Impuls cevabını hesapla: h[n] = β^n * u[n]
    h = (beta ** n) * (n >= 0)  # u[n] birim basamak fonksiyonu
    
    # Kararsız durumda (β=1.2) sınırlama
    if beta == 1.2:
        h[h > 1e6] = np.nan  # Aşırı büyük değerleri gösterme
    
    plt.subplot(1, 3, i+1)
    plt.stem(n, h, basefmt=' ')
    plt.title(f'Impuls Cevabı (β={beta})')
    plt.xlabel('Örnek [n]')
    plt.ylabel('h[n]')
    plt.grid(True)
    plt.ylim(-0.1, 1.1 if beta != 1.2 else 10)  # Eksen sınırları

plt.tight_layout()
plt.show()