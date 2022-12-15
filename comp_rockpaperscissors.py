"""Rock, Paper, Scissors game!"""
import getpass
import random


def rps():
    """Rock Paper Scissors function to stop pylint from throwing errors"""
    valid_options = [1, 2, 3]
    valid_choice = False
    while not valid_choice:
        user_choice = int(getpass.getpass("Player: Rock = 1 / Paper = 2 / Scissors = 3"))
        if user_choice in valid_options:
            valid_choice = True
        else:
            print("Invalid option. Please try again")

    if user_choice == 1:
        user_choice = "Rock"
    elif user_choice == 2:
        user_choice = "Paper"
    elif user_choice == 3:
        user_choice = "Scissors"

    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    print("")
    print(f"Player: {user_choice}")
    print(f"Computer: {computer_choice}")
    print("")

    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif ((computer_choice == "Rock" and user_choice == "Paper")
            or (computer_choice == "Paper" and user_choice == "Scissors")
            or (computer_choice == "Scissors" and user_choice == "Rock")):
        print("Player wins!")
    else:
        print("Computer wins!")


rps()
