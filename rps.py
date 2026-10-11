#python liabraries are useful because we dont have to write the code from scratch and we get access to many more features
import random

def get_choices():
    option = ["rock", "paper", "scissors"]

    player_choice = input("Enter a choice ( rock, paper, scissors)")
    computer_choice = random.choice(option)
    #dictionaries in python are used to stored data in key-value pairs
    choices ={"player" : player_choice, "computer": computer_choice}
    return choices

def check_win(player,computer):
    print(f"You chose {player} and computer chose {computer}")
    if player==computer:
        print ("Its a tie")
    elif player=='rock':
        if  computer=='paper':
            print("Computer wins")
        else:
            print("Player wins")
    elif player=='paper':
        if computer=='scissors':
            print("Computer wins")
        else:
            print("Player wins")
    elif player=='scissors':
        if computer=='paper':
            print("Player wins")
        else:
           print("Computer wins")

check_win('rock', 'scissors')
