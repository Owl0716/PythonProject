import random
import tkinter as tk

test_number = 0
test_type = 0
score = 0
mode = 2
answer = 0

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


def handle_text_entry(textbox, result_label, english_list, french_list, word_label, score_label):
    global test_number
    global test_type
    global score
    global answer
    first_digit = int(str(score)[0])
    exam_size = len(english_list)

    if test_type == 1:
        answer = english_list[test_number]
    else:
        answer = french_list[test_number]
    print(answer)

    text = textbox.get().strip()
    if text == answer:
        result_text = "Correct!!! Move On"
        bg_color = "green"
        next_question(french_list, word_label, english_list)
        score += 10 - first_digit
    else:
        result_text = f"Wrong! The answer is {answer}"
        bg_color = "red"
        score -= first_digit
    result_label.config(text=result_text, bg=bg_color)
    score_label.config(text=score)
    textbox.delete(0, tk.END)

def createWindows(root_frame, english_list, french_list):
    main_frame = tk.Frame(root_frame)
    main_frame.pack(fill="both", expand=True)
    # Create a PanedWindow (this will divide the window into two parts)
    left_window = tk.PanedWindow(main_frame, orient="vertical", width=500)
    left_window.pack(fill="both", expand=True, side="left")
    # Left part (150px wide), this will hold the Entry and Button widgets
    word_frame = tk.Frame(left_window, height=150, bg="lightblue", width=150)
    word_frame.pack(fill="both", expand=True)
    word_label = tk.Label(word_frame, text="", font=("Arial", 48), bg="lightblue")
    word_label.pack(pady=5)

    # result_frame
    result_frame = tk.Frame(left_window, height=150, bg="lightblue", width=150)
    result_frame.pack(fill="both", expand=True)

    # result_label
    result_label = tk.Label(result_frame, text="", font=("Arial", 32), bg="lightblue")
    result_label.pack(pady=5)

    # give up button
    give_up_button = tk.Button(result_frame, text="Don't Know", font=("Arial", 16),
                               command=lambda: give_up(word_label, english_list, result_label, french_list, score_label))
    give_up_button.pack()

    # entry_frame
    entry_frame = tk.Frame(left_window, height=150, bg="lightblue", width=150)
    entry_frame.pack(fill="both", expand=True)

    # text_box
    text_box = tk.Entry(entry_frame, justify="center", borderwidth=2, relief="solid",
                        highlightbackground="blue", highlightcolor="green", width=15, font=("Arial", 32))
    text_box.pack(side="top")  # Ad
    return_button = tk.Button(result_frame, text="Next Question", font = ("Arial",16),command= lambda: handle_text_entry(text_box, result_label, english_list, french_list, word_label,
                                                          score_label))
    return_button.pack(pady = 50)

    # Right frame (this will take up 2/5 of the screen)
    right_frame = tk.Frame(main_frame, bg="lightgray", padx=30)
    right_frame.pack(side="left", fill="both")
    score_label = tk.Label(right_frame, text="0", font=("Arial", 48), bg="lightgray")
    score_label.pack(side="right", pady=10)
    other_label = tk.Label(right_frame, text="score:", font=("Arial", 48), bg="lightgray")
    other_label.pack(side="right", pady=20)
    return word_label

def give_up(word_label, english_list, result, french, score_label, ):
    global test_number
    global score
    if (test_type == 1):
        result.config(text="The correct answer was: " + english_list[test_number], bg="gray")
    else:
        result.config(text="The correct answer was: " + french[test_number], bg="gray")
    first_digit = int(str(score)[0])
    score -= first_digit
    score_label.config(text=score)
    next_question(french, word_label, english_list)

def next_question(french_list, word_label, english_list):
    global test_number
    global test_type
    exam_size = len(french_list)
    test_number = random.randint(1, exam_size - 1)
    test_type = random.randint(1, 2)

    if (test_type == 1):
        language = "(French)"
        word_label.config(text=french_list[test_number] + language)
    else:
        language = "(English)"
        word_label.config(text=english_list[test_number] + language)
def get_answer(english_list, french_list):
    global test_number
    if test_type == 1:
        answer = english_list[test_number]
    else:
        answer = french_list[test_number]
    print(test_number)
    return answer

def main():
    # read exam file
    english_list, french_list = read_and_split_file("HouseWork.txt")
    # create a windows
    root = tk.Tk()
    root.title("Function Graphic")
    root.geometry("1000x1000")

    word_label = createWindows(root, english_list, french_list)
    next_question(french_list, word_label, english_list)
    # create the exam
    root.mainloop()


if __name__ == "__main__":
    main()

#
