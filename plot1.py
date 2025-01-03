import matplotlib.pyplot as plt
import numpy as np

#Triangle
# Define a range of x values
x = np.linspace(-10, 10, 100)  # 100 points from -10 to 10
# Calculate the corresponding y values for the equation y = x + 1
y = x + 1



plt.plot(x, y, label="Line")
# Add labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Y = AX + B")

# Show the plot
plt.grid(True)  # Optional: Adds a grid to the plot
plt.legend()  # Optional: Adds a legend
plt.show()



