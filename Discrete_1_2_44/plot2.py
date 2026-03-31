import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x**3 - y/x

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

x0, y0, xf, h = 1.0, 1.0, 2.0, 0.25
xs, ys_rk4 = rk4(f, x0, y0, xf, h)

x = np.linspace(0.1, 2, 1000)
y = (x**4)/5 + 4/(5*x)

plt.figure()
plt.plot(x, y, label="Exact: y = x^4/5 + 4/(5x)")
plt.plot(xs, ys_rk4, 'o--', label="RK4 (h=0.25)")
plt.scatter([1], [1], color='red', zorder=5)
plt.text(1, 1, " (1,1)")
plt.title("Exact Solution vs RK4")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.savefig("plot2.png", dpi=150, bbox_inches='tight')
plt.show()