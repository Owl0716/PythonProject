import matplotlib.pyplot as plt
import numpy as np
#Triangle
# Define a range of x values
x = np.linspace(-10, 10, 100)  # 100 points from -10 to 10
x1 = np.linspace(10, 10, 100)  # 100 points from -10 to 10
x2 = np.linspace(-10, 10, 100)
y3 = np.full_like(x, -10)  # y = 3 for a horizontal line
# Calculate the corresponding y values for the equation y = x + 1
y1 = x + 1
y2 = -x - 1

# Plot the line
plt.plot(x, y1, label="Diagonal")
plt.plot(x1, y2, label="Vertical")
plt.plot(x2, y3, label="Horizontal")
# Add labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Triangle")

# Show the plot
plt.grid(True)  # Optional: Adds a grid to the plot
plt.legend()  # Optional: Adds a legend
plt.show()
