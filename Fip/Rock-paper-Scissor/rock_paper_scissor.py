import random

# 1. Define the possible choices
choices = ["rock", "paper", "scissors"]

# 2. Get the user's choice
user_choice = input("Choose rock, paper, or scissors: ").lower()

# Check if the user's choice is valid
if user_choice not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    # 3. Generate a random choice for the computer
    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # 4. Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")

    else:
        print("Computer wins!")
