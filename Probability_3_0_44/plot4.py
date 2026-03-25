import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
 
# Parameters
mu_X, sigma_X = 1, 2      # X ~ N(1, 4)
mu_Y, sigma_Y = -1, 3     # Y ~ N(-1, 9)
 
# Range for plotting
x = np.linspace(-10, 10, 1000)
 
# PDFs
pdf_X = norm.pdf(x, mu_X, sigma_X)
pdf_Y = norm.pdf(x, mu_Y, sigma_Y)
# Plot curves
plt.figure(figsize=(8, 4))
plt.plot(x, pdf_X, linewidth=1.8,
         label=r'$X \sim \mathcal{N}(1,\,4)$')
plt.plot(x, pdf_Y, linewidth=1.8,
         label=r'$Y \sim \mathcal{N}(-1,\,9)$')
        
 # Shade P(X <= -1)
x_fill_X = np.linspace(-10, -1, 500)
plt.fill_between(x_fill_X,
                 norm.pdf(x_fill_X, mu_X, sigma_X), alpha=0.3, label=r'$P(X \leq -1)$')
# Shade P(Y >= 2)
x_fill_Y = np.linspace(2, 10, 500)
plt.fill_between(x_fill_Y,
               norm.pdf(x_fill_Y, mu_Y, sigma_Y),
               alpha=0.3, label=r'$P(Y \geq 2)$')
 
# Labels and formatting
plt.title(r'$P(X \leq -1)$ and $P(Y \geq 2)$', fontsize=12)
plt.xlabel('x'); plt.ylabel('Probability Density')
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('plot4.png', dpi=150)
