import numpy as np
import matplotlib.pyplot as plt

# Abbildung 1: f(x) = e^x auf dem Intervall [-5, 5] mit Schrittweite 0.05
x1 = np.arange(-5, 5, 0.05)
y1 = np.exp(x1)
plt.figure()
plt.plot(x1, y1)
plt.title('f(x) = e^x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

# Abbildung 2: p(x) = x^5 + 3x^4 + 3x^2 + x + 1 auf dem Intervall [-10, 10] mit Schrittweite 0.1
x2 = np.arange(-10, 10, 0.1)
y2 = x2**5 + 3*x2**4 + 3*x2**2 + x2 + 1
plt.figure()
plt.plot(x2, y2)
plt.title('p(x) = x^5 + 3x^4 + 3x^2 + x + 1')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.grid(True)

# Abbildung 3: g(x) = 1/2 sin(3x) und h(x) = 1/2 cos(3x) auf dem Intervall [-2π, 2π] mit Schrittweite 0.01
x3 = np.arange(-2*np.pi, 2*np.pi, 0.01)
y3_g = 0.5 * np.sin(3*x3)
y3_h = 0.5 * np.cos(3*x3)
plt.figure()
plt.plot(x3, y3_g, label='g(x) = 1/2 sin(3x)')
plt.plot(x3, y3_h, label='h(x) = 1/2 cos(3x)')
plt.title('g(x) und h(x) auf dem Intervall [-2π, 2π]')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Anzeigen der Plots
plt.show()