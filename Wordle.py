# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from pydantic import MissingError

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR, WordleGWindow, N_COLS, N_ROWS

LRandomWord = []
iRow = 0
sRandomWord = ""

def wordle():

    def enter_action(s):
        global iRow
        global sRandomWord
        global LRandomWord
        sInWordList = "no"
        sGuessedWord = s.upper()
        LGuessedWord = []

        def changeWordleSquare(LRandomWord):
            print("Hello " + str(LRandomWord))

            for i in range(len(LGuessedWord)):
                if LGuessedWord[i].upper() == LRandomWord[i].upper():
                    gw.set_square_color(iRow, i, CORRECT_COLOR) 
                elif LGuessedWord[i].upper() in sRandomWord.upper() :  
                    gw.set_square_color(iRow, i, PRESENT_COLOR)
                else:
                    gw.set_square_color(iRow, i, MISSING_COLOR)

        for letter in sGuessedWord:
            if letter.strip() != '':
                LGuessedWord.append(letter.upper())

        if iRow == N_ROWS - 1:
            changeWordleSquare(LRandomWord)
            gw.show_message("Sorry champ you ran out of guesses...")
        elif sRandomWord.upper() == sGuessedWord:
            changeWordleSquare(LRandomWord)
            gw.show_message("YOU GOT IT BUDDY!!!")
        else:
            for i in range(len(FIVE_LETTER_WORDS)):
                if FIVE_LETTER_WORDS[i].upper() == sGuessedWord:
                    sInWordList = "yes"
        
            if sInWordList == "yes":
                gw.show_message("That is a valid word!")
                changeWordleSquare(LRandomWord)

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
    
    randomWord()

    for c in range(N_COLS):
        gw.set_square_letter(0, c, LRandomWord[c])
  

# Startup code

if __name__ == "__main__":
    wordle()