# -*- coding: utf-8 -*-
import random



#word_list = ["ardvark","camal","mango"]
from hangman_words import word_list 
chosen_word = random.choice(word_list)

end_of_game = False
lives = 6

from hangman_art import logo,stages  
print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_len = len(chosen_word)

for _ in range(word_len):
    display += "_"
print(display)



while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You already guessed {guess}")
    
    for position in range(word_len):
        letter = chosen_word[position]
       # print(f"Current position: {position}\nCurrent letter: {letter}\n Guessed letter:{guess}n") 
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guess {guess}, that's not in the word, You loose a live")
        lives -= 1
        if lives == 0:
            end_of_game == True
            print("You Lose")
   
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("********* You Win**********")
        
    print(stages[lives])    
        
        
        
        
        
        
        
        