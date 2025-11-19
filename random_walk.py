import numpy as np
from matplotlib import pyplot as plt

steps = 1000

x_positions = np.zeros(steps)
y_positions = np.zeros(steps)

for i in range(1,steps):
    x_direction = np.random.randint(-1,2)
    y_direction = np.random.randint(-1,2)

    x_positions[i] = x_positions[i-1] + x_direction
    y_positions[i] = y_positions[i-1] + y_direction

plt.title(f"Random Walk with {steps} Steps")

plt.plot(x_positions,y_positions, color='blue', alpha=0.5)

plt.scatter(x_positions[0], y_positions[0], color='green', s=100, label='start')
plt.scatter(x_positions[-1], y_positions[-1], color='red', s=100, label='end')

plt.legend()

plt.grid(True)

plt.show()
