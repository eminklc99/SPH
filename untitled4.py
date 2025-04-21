import numpy as np
import matplotlib.pyplot as plt

# Sistem parametreleri
N = 100  # Örnek sayısı
x = np.zeros(N+4)  # Gelecek örnekler için ekstra yer
x[4] = 1  # δ[n] (x[n+4] için n=0'da impuls)
y = np.zeros(N)

# Kausal olmayan fark denklemi uygula
for n in range(N):
    y[n] = 0.98 * y[n-1] + 0.2 * x[n+4] + 0.1 * x[n+3] - 0.1 * x[n+1] - 0.2 * x[n]

# Çizim
plt.figure(figsize=(12, 6))
plt.stem(y, linefmt='C0-', markerfmt='C0o')
plt.title('Kausal Olmayan Süzgeç İmpuls Cevabı\n' + 
          r'$y[n]=0.98y[n-1]+0.2x[n+4]+0.1x[n+3]-0.1x[n+1]-0.2x[n]$')
plt.xlabel('Zaman [n]')
plt.ylabel('Genlik')
plt.grid(True)
plt.xlim([-1, N])