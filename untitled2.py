
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

alpha = 0.97
n = np.arange(0, 50)

# Ön-vurgulama ve ters süzegeç
def pre_emphasis(x, alpha):
    return lfilter([1, -alpha], [1], x)

def post_emphasis(y, alpha):
    return lfilter([1], [1, -alpha], y)  # Payda: [1, -α]

# Test sinyali (impuls)
x = np.zeros(50)
x[0] = 1  # δ[n]

# Ön-vurgulama + Ters süzegeç uygula
y = pre_emphasis(x, alpha)
x_recovered = post_emphasis(y, alpha)

# Çizim
plt.stem(n, x_recovered)
plt.title('Ters Süzegeç Çıktısı (Ön-Vurgulama İptal Edildi)')
plt.xlabel('Zaman [n]')
plt.ylabel('Genlik')
plt.grid(True)
plt.show()