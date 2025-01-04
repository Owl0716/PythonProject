import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

def display(a, b, canvas_plot):
    global fig, ax
    if not fig:
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
    a_num = float(a)
    b_num = float(b)

    x = np.linspace(-10, 10, 100)  # 100 points from -10 to 10
    # Calculate the corresponding y values for the equation y = x + 1
    y = a_num*x + b_num
    ax.plot(x,y)

    canvas_plot.draw()
    print(f"{a_num} {b_num}")

def clear(canvas_plot):
    fig.clf()
    canvas_plot.draw()

def mainWindow():
    root = tk.Tk()
    root.title("Window with Split Panels")

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

    canvas_plot = FigureCanvasTkAgg(fig, master=canvas)
    canvas_plot.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    label = tk.Label(left_frame,text="A: ", font=("Arial", 16), bg= "lightblue")
    label.pack(pady=5)
    # Create two Entry widgets in the left part
    entry1 = tk.Entry(left_frame, justify="center", font=("Arial", 12) ,)
    entry1.pack(pady=20)

    label = tk.Label(left_frame,text="B: ", font=("Arial", 16), bg= "lightblue")
    label.pack(pady=5)
    entry2 = tk.Entry(left_frame, justify="center", font=("Arial", 12))
    entry2.pack(pady=20)

    # Create two Buttons in the left part
    button1 = tk.Button(left_frame, text="Draw" , command= lambda:display(entry1.get(), entry2.get(),canvas_plot))
    button1.pack(pady=10)

    button2 = tk.Button(left_frame, text="Clear", command = lambda:clear(canvas_plot))
    button2.pack(pady=10)

    # Run the Tkinter main loop
    root.mainloop()


mainWindow()