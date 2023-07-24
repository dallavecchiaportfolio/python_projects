from random import shuffle, choice

output = []
tries = 10

print("\nI'm thinking of a 3-digit number. Try to guess what it is. \nHere are some clues: ")
print("\nWhen I say:\tThat means:")
print("PICO:\t\tOne digit is correct but in the wrong position.")
print("FERMI:\t\tOne digit is correct and in the right position.")
print("BAGELS:\t\tNo digit is correct.")

initialList = [0,1,2,3,4,5,6,7,8,9]
finalList = []

for i in range(3):
    itemTemp = choice(initialList)
    finalList.append(itemTemp)
    initialList.remove(itemTemp)

number2guess = ''.join(str(elem) for elem in finalList) #CONVERT LIST TO STRING FOR COMPARISON

while True:

    strPLayerGuess = input("\nEnter your guess: ")

    if strPLayerGuess == number2guess:
        print("Well done, you get it right!")
        break
    else:
        for x in range(3):
            if strPLayerGuess[x] in number2guess:
                if strPLayerGuess[x] == number2guess[x]:
                    output.append("FERMI")
                else:
                    output.append("PICO ")

    if len(output) > 0:
        print(shuffle(output)) # SHUFFLE TO GIVE LESS CLUES WHERE IS THE CORRECT/UNCORRECT POSITION
    else:
        print("BAGELS")

    output = ""

    tries = tries - 1

    if tries >= 2:
        print("Try again - {} tries left.".format(tries))
    elif tries == 1:
        print(("Try again - 1 try left."))
    else: 
        print("The number to guess was {}.".format(number2guess))