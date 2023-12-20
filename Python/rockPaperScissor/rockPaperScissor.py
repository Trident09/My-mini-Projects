import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input in ["quit", "q"]:
        break
    if user_input not in options:
        print("Please enter a valid input.")
        continue
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    if (
        (user_input == "rock" and computer_pick == "scissors")
        or (user_input == "paper" and computer_pick == "rock")
        or (user_input == "scissors" and computer_pick == "paper")
    ):
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a tie!")
    else:
        print("You lost!")
        computer_wins += 1
        continue

total_games = user_wins + computer_wins
print("You won", user_wins, "times out of ", total_games, "games.")
print("Goodbye!")
