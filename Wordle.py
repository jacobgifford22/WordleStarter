# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

# from pydantic import MissingError

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

        # Updates squares to the correct color
        def changeWordleSquare(LRandomWord):

            # Sets a count of each letter in a word
            def setLetterDictionary(LWord):
                DLetters = {}
                
                for letter in LWord:
                    if letter in DLetters:
                        DLetters.update({letter: DLetters[letter] + 1})
                    else:
                        DLetters.update({letter: 1})
                
                return DLetters

            # Sets each letter in word with a count of 0
            def setZeroDictionary(LWord):
                DLetters = {}

                for letter in LWord:
                    DLetters.update({letter: 0})

                return DLetters

            # Dictionaries for the counts of each letter in guess and random word
            DGuessLetters = setLetterDictionary(LGuessedWord)
            DRandomLetters = setLetterDictionary(LRandomWord)

            # Dictionaries for correct letters and present letters (initializes count to 0)
            DCorrectLetters = setZeroDictionary(LRandomWord)
            # DPresentLetters = setZeroDictionary(LRandomWord)

            for i in range(len(LGuessedWord)):
                # If guessed letter is in correct square
                if LGuessedWord[i] == LRandomWord[i]:
                    gw.set_square_color(iRow, i, CORRECT_COLOR)
                    DCorrectLetters.update({LRandomWord[i]: DCorrectLetters[LRandomWord[i]] + 1})
                    gw.set_key_color(LGuessedWord[i], CORRECT_COLOR)

                else:
                    # If guessed letter is in word, but not correct square
                    if LGuessedWord[i] in LRandomWord:
                        # If duplicate guessed letter and correct letter is all green
                        if DRandomLetters[LGuessedWord[i]] == DCorrectLetters[LGuessedWord[i]]:
                            gw.set_square_color(iRow, i, MISSING_COLOR) 
                        # If duplicate guessed letter and correct letter is not all green
                        elif DRandomLetters[LGuessedWord[i]] > DCorrectLetters[LGuessedWord[i]]:
                            gw.set_square_color(iRow, i, PRESENT_COLOR)
                            gw.set_key_color(LGuessedWord[i], PRESENT_COLOR)
                            DCorrectLetters.update({LGuessedWord[i]: DCorrectLetters[LGuessedWord[i]] + 1})
                    # If guessed letter isn't in word
                    else:
                        gw.set_square_color(iRow, i, MISSING_COLOR)
                        gw.set_key_color(LGuessedWord[i], MISSING_COLOR)

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