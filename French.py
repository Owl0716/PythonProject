import random
import tkinter as tk
test_number = 0
testtype = 0
score = 0

def read_and_split_file(file_path):
    try:
        with open(file_path, 'r') as file:
            english_list = []
            french_list = []

            # Read the file line by line
            for line in file:
                # Split each line by the semicolon
                english, french = line.strip().split(';')
                english_list.append(english)
                french_list.append(french)

            return english_list, french_list
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return [], []
def handle_text_entry(textbox, result_label,english_list,french_list, word_label, score_label):
    global  test_number
    global testtype
    global score

    first_digit = int(str(score)[0])
    exam_size = len(english_list)
    text= textbox.get().strip()
    if(testtype == 1):
        answer = english_list[test_number]
    else:answer = french_list[test_number]


    if text == answer:
        result_text = "You are correct"
        bg_color="green"
        random_number(exam_size,french_list,word_label,english_list)
        score += 10 - first_digit
    else:
        result_text = f"You are incorrect"
        bg_color="red"
        score -= first_digit

    result_label.config(text = result_text, bg = bg_color)
    score_label.config(text= f"Score:{score}")
    textbox.delete(0, tk.END)





def createWindows(root_frame,english_list,french_list):
    # Create a PanedWindow (this will divide the window into two parts)
    main_window = tk.PanedWindow(root_frame, orient="vertical", width=500)
    main_window.pack(fill="both", expand=True)

    # Left part (150px wide), this will hold the Entry and Button widgets
    word_frame = tk.Frame(main_window, height=150, bg="lightblue", padx=30,
                          pady=30)  # Added padx for space on the left side
    word_frame.pack(fill="both", expand=True)
    word_label = tk.Label(word_frame, text="", font=("Arial", 48), bg="lightblue")
    word_label.pack(pady=5)
    score_label = tk.Label(word_frame, text=f"score{0}", font=("Arial", 48), bg="lightblue")
    score_label.pack(pady=5)
    # Right part (750px wide), this will hold the Canvas
    entry_frame = tk.Frame(main_window, height=150, bg="lightgray", padx=30, pady=30)
    entry_frame.pack(fill="both", expand=True)

    text_box = tk.Entry(entry_frame, justify="center", borderwidth=2, relief="solid",
                        highlightbackground="blue", highlightcolor="green", width=10, font=("Arial", 12))
    text_box.pack(fill="both", expand=True)

    result_frame = tk.Frame(main_window, height=150, bg="lightblue", padx=30, pady=30)
    result_frame.pack(fill="both", expand=True)
    result_label = tk.Label(result_frame, text="", font=("Arial", 32), bg="lightblue")
    result_label.pack(pady=5)
    give_up_button = tk.Button(result_frame, text="Don't Know",command = lambda: answer(word_label,english_list, result_label,french_list,score_label))
    give_up_button.pack()
    text_box.bind("<Return>", lambda e: handle_text_entry(text_box, result_label, english_list,french_list,word_label,score_label))
    return word_label

def answer(word_label,english_list,result,french,score_label,):
    global test_number
    global  score
    if (testtype == 1):
        result.config(text = "The correct answer was: "+english_list[test_number], bg = "gray")
    else:
        result.config(text = "The correct answer was: "+french[test_number], bg = "gray")
    first_digit = int(str(score)[0])
    score -= first_digit
    score_label.config(text = f"Score:{score}")
    random_number(len(english_list),french,word_label,english_list)

def random_number(exam_size,french_list,word_label,english_list):
    global  test_number
    global  testtype
    random_number = random.randint(0, exam_size - 1)
    testtype = random.randint(1,2)
    test_number = random_number
    if(testtype == 1):
        word_label.config(text=french_list[test_number])
    else: word_label.config(text=english_list[test_number])

def main():
    # read exam file
    english_list, french_list = read_and_split_file("French.txt")
    exam_size = len(french_list)
    # create a windows
    root = tk.Tk()
    root.title("Function Graphic")
    root.geometry("1000x600")
    word_label= createWindows(root,english_list,french_list)
    # create the exam
    random_number(exam_size,french_list,word_label,english_list)

    root.mainloop()
if __name__ == "__main__":
    main()
