# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
import tkinter as tk

def wordle():
    def toggle_mode():
        nonlocal CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
        if mode_button.cget("text") == "Switch to Colorblind Mode":
            CORRECT_COLOR = "#AAAAAA"  # Change these values for Colorblind Mode
            PRESENT_COLOR = "#BBBBBB"
            MISSING_COLOR = "#CCCCCC"
            mode_button.config(text="Switch to Regular Mode")
        else:
            CORRECT_COLOR = "#228833"  # Reset to original values for Regular Mode
            PRESENT_COLOR = "#CCBB44"
            MISSING_COLOR = "#999999"
            mode_button.config(text="Switch to Colorblind Mode")

    def enter_action(s):
        row = gw.get_current_row()

        for x in range(0, N_ROWS):
            x = 0
            letters = []
            while x < 5:
                letter = gw.get_square_letter(row, x)
                letters.append(letter)
                x = x + 1
            word = ''.join(letters)

            if word.lower() in FIVE_LETTER_WORDS:
                for col in range(0, N_COLS):
                    if solution[col] == gw.get_square_letter(row, col):
                        gw.set_square_color(row, col, CORRECT_COLOR)
                    elif gw.get_square_letter(row, col) in solution:
                        gw.set_square_color(row, col, PRESENT_COLOR)
                    else:
                        gw.set_square_color(row, col, MISSING_COLOR)

                if solution == word.upper():
                    gw.show_message("Congrats! You did it!")
                else:
                    gw.set_current_row(row + 1)
            else:
                gw.show_message('Not in word list')

    root = tk.Tk()
    top = tk.Toplevel(root)
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    mode_button = tk.Button(root, text="Switch to Colorblind Mode", command=toggle_mode)
    mode_button.grid(row=N_ROWS + 1, columnspan=N_COLS)  # Adjust the grid position as needed

    location = random.randint(0, (len(FIVE_LETTER_WORDS) - 1))
    solution = FIVE_LETTER_WORDS[location].upper()

    CORRECT_COLOR = "#228833"
    PRESENT_COLOR = "#CCBB44"
    MISSING_COLOR = "#999999"

    root.mainloop()

# Startup code

if __name__ == "__main__":
    wordle()

