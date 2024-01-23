# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    #set solution
    location = random.randint(0,(len(FIVE_LETTER_WORDS)-1))
    solution = FIVE_LETTER_WORDS[location].upper()
    print(solution)

    def enter_action(s):
        #set current row
        row = gw.get_current_row()
        
        for x in range(0, N_ROWS):
            x = 0
            letters = []
            while x < 5:
                letter = gw.get_square_letter(row, x)
                letters.append(letter)
                x = x + 1
            word = ''.join(letters)
            
            #If word exists
            if word.lower() in FIVE_LETTER_WORDS:
                for col in range(0, N_COLS):
                    #Check for correct letters
                    if solution[col] == gw.get_square_letter(row, col):
                        gw.set_square_color(row, col, CORRECT_COLOR)
                    #Check for almost correct letters
                    elif gw.get_square_letter(row, col) in solution:
                        gw.set_square_color(row, col, PRESENT_COLOR)
                    #Check for missing letters
                    else:
                        gw.set_square_color(row, col, MISSING_COLOR)
                
                #If word guessed correctly
                if solution == word.upper():
                    gw.show_message("Congrats! You did it!")                
                else:
                    #Move to next row
                    gw.set_current_row(row + 1)

            else: 
                gw.show_message('Not in word list')

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    #MILESTONE 1 
    # location = random.randint(0,(len(FIVE_LETTER_WORDS)-1))
    # word = FIVE_LETTER_WORDS[location]

    # for x in range(N_COLS):
    #     gw.set_square_letter(0,x,word[x].upper())

# Startup code

if __name__ == "__main__":
    wordle()
