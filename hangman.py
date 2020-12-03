# -*- coding: utf-8 -*-
import random

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



word_list = ["ardvark","camal","mango"]
chosen_word = random.choice(word_list)

lives = 6

print(f'Pssst, the solution is {chosen_word}.')

display = []
word_len = len(chosen_word)

for _ in range(word_len):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    for position in range(word_len):
        letter = chosen_word[position]
       # print(f"Current position: {position}\nCurrent letter: {letter}\n Guessed letter:{guess}n") 
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game == True
            print("You Lose")
   
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("********* You Win**********")
        
    print(stages[lives])    
        
        
        
        
        
        
        
        