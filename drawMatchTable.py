import tkinter as tk
def read_names_from_file(filename):
    """Read names from a text file, one per line."""
    with open(filename, "r") as file:
        names = [line.strip().capitalize() for line in file.readlines()]
    return names

def draw_grid(canvas, number_of_players, cell_width, cell_height, width_margin, height_margin,names):
    height, width =0, 0
    height_offset = cell_height/2
    width_offset =cell_width/2
    # j = 1
    for i in range(number_of_players+1):
        height = height_margin+cell_height*i
        width =  width_margin + cell_width*i
        canvas.create_line(width_margin,height,width_margin+number_of_players*cell_width, height, fill='black')
        canvas.create_line(width, height_margin, width, height_margin + number_of_players * cell_height, fill="black")
        if 0< i <10 :
            canvas.create_text(width_margin+width_offset, height+height_offset, text = names[i-1])
            canvas.create_text(width + width_offset,height_margin + height_offset, text = names[i-1])
    canvas.create_line(width_margin, height_margin,width,height, fill="blue")
    for i in range(1, number_of_players):
        height = height_margin+cell_height*i
        for j in range (1, number_of_players):
            width = width_margin + cell_width * j
            if i > j:
                entry = tk.Entry(canvas, justify="center", borderwidth=2, relief="solid", highlightbackground="blue",
                                 highlightcolor="green", width=10, font=("Arial", 12))
                entry.place(x= width +2, y=height + 0.5 * height_offset)
                entry.bind("<Return>", lambda event, e=entry, id=f"{i}-{j}": handle_score_entry(event,e,id))
def handle_score_entry(event, entry, id):
       score = entry.get().strip()
       if ":" not in score:
           print(f"Error Input,You need Colon :( Your Input Was {score}" )
           entry.delete(0, tk.END)
           return
       score1, score2 = score.split(":")
       if (not score1.isdigit()) or (not score2.isdigit()):
           print(f"Error Input, Numbers Only! :( Your Input Was {score}")
           entry.delete(0, tk.END)
           return

       score = (f"{score2}:{score1}")
       color = win_color if int(score1) < int(score2) else lose_color
       op_color = lose_color if color == win_color else win_color
       col, row = id.split("-")

       height = height_margin + cell_height * int(row)
       width = width_margin + cell_width * int(col)
       op_height = height_margin + cell_height * int(col)
       op_width = width_margin + cell_width * int(row)
       canvas.create_rectangle(width, height,
                               width + cell_width, height + cell_height,
                               fill=color, outline="black")
       canvas.create_rectangle(op_width, op_height,
                               op_width + cell_width, op_height + cell_height,
                               fill=op_color, outline="black")
       canvas.create_text(width + width_offset, height + height_offset, text=score, font=("Arial", 12))

if __name__ == "__main__":
    filename = "names.txt"
    names = read_names_from_file(filename)
    number_of_players = len(names)+1
    # Initialize the main Tkinter window
    root = tk.Tk()
    root.title("Badminton Score Keeper")
    # Define the size of the grid and cells
    cell_width = 100  # Size of each cell
    cell_height = 40
    width_margin = 50
    height_margin = 30
    height_offset = cell_height/2
    width_offset =cell_width/2
    win_color ="red"
    lose_color = "green"
    # Create a canvas to draw the grid
    canvas_width = number_of_players * cell_width + width_margin*2
    canvas_height = number_of_players * cell_height + height_margin*2
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()
    draw_grid(canvas, number_of_players, cell_width, cell_height, width_margin, height_margin, names)
    root.mainloop()
