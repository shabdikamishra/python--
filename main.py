#python liabraries are useful because we dont have to write the code from scratch and we get access to many more features
import random

def get_choices():
    option = ["rock", "paper", "sciccors"]

    player_choice = input("Enter a choice ( rock, paper, sciccors)")
    computer_choice = random.choice(option)
    #dictionaries in python are used to stored data in key-value pairs
    choices ={"player" : player_choice, "computer": computer_choice}
    return choices

choices= get_choices()
print(choices)

#list is used to store multiple diff items
food = ["pizza", "carrot","eggs"]
dinner = random.choice(food)
print(dinner)