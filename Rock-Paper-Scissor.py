# Python Random Module
import random

# Intro
print("Rock, Paper, Scissors...")

# Main Function
def try_again():
  # Random Choice (Rock, Paper, or Scissors)
    R_P_S = ["Rock", "Paper", "Scissors"]
    computer = random.choice(R_P_S)

  # Player's choice
    player = input("your choice: ").lower().capitalize()

  # If the program chose rock
    if computer == "Rock":
    	# If the player chose rock
        if player == "Rock":
            print(f"I chose {computer}, you chose {player}\nit's a tie!\n\n")
        # If the player chose paper
        elif player == "Paper":
            print(f"I chose {computer}, you chose {player}\nYou won!\n\n")
        # If the player chose scissors
        elif player == "Scissors":
            print(f"I chose {computer}, you chose {player}\nI won!\n\n")

  # If the program chose paper
    elif computer == "Paper":
    	# If the player chose rock
        if player == "Rock":
            print(f"I chose {computer}, you chose {player}\nI won!\n\n")
        # If the player chose paper
        elif player == "Paper":
            print(f"I chose {computer}, you chose {player}\nIt's a tie!\n\n")
        # If the player chose scissors
        elif player == "Scissors":
            print(f"I chose {computer}, you chose {player}\nYou won!\n\n")

  # If the program chose scissors
    elif computer == "Scissors":
    	# If the player chose rock
        if player == "Rock":
            print(f"I chose {computer}, you chose {player}\nYou won!\n\n")
        # If the player chose paper
        elif player == "Paper":
            print(f"I chose {computer}, you chose {player}\nI won!\n\n")
        # If the player chose scissors
        elif player == "Scissors":
            print(f"I chose {computer}, you chose {player}\nIt's a tie\n\n")

    try_again()

# End of function
try_again()
