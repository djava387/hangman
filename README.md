## Milestone 2
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
        