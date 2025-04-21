import numpy as np
import matplotlib.pyplot as plt

beta_values = [0.5, 0.9, 1.2]
n = np.arange(100)  # İlk 100 örnek

plt.figure(figsize=(10, 8))
for i, beta in enumerate(beta_values, 1):
    h = beta**n  # Impuls cevabı: h[n] = β^n
    
    plt.subplot(3, 1, i)
    plt.stem(n, h)
    plt.title(f'β = {beta}')
    plt.xlabel('Zaman örnekleri (n)')
    plt.ylabel('Genlik')
    plt.grid(True)
    
    # Kararlılık kontrolü
    if abs(beta) >= 1:
        plt.text(50, max(h)/2, 'KARARSIZ SİSTEM', color='red', fontweight='bold')

plt.tight_layout()
plt.suptitle('Süzgeç İmpuls Cevabı (İlk 100 Örnek)', y=1.02)
plt.show()