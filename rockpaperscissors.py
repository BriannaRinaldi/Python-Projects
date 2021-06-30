import random
options = ("scissors", "paper", "rock")
user_score = 0
comp_score = 0
user_choice = ""

input("""Would you like to play Rock, Paper, Scissors? Press Enter to start. """)

while user_choice != "end":
    user_choice = input("Enter rock, paper, or scissors: ")
    comp_choice = random.choice(options)
    if user_choice not in options:
        print("Oops! That's not a valid entry. Please try again.")
        break
    result = options.index(user_choice)-options.index(comp_choice)
    if result == 0:
        print("You both chose {}. It's a draw!".format(user_choice))
    else:
        print("You chose {} and the computer chose {}.".format(user_choice, comp_choice))
        if result == 2 or result == -1:   # user win conditions will always evaluate to 2 or -1
            print("You won!")
            user_score += 1
            comp_score -= 1
        else:
            print("You lost.")
            user_score -= 1
            comp_score += 1
    user_choice = input("""Your score: {}
Computer score: {}
Press Enter to continue or type "end" to end the game. """.format(user_score, comp_score))

else:
    print("Final score:\nYou:      {}\nComputer: {}\nGood game!".format(user_score, comp_score))
