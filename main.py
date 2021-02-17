rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choices = [rock, paper, scissors]

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors  ")
user_play = choices[int(user_input)]

print(user_play)

computer_input = random.randint(0,2)
computer_play = choices[computer_input]
print(f"Computer chose: {computer_play}")

if computer_play == user_play:
  print("It's a draw")
elif (computer_play == rock and user_play == scissors) or (computer_play == scissors and user_play == paper) or (computer_play == paper and user_play == rock):
  print("Computer wins!")
else:
  print("You won!")



