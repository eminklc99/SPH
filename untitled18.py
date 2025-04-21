import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Create the frequency range
omega = np.linspace(-np.pi, np.pi, 1000)
H = np.zeros_like(omega)

# Define the triangular magnitude response
cutoff = 2*np.pi/5
peak_value = 1/5  # Since area should be 1 (1/L where L=5 in this case)

for i, w in enumerate(omega):
    if -cutoff <= w <= cutoff:
        H[i] = peak_value * (1 - np.abs(w)/cutoff)
    else:
        H[i] = 0

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(omega, H, linewidth=3)
plt.title('Magnitude Response |H(e$^{jω}$)|')
plt.xlabel('Frequency ω (radians/sample)')
plt.ylabel('Magnitude')

# Set x-axis ticks
plt.xticks([-np.pi, -2*np.pi/5, 0, 2*np.pi/5, np.pi],
           ['-π', '-2π/5', '0', '2π/5', 'π'])

# Add grid and limits
plt.xlim(-np.pi, np.pi)
plt.ylim(0, 1.1*peak_value)
plt.grid(True, which='both', alpha=0.3)

# Add the annotations
plt.text(0, peak_value*1.05, '1/L', ha='center', fontsize=12)
plt.annotate('', xy=(0, peak_value), xytext=(0, 0),
             arrowprops=dict(arrowstyle='<->', lw=1.5))

plt.tight_layout()
plt.show()