import random
import tkinter as tk
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
import tkinter as tk

def wordle():
    def toggle_mode():
        nonlocal CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
        if mode_button.cget("text") == "Switch to Colorblind Mode":
            CORRECT_COLOR = "#228833"       # Light green for correct letters
            PRESENT_COLOR = "#CCBB44"       # Brownish yellow for misplaced letters
            MISSING_COLOR = "#999999"
            mode_button.config(text="Switch to Regular Mode")
        else:
            CORRECT_COLOR = "#66BB66"  # Reset to original values for Regular Mode
            PRESENT_COLOR = "#CCBB66"
            MISSING_COLOR = "#999999"
            mode_button.config(text="Switch to Colorblind Mode")

    total_guesses = 0
    correct_guesses = 0
    incorrect_guesses = 0

    # Set solution
    location = random.randint(0, len(FIVE_LETTER_WORDS) - 1)
    solution = FIVE_LETTER_WORDS[location].upper()

    def enter_action(s):
        nonlocal total_guesses, correct_guesses, incorrect_guesses
        total_guesses += 1

        row = gw.get_current_row()
        letters = [gw.get_square_letter(row, i) for i in range(N_COLS)]
        word = ''.join(letters)

        if word.lower() in FIVE_LETTER_WORDS:
            correct_word = True
            for col in range(N_COLS):
                if solution[col] == gw.get_square_letter(row, col):
                    gw.set_square_color(row, col, CORRECT_COLOR)
                elif gw.get_square_letter(row, col) in solution:
                    gw.set_square_color(row, col, PRESENT_COLOR)
                else:
                    gw.set_square_color(row, col, MISSING_COLOR)
                    correct_word = False

            if correct_word:
                gw.show_message("Congrats! You did it!")
                correct_guesses += 1
                update_statistics()
                return
            else:
                incorrect_guesses += 1  # Increment here for whole word
                gw.set_current_row(row + 1)
        else:
            gw.show_message('Not in word list')
            incorrect_guesses += 1  # Increment here for invalid word

        update_statistics()

        if total_guesses == N_ROWS:
            update_statistics("Sorry, you didn't get it right.")

    def update_statistics(message=""):
        stats_msg = f"{message}\nTotal Guesses: {total_guesses}\nCorrect Guesses: {correct_guesses}\nIncorrect Guesses: {incorrect_guesses}"
        gw.show_message(stats_msg)

    root = tk.Tk()
    top = tk.Toplevel(root)
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    mode_button = tk.Button(root, text="Switch to Colorblind Mode", command=toggle_mode)
    mode_button.grid(row=N_ROWS + 1, columnspan=N_COLS)  # Adjust the grid position as needed

    location = random.randint(0, (len(FIVE_LETTER_WORDS) - 1))
    solution = FIVE_LETTER_WORDS[location].upper()
    print(solution)

    CORRECT_COLOR = "#66BB66"
    PRESENT_COLOR = "#CCBB66"
    MISSING_COLOR = "#999999"

    root.mainloop()

# Startup code

if __name__ == "__main__":
    wordle()

