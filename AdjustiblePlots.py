import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

memory = []

def drawButtonAction(a, b, canvas,Type):
    if (a == ""or b == ""):
        print("Please select a number")
        return
    a_num = float(a)
    b_num = float(b)
    memory.append((a_num,b_num))
    display(canvas,Type)

def display(canvas,type):

    # canvas.delete()
    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)
    x_max = 100
    x = np.linspace(-x_max, x_max, 200)
    y_max = 0

    print("Start drawing")
    a,b = 0,0
    for points in memory:
        a, b = points
        y = type
        mask = (x >= -x_max) & (x <= x_max) & (y >= -x_max) & (y <= x_max)
        x_fil = x[mask]
        y_fil = y[mask]

        max_y=100
        y_max = max_y
        ax.plot(x_fil, y_fil)
        # print(a, b)
    # ax.legend()  # Add a legend for clarity
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    plt.gca().set_aspect('equal', adjustable='box')
    ax.grid(color='gray', linestyle='-', linewidth=0.5)
    ax.set_title("Y = A * X + B")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.axhline(y=0, color='black', linewidth=1)  # X-axis
    ax.axvline(x=0, color='black', linewidth=1)  # Y-axis
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    arrow_x = patches.FancyArrowPatch((0, 0), (x_max+1, 0), mutation_scale=15, color='black', arrowstyle="->")
    arrow_y = patches.FancyArrowPatch((0, 0), (0, y_max), mutation_scale=15, color='black', arrowstyle="->")
    # Add the arrows to the plot
    ax.add_patch(arrow_x)
    ax.add_patch(arrow_y)

    ax.text(x_max-10, 10, 'X', fontsize=16, verticalalignment='center', horizontalalignment='left')
    ax.text(10, y_max-15, 'Y', fontsize=16, verticalalignment='bottom', horizontalalignment='center')

    for widget in canvas.winfo_children():
        widget.destroy()

    canvas_plot = FigureCanvasTkAgg(fig, master=canvas)
    canvas_plot.draw()

    # Pack the canvas plot inside the Tkinter canvas
    canvas_plot.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def clear(canvas):
    length = len(memory)
    if length == 0:
        print("there is nothing to clear")
        return
    memory.clear()
    display(canvas)

def mainWindow():

    root = tk.Tk()
    root.title("Function Graphic")

    # Create a PanedWindow (this will divide the window into two parts)
    paned_window = tk.PanedWindow(root, orient="horizontal")
    paned_window.pack(fill="both", expand=True)

    # Left part (150px wide), this will hold the Entry and Button widgets
    left_frame = tk.Frame(paned_window, width=150, bg="lightblue",padx= 30,pady= 30)  # Added padx for space on the left side
    left_frame.pack(fill="both", expand=True)

    # Right part (750px wide), this will hold the Canvas
    right_frame = tk.Frame(paned_window, width=750, bg="lightgray",padx= 30,pady= 30)
    right_frame.pack(fill="both", expand=True)

    # Add the left frame and right frame to the paned window
    paned_window.add(left_frame)
    paned_window.add(right_frame)
    # Create a Canvas in the right part
    canvas = tk.Canvas(right_frame, bg="lightblue" )
    canvas.pack(fill="both",expand= True)

    a_label = tk.Label(left_frame,text="A: ", font=("Arial", 16), bg= "lightblue")
    a_label.pack(pady=5)
    # Create two Entry widgets in the left part

    a_options = [i for i in range(-10, 11)]
    a_dropdown = ttk.Combobox(left_frame, values= a_options, state="readonly",justify="center",font=("Arial", 12))
    a_dropdown.pack(pady=20)


    b_label = tk.Label(left_frame,text="B: ", font=("Arial", 16), bg= "lightblue")
    b_label.pack(pady=5)

    b_options = [i*5 for i in range(-10, 11)]
    b_dropdown = ttk.Combobox(left_frame, values=b_options, state="readonly",justify="center",font=("Arial", 12))
    b_dropdown.pack(pady=20)


    label = tk.Label(left_frame, text="type of equation ", font=("Arial", 16), bg="lightblue")
    label.pack(pady=5)
    options = [()]
    Typedropdown = ttk.Combobox(left_frame, values=options, state="readonly", justify="center", font=("Arial", 12))
    Typedropdown.pack(pady=10)
    # Create two Buttons in the left part
    draw_button = tk.Button(left_frame, text="Draw" , command= lambda:drawButtonAction(a_dropdown.get(), b_dropdown.get(), canvas, Typedropdown.get()))
    draw_button.pack(pady=10)

    clear_button = tk.Button(left_frame, text="Clear", command = lambda:clear(canvas))
    clear_button.pack(pady=10)

    # Run the Tkinter main loop
    root.mainloop()


mainWindow()