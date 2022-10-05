# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

LRandomWord = []
iRow = 0
sRandomWord = ""

def wordle():

    def enter_action(s):
        global iRow
        global sRandomWord
        sInWordList = "no"
        sGuessedWord = s.upper()
        LGuessedWord = []

        for letter in sGuessedWord:
            if letter.strip() != '':
                LGuessedWord.append(letter.upper())

        if iRow == N_ROWS - 1:
            gw.show_message("Sorry champ you ran out of guesses...")
        elif sRandomWord.upper() == sGuessedWord:
            gw.show_message("YOU GOT IT BUDDY!!!")
        else:
            for i in range(len(FIVE_LETTER_WORDS)):
                if FIVE_LETTER_WORDS[i].upper() == sGuessedWord:
                    sInWordList = "yes"
        
            if sInWordList == "yes":
                gw.show_message("That is a valid word!")
                iRow += 1
            else:
                gw.show_message("Not in word list.")

            gw.set_current_row(iRow)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    gw.set_square_letter
    gw.get_square_letter
    gw.get_current_row
    gw.set_current_row(iRow)

    def randomWord():
        global sRandomWord
        sRandomWord = random.choice(FIVE_LETTER_WORDS)
        for letter in sRandomWord:
            if letter.strip() != '':
                LRandomWord.append(letter.upper())

        print(LRandomWord)
        print(sRandomWord)
        print(LRandomWord[0])
    
    randomWord()

    for c in range(N_COLS):
        gw.set_square_letter(0, c, LRandomWord[c])
  

# Startup code

if __name__ == "__main__":
    wordle()