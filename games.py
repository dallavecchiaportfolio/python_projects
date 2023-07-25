import platform

# MAIN SCREEN TO SELECT WHICH GAME TO PLAY
print("Welcome to my selections of games.")
print("Enter the number of the game as shows below: ")
print("(1) Guess Number\nGame where ou have 10 tries to guess the number that the computer choses.")
print("(2) Greater/Lower\nGame where you have clues if the entered number is greater or lower as the computer choses.")
print("(3) The famous Rock/Paper/Scissors game. You going to play against the computer.")

# SET THE PATH ACCORDING THE OS - Windows, Linux or macOS
 
which_os = platform.system()
set_path = ""

match which_os:
    case "Windows":
        set_path = "C:\\Users\\dalla\\Documents\\python_projects\\"
    case "Linux":
        set_path = "/home/gio/Documents/python_projects"
    case "Darwin":
        # macBook Pro
        set_path = "/Users/pro/Dcouments/python_projects"
        # macBook Air
    case _:
        print("Cannot set the path, OS not identified!")

gameChosed = input("\nWhich game would you like to play? ")

match gameChosed:
    case "1":
        print("You want to play Guess Number")
        exec(open(set_path + "guessNumber.py").read())
    case "2":
        print("You want to play Lower/Greater")
        exec(open(set_path + "greaterLowerv1.py").read())
    case "3":
        print("You want to play Rock/Paper/Scissors")
        exec(open(set_path + "rps.py").read())
    case _:
        print("Can see you are not in a mood today! Bye Bye")