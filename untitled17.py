import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from matplotlib.ticker import MultipleLocator

# Parametreler
N = 31
fs = 10000
n_fft = 1024
freq_limit = 4 * fs / N  # ≈1290.32 Hz
fs_N = fs/N  # ≈322.58 Hz

# Pencere fonksiyonları ve teorik bilgiler
windows = {
    'Rectangular': {
        'window': np.ones(N),
        'main_lobe': 2,
        'formula': r'$W_{rect}(n) = 1$'
    },
    'Hamming': {
        'window': 0.54 - 0.46*np.cos(2*np.pi*np.arange(N)/(N-1)),
        'main_lobe': 4,
        'formula': r'$W_{ham}(n) = 0.54 - 0.46\cos(\frac{2\pi n}{N-1})$'
    },
    'Hanning': {
        'window': 0.5 - 0.5*np.cos(2*np.pi*np.arange(N)/(N-1)),
        'main_lobe': 4,
        'formula': r'$W_{han}(n) = 0.5 - 0.5\cos(\frac{2\pi n}{N-1})$'
    }
}

# Stil ayarları
plt.style.use('seaborn-v0_8-poster')
fig, ax = plt.subplots(figsize=(16, 8))

# Renk paleti
colors = plt.cm.tab10.colors

# FFT hesaplama ve çizim
for i, (name, data) in enumerate(windows.items()):
    window = data['window']
    fft_result = fft(window, n_fft)
    mag = np.abs(fft_result[:n_fft//2]) / np.max(np.abs(fft_result))
    freq = np.linspace(0, fs/2, n_fft//2)
    
    # Ana lob genişliğini hesapla
    null_index = np.where(mag < 0.001)[0][0] if name != 'Rectangular' else np.where(mag < 0.01)[0][0]
    main_lobe_width = 2 * freq[null_index]
    main_lobe_fsN = main_lobe_width / fs_N
    
    # Çizgi ve formül bilgisi
    line, = ax.plot(freq, mag, label=f'{name}\n{data["formula"]}', 
                   linewidth=3, alpha=0.8, color=colors[i],
                   marker='o' if i==0 else '', 
                   markevery=int(n_fft/(8*N)), 
                   markersize=8 if i==0 else 0)
    
    # Ana lob genişliği annotasyonu
    ax.annotate(f'Δf = {main_lobe_fsN:.1f} fs/N\nTeorik: {data["main_lobe"]} fs/N',
               xy=(main_lobe_width/2, 0.5),
               xytext=(main_lobe_width/2, 0.7 - i*0.15),
               color=line.get_color(),
               arrowprops=dict(arrowstyle="->", color=line.get_color()),
               ha='center', fontsize=12, weight='bold',
               bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.8))

# fs/N çizgileri
for k in range(1,5):
    freq_line = k*fs_N
    ax.axvline(freq_line, color='darkred', linestyle=':', alpha=0.7, linewidth=1.5)
    ax.text(freq_line, 1.02, f'{k}·fs/N', ha='center', va='bottom', 
            color='darkred', bbox=dict(facecolor='white', alpha=0.8))

# Eksen ve grid ayarları
ax.set_xlim(0, freq_limit)
ax.set_ylim(0, 1.1)
ax.xaxis.set_major_locator(MultipleLocator(fs_N))
ax.xaxis.set_minor_locator(MultipleLocator(fs_N/2))
ax.yaxis.set_major_locator(MultipleLocator(0.2))
ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.grid(which='major', linestyle='-', linewidth=1, alpha=0.7)
ax.grid(which='minor', linestyle=':', linewidth=1, alpha=0.4)

# Başlık ve etiketler
ax.set_title('Pencere Fonksiyonlarının Ana Lob Genişlikleri ve Formülleri\n'
            f'$N$={N}, $f_s$={fs/1000} kHz, $f_s/N$≈{fs_N:.1f} Hz',
            pad=20, fontsize=14)
ax.set_xlabel('Frekans (Hz)', labelpad=10)
ax.set_ylabel('Normalize Genlik', labelpad=10)

# Gösterge (legend)
ax.legend(loc='upper right', framealpha=1, shadow=True, fontsize=12)

plt.tight_layout()
plt.show()