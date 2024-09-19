import numpy as np
import matplotlib.pyplot as plt

# Generate values for x from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 1000)

# Compute the sine of x
y = np.sin(x)

# Create the plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('x (radians)')
plt.ylabel('sin(x)')
plt.title('Sine Wave')

# Display the plot
plt.grid(True)
plt.show()
