import random
import tkinter as tk
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
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

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()
