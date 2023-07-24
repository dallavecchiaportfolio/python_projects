from random import sample, shuffle

digits = 3
guesses = 10

print("I'm thinking of a {}-digits number.".format(digits))
print("Try to guess what it is.")
print("Here are some clues: ")
print("\nWhen I say:\tThat means:")
print("PICO:\t\tOne digit is correct but in the wrong position.")
print("FERMI:\t\tOne digit is correct and in the right position.")
print("BAGELS:\t\tNo digit is correct.")
print("There are no repeated digit in the number.")

tmpNumber = sample('0123456789', digits)

if tmpNumber[0] == '0': # IF ZERO IS THE FIRST NUMBER IN THE LIST CHANGE THE ORDER OF THE LIST: IF 012 CHANGES TO 210
    tmpNumber.reverse()

numberToGuess = ''.join(tmpNumber) # Convert List to String

print("\nI have thought up a number.")
print("You have {} guesses to get it.".format(guesses))

counter = 1

while True:
    
    print("\nGuess #{}".format(counter))
    guess = input()

    if guess == numberToGuess:
        print("You got it - {}!".format(guess))
        break

    clues = []

    for index in range(digits):
        if guess[index] == numberToGuess[index]:
            clues.append("FERMI")
        elif guess[index] in numberToGuess:
            clues.append("PICO")

    shuffle(clues)

    if len(clues) == 0:
        print("BAGELS")
    else:
        print(' '.join(clues))

    counter += 1

    if counter > guesses:
        print("You ran out of guesses. The number to guess was {}".format(numberToGuess))
        break