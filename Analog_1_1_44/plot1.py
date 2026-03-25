import numpy as np
import matplotlib.pyplot as plt

# Time axis
t = np.linspace(0, 4, 1000)

# Parameters
K  = 0.6   # scale factor
t0 = 0.5   # time delay (seconds)

# Input signal (sum of sinusoids)
x = np.sin(2 * np.pi * t) + 0.4 * np.sin(2 * np.pi * 3 * t)

# Output: scaled and delayed (distortion-free)
y = K * (np.sin(2 * np.pi * (t - t0)) + 0.4 * np.sin(2 * np.pi * 3 * (t - t0)))

plt.figure(figsize=(8, 3.5))
plt.plot(t, x, 'b-',  linewidth=1.8, label=r'Input $x(t)$')
plt.plot(t, y, 'r--', linewidth=1.8, label=r'Output $y(t) = K\,x(t - t_0)$')

# Annotate delay arrow
plt.annotate('', xy=(0.5 + t0, 0.95), xytext=(0.5, 0.95),
             arrowprops=dict(arrowstyle='<->', color='black'))
plt.text(0.63, 1.0, r'$t_0 = 0.5\,$s', fontsize=9)

plt.xlabel(r'$t$ (s)', fontsize=11)
plt.ylabel('Amplitude', fontsize=11)
plt.title(r'Distortion-Free Output: $K = 0.6$, $t_0 = 0.5\,$s', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('plot1.png', dpi=150, bbox_inches='tight')
print("Plot saved.")