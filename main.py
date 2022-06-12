import random
print("Welcome to Rock, Paper, Scissors Game!")
print(" R stands for Rock, \n P stands for Paper, \n S stands for Scissors")
while True:
    #Create possible options to generate computer and player outcomes 
    possible_options = ["R", "P", "S"]
    computer_choice = random.choice(possible_options)
    #create a validation loop for player input
    while True:
        player_choice = input("Pick an option from R, P and S \n Player_choice: ").upper()
        if player_choice == "R" or player_choice=="P" or player_choice=="S":
           break
        else:
            print("Invalid entry, please try again!")
    #Check possible computer and player moves, and print result
    if player_choice == "R" and computer_choice == "P":
        print("Player", (player_choice), ": CPU", (computer_choice))
        print("Sorry! You lost! Paper covers Rock")
    elif player_choice == "R" and computer_choice == "S":
        print("Player", (player_choice), ": CPU", (computer_choice))      
        print("Congrats! You win! Rock smashes Scissors")
    elif player_choice == "P" and computer_choice == "S":
        print("Player", (player_choice), ": CPU", (computer_choice))      
        print("Sorry! You lost! Scissors cuts Paper")
    elif player_choice == "P" and computer_choice == "R":
        print("Player", (player_choice), ": CPU", (computer_choice))      
        print("Congrats! You win! Paper covers Rock")    
    elif player_choice == "S" and computer_choice == "P":
        print("Player", (player_choice), ": CPU", (computer_choice))      
        print("Congrats! You win Scissors cuts Paper!")
    elif player_choice == "S" and computer_choice == "R":
        print("Player", (player_choice), ": CPU", (computer_choice))      
        print("Sorry! You lost!, Rock smashes Scissors")
    else:
        print("Player", (player_choice), ": CPU", (computer_choice))
        print("Its a Tie, play again!")
    if player_choice != computer_choice:
        break
print("Game Over!")
