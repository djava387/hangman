## Milestone 2: Gama Variables
The  code creates a guessing game where the user has to input a letter. If the letter is valid, the code will print "Good guess!". Otherwise, it will print "Oops! That is not a valid input."

 Assigning input to variable
~~~      
guess = input('Enter a single letter')
print(f'Your letter is {guess}')
 ~~~       

checks  the length of the character using len() and passing guess variable. It also check if the character is an alphabet with isalpha method
~~~
if len(guess)==1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
~~~

## Milestone 3: functions for the game
### check_guess()
The game checks if the letter from the user is in a word that is randomly chosen. The randomly generated word is from an external package (random-word) that is installed and importing RandomWords(). In orader to fetch the word, .get_random_word() is used. 
~~~
pip install random-word
~~~


~~~
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
~~~
### ask_for_input()
 Iteratively checks if the input is a valid guess by using condtional checks that are passed before the input can be accepted
 ~~~
 def ask_for_input():
     while True:
            
     # print(f'Your letter is {guess}')
      if len(guess)==1 and guess.isalpha():
       break
      else:
         print('Invalid letter. Please, enter a single alphabetical character.')
         check_guess(guess)
ask_for_input()
 ~~~