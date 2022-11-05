guess = input('Enter a single letter ')

def check_guess(guess):
    guess = guess.lower()
    return guess
from random_word import RandomWords

r = RandomWords()
new_word = r.get_random_word()

while True:
  if guess  in new_word:
    print(f'Good guess! {guess} is in the word {new_word}')
    break
  else:
    print(f'Sorry, {guess} is not in the word. Try again.')
    break

def ask_for_input():
     while True:
            
     # print(f'Your letter is {guess}')
      if len(guess)==1 and guess.isalpha():
       break
      else:
         print('Invalid letter. Please, enter a single alphabetical character.')
         check_guess(guess)
ask_for_input()



