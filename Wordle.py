# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

LRandomWord = []

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    gw.set_square_letter


    gw.set_square_letter
    gw.get_square_letter

    def randomWord():
        sRandomWord = random.choice(FIVE_LETTER_WORDS)
        for letter in sRandomWord:
            if letter.strip() != '':
                LRandomWord.append(letter)
        # print(LRandomWord)
        # print(sRandomWord)
        # print(LRandomWord[0])
    
    randomWord()
    
    for c in range(N_COLS):
        gw.set_square_letter(0, c, LRandomWord[c])
    

# Startup code

if __name__ == "__main__":
    wordle()