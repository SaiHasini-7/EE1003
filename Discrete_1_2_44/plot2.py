import numpy as np
import matplotlib.pyplot as plt

# Define x range (avoid x = 0)
x = np.linspace(0.1, 2, 1000)

# Solution of the differential equation
y = (x**4)/5 + 4/(5*x)

# Boundary condition
x_bc = 1
y_bc = 1

# Plot the solution
plt.figure()
plt.plot(x, y, label="y = x^4/5 + 4/(5x)")
# Mark boundary condition
plt.scatter([x_bc], [y_bc])
plt.text(x_bc, y_bc, " (1,1)")

plt.title("Solution with Boundary Condition")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.savefig('plot2.png', dpi=150)
plt.show()
