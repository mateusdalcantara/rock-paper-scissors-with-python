import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Player pick
player_pick = int(input("Type 0 to choose rock, type 1 to choose paper, or 2 for scissors: "))
print()

# List of choices
computer_choices = [rock, paper, scissors]

# Randomly choose for the computer
computer_pick = random.choice(computer_choices)

if player_pick == 0 and computer_pick == scissors:
    print("Player wins! Rock beats scissors.\n")
    print("Player picked: ", rock)
    print("Computer picked: ", scissors)
elif player_pick == 1 and computer_pick == rock:
    print("Player wins! Paper beats rock.\n")
    print("Player picked: ", paper)
    print("Computer picked: ", rock)
elif player_pick == 2 and computer_pick == paper:
    print("Player wins! Scissors beats paper.\n")
    print("Player picked: ", scissors)
    print("Computer picked: ", paper)
elif player_pick == 0 and computer_pick == paper:
    print("Player LOSES! Paper beats rock.\n")
    print("Player picked: ", rock)
    print("Computer picked: ", paper)
elif player_pick == 1 and computer_pick == scissors:
    print("Player LOSES! Scissors beats paper.\n")
    print("Player picked: ", paper)
    print("Computer picked: ", scissors)
elif player_pick == 2 and computer_pick == rock:
    print("Player LOSES! Rock beats scissors.\n")
    print("Player picked: ", scissors)
    print("Computer picked: ", rock)
else:
    print("It's a draw!\n")
    print("Player picked: ", computer_pick)
    print("Computer picked: ", computer_pick)
