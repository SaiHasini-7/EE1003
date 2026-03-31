import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x**2 + 2*y

def rk4(f, x0, y0, xf, h):
    xs, ys = [x0], [y0]
    x, y = x0, y0
    while x < xf - 1e-10:
        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h/2, y + h/2 * k2)
        k4 = f(x + h, y + h * k3)
        y = y + h/6*(k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        xs.append(x); ys.append(y)
    return np.array(xs), np.array(ys)
x0, y0, xf, h = 0.0, 1.0, 2.0, 0.25
xs, ys_rk4 = rk4(f, x0, y0, xf, h)

x_plot = np.linspace(0, 2, 500)
C = 5/4
y_plot = C*np.exp(2*x_plot) - x_plot**2/2 - x_plot/2 - 1/4

plt.figure()
plt.plot(x_plot, y_plot,
    label=r'Exact: $y=\frac{5}{4}e^{2x}-\frac{x^2}{2}-\frac{x}{2}-\frac{1}{4}$')
plt.plot(xs, ys_rk4, 'o--', label='RK4 (h=0.25)')
plt.scatter([0], [1], color='red', zorder=5)
plt.text(0.05, 1, ' (0,1)')
plt.title('Exact Solution vs RK4')
plt.xlabel('x'); plt.ylabel('y')
plt.legend(); plt.grid()
plt.savefig('plot2.png', dpi=150)
