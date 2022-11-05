guess = input('Enter a single letter ')
print(f'Your letter is {guess}')

if len(guess)==1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
