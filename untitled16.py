import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(freq, magnitude, label='Rectangular Pencere')
plt.axvline(first_null_freq, color='red', linestyle='--', 
            label=f'Ana Lob Genişliği = {main_lobe_width/(fs/N):.1f} fs/N')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.legend()
plt.grid()
plt.show()