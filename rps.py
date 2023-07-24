# ****************************************************
#
#   ROCK-PAPER-SCISSORS GAME
#   CREATED BASED ON THE YOUTUBE VIDEO BY FREECODECAMP
#   https://youtu.be/eWRfhZUzrAc
#
# ****************************************************

import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_winner(player, computer):
    print("You chose {}, computer chose {}.".format(player, computer))
    if player == computer:
        return "It is a TIE!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smases scissors! You win!"
        else:
            return "Paper envolves rock! You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper! You win!"
        else:
            return "Rock smashes scissors! You lose!"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cut paper! You lose!"
        else:
            return "Paper envolves rock! You win!"
    
choices = get_choices()
result = check_winner(choices["player"], choices["computer"])
print(result)