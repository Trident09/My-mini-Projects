name = input("What is your name? ")
print("Hello, " + name + ". Welcome to the adventure game!")

answer = input(
    "You are walking down a path and come to a fork in the road. Do you go left or right? (left/right) "
).lower()
if answer == "left":
    answer = input(
        "You come to a lake. There is something on the other side of the river. Do you swim out to the other side or go around? (swim/walk) "
    ).lower()
    if answer == "walk":
        print("You walked for many miles, ran out of water, and you lost the game.")
    elif answer == "swim":
        print("You swam into the river and were eaten by a crocodile. You lose.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge. This bridge is wobbly, Do you cross it? (yes/no) ").lower()
    if answer == "yes":
        answer = input("You crossed the bridge and found a stranger. Do you talk to them? (yes/no) ").lower()
        if answer == "yes":
            print("You talked to the stranger and they gave you a million dollars. You win!")
        elif answer == "no":
            print("You ignored the stranger and they got angry. You lose.")
        else:
            print("Not a valid option. You lose.")
    elif answer == "no":
        print("You turned around and lost the game.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print("Thank you for playing, " + name + ".")