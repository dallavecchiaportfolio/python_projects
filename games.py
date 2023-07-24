# MAIN SCREEN TO SELECT WHICH GAME TO PLAY
print("Welcome to my selections of games.")
print("Enter the number of the game as shows below: ")
print("(1) Guess Number\nGame where ou have 10 tries to guess the number that the computer choses.")
print("(2) Greater/Lower\nGame where you have clues if the entered number is greater or lower as the computer choses.")
print("(3) The famous Rock/Paper/Scissors game. You going to play against the computer.")

gameChosed = input("\nWhich game would you like to play? ")

if gameChosed == '1':
    print("You want to play Guess Number")
    exec(open("/home/gio/Documents/projects/python/guessNumberv1.py").read())
elif gameChosed == '2':
    print("You want to play Lower/Greater")
    exec(open("/home/gio/Documents/projects/python/greaterLowerv1.py").read())
elif gameChosed == '3':
    print("You want to play Rock/Paper/Scissors")
    exec(open("/home/gio/Documents/projects/python/rps.py").read())
else:
    print("Can see you are not in a mood today! Bye Bye")