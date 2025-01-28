import tkinter as tk

root = tk.Tk()
root.title("Mixed Orientation Frames")

# Create a main frame to hold the left frame and a right sub-frame
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Create the left frame
left_frame = tk.Frame(main_frame, bg="lightblue")
left_frame.pack(side="right", fill="y", expand=True)

# Create a right frame to hold the upper and lower frames
right_frame = tk.Frame(main_frame)
right_frame.pack(side="left", fill="both", expand=True)

# Create the upper frame inside the right frame
upper_frame = tk.Frame(right_frame, bg="lightgreen", height=150)
upper_frame.pack(fill="both", expand=True)

# Create the lower frame inside the right frame
lower_frame = tk.Frame(right_frame, bg="lightgray", height=150)
lower_frame.pack(fill="both", expand=True)

# Adding content to frames (optional)
tk.Label(left_frame, text="Left Frame").pack(pady=20)
tk.Label(upper_frame, text="Upper Frame").pack(pady=20)
tk.Label(lower_frame, text="Lower Frame").pack(pady=20)

root.mainloop()
