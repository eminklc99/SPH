# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 19:30:51 2025

@author: Emin
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Create the frequency range
omega = np.linspace(-np.pi, np.pi, 1000)

# Create a linear phase response (∠H(e^jω) = -αω)
alpha = 2  # Phase slope parameter (adjust as needed)
phase = -alpha * omega

# Wrap phase to [-π, π] range
phase = np.angle(np.exp(1j*phase))

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(omega, phase, linewidth=3)
plt.title('Phase Response ∠H(e$^{jω}$)')
plt.xlabel('Frequency ω (radians/sample)')
plt.ylabel('Phase (radians)')

# Set x-axis ticks
plt.xticks([-np.pi, 0, np.pi], ['-π', '0', 'π'])

# Set y-axis ticks
plt.yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], 
           ['-π', '-π/2', '0', 'π/2', 'π'])

# Add grid and limits
plt.xlim(-np.pi, np.pi)
plt.ylim(-np.pi*1.1, np.pi*1.1)
plt.grid(True, which='both', alpha=0.3)

# Add the annotations
plt.text(np.pi/4, -alpha*np.pi/4, f'Slope = -{alpha}', 
         ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()