import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Parametreler
beta_values = [0.5, 0.9, 1.2]  # β değerleri
omega = np.linspace(-np.pi, np.pi, 1000)  # Frekans aralığı: -π ile π

plt.figure(figsize=(15, 10))

for i, beta in enumerate(beta_values):
    # Manuel DTFT Hesaplama (analitik çözüm)
    H_manual = np.exp(1j * omega) / (np.exp(1j * omega) - beta)
    magnitude_manual = np.abs(H_manual)
    phase_manual = np.angle(H_manual)
    
    # freqz ile Hesaplama (sayısal çözüm)
    # Dikkat: Kararsız sistemler için farklı yaklaşım
    if abs(beta) < 1:  # Kararlı sistemler
        b = [1]  # Pay katsayıları
        a = [1, -beta]  # Payda katsayıları
        w_freqz, H_freqz = freqz(b, a, worN=1000, whole=True)
    else:  # Kararsız sistemler
        # Kararsız sistemler için farklı bir yaklaşım
        N = 1000  # Sonlu sayıda örnek
        n = np.arange(N)
        h = beta**n  # Üstel artan impuls cevabı
        w_freqz, H_freqz = freqz(h, worN=1000, whole=True)
    
    # Frekaz vektörünü [-π, π] aralığına ayarla
    w_freqz = np.linspace(-np.pi, np.pi, len(H_freqz))
    H_freqz = np.fft.fftshift(H_freqz)
    
    # Fazı düzgün şekilde unwrap etme
    def correct_phase(phase):
        return np.unwrap(phase, discont=np.pi)
    
    # Grafikler
    plt.subplot(3, 2, 2*i+1)
    plt.plot(omega, magnitude_manual, 'b-', linewidth=2, label='Analitik')
    plt.plot(w_freqz, np.abs(H_freqz), 'r--', label='freqz')
    plt.title(f'Genlik Cevabı (β={beta})')
    plt.xlabel('Frekans (ω) [rad/örnek]')
    plt.ylabel('|H(ω)|')
    plt.grid(True)
    plt.xlim(-np.pi, np.pi)
    plt.legend()
    
    plt.subplot(3, 2, 2*i+2)
    plt.plot(omega, correct_phase(phase_manual), 'b-', linewidth=2, label='Analitik')
    plt.plot(w_freqz, correct_phase(np.angle(H_freqz)), 'r--', label='freqz')
    plt.title(f'Faz Cevabı (β={beta})')
    plt.xlabel('Frekans (ω) [rad/örnek]')
    plt.ylabel('∠H(ω) [radyan]')
    plt.grid(True)
    plt.xlim(-np.pi, np.pi)
    plt.legend()

plt.tight_layout()
plt.show()