# Pig (Dice Gane)

import random

def rollDice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    Players = input("Enter the number of players ( 2 - 4 ) : ")
    if Players.isdigit():
        Players = int(Players)
        if 2 <= Players <= 4:
            break
        else:
            print("Invalid number of players. Try again.")
    else:
        print("Invalid input. Try again.")

print("The game will have", Players, "players")

max_score = int(input("Enter the winning score ( 10 - 50 ) : "))
player_scores = [0 for _ in range(Players)]

while max(player_scores) < max_score:
    for player_idx in range(Players):
        print("Player number ", player_idx + 1, " turn has started.")
        print("Your total score is: ", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Press enter to roll the dice or 'q' to quit : ")
            if should_roll.lower() == 'q':
                break

            roll_value = rollDice()
            if roll_value == 1:
                print("You rolled a 1. You lost your points and your turn.")
                current_score = 0
                break
            else:
                current_score += roll_value
                print("You rolled a: ", roll_value)

            print("Your current score is: ", current_score)

        player_scores[player_idx] += current_score
        print("Your final score is: ", player_scores[player_idx], "\n")

max_player_score = max(player_scores)
winning_idx = player_scores.index(max_player_score) + 1
print("Player number ", winning_idx, " has won the game with ", max_player_score, " points.")