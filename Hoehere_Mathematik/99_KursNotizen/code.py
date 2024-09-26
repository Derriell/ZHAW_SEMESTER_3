import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(0, 10, 100)

# Generate y values as a sine function of x
y = np.pi * np.sin(x)

# Create the plot
plt.plot(x, y)

# Add title and labels
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')

# Show the plot
plt.show()