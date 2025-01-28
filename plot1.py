import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# #Triangle
# # Define a range of x values
# x = np.linspace(-10, 10, 100)  # 100 points from -10 to 10
# # Calculate the corresponding y values for the equation y = x + 1
# y = x + 1

#
#
#
# plt.plot(x, y, label="Line")
# # Add labels and title
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Y = AX + B")
#
# # Show the plot
# plt.grid(True)  # Optional: Adds a grid to the plot
# plt.legend()  # Optional: Adds a legend
# plt.show()


# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Define the arrowhead length and the line end before the arrow
arrow_length = 1  # Length of the axis lines (before arrows)
arrow_head_length = 0.1  # Length of the arrowheads

# Plot the X and Y axis lines with a fixed length before the arrow
ax.plot([0, arrow_length], [0, 0], color='black', linewidth=2)  # X-axis
ax.plot([0, 0], [0, arrow_length], color='black', linewidth=2)  # Y-axis

# Add arrows at the end of the lines
arrow_x = patches.FancyArrowPatch((arrow_length, 0), (arrow_length + arrow_head_length, 0), mutation_scale=15, color='black', arrowstyle="->")
arrow_y = patches.FancyArrowPatch((0, arrow_length), (0, arrow_length + arrow_head_length), mutation_scale=15, color='black', arrowstyle="->")

# Add the arrows to the plot
ax.add_patch(arrow_x)
ax.add_patch(arrow_y)

# Set the limits of the plot
ax.set_xlim(-0.5, 2)
ax.set_ylim(-0.5, 2)

# Optionally, add labels
ax.text(arrow_length + 0.1, 0, 'X', fontsize=12, verticalalignment='center', horizontalalignment='left')
ax.text(0, arrow_length + 0.1, 'Y', fontsize=12, verticalalignment='bottom', horizontalalignment='center')

# Hide the ticks on the axes
ax.set_xticks([])
ax.set_yticks([])

# Display the plot
plt.grid(True)
plt.title("X and Y Axes with Arrows, Lines Stop Before Arrows")
plt.show()



