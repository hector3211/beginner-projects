
import random

from numpy import append
words = ["hector","nina","mia"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

hangman = """
_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
"""
print(hangman)


def get_word():
    word = random.choice(words)
    return word.upper()


def play(word):
    body_parts = 6
    letters_guessed = []
    blanks = []
    for blank in word:
        blanks += "_"
    while body_parts != 0:
        print(blanks)
        guess = input("Please enter a letter: ").upper()
        for position in range(len(word)):
            letter = word[position]
            if guess == letter:
                blanks[position] = letter
                print("\n")
        if "_" not in blanks:
            print("YOU WON!!!")
            print(blanks)
            break
        if guess in letters_guessed:
            print(f"\nyou already guessed :{guess}")
        if guess not in word:
            letters_guessed.append(guess)
            print(f"\nsorry {guess} not in word")
            body_parts -= 1
            print(stages[body_parts])
            print(f"\nyou have {body_parts},tries left ")
    if body_parts == 0:
        print("YOU LOST!!!\n")






while input("do you want to play hangman? type 'yes' or 'no:' \n") == 'yes':
    play(get_word())
