import random

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


actions = [rock, paper, scissors]
player_move = actions[int(input('Your move: rock (1), paper (2), scissors (3):\n'))-1]
computer_move = random.choice(actions)

print(f'Your move:\n{player_move}')
print(f'Computer move:\n{computer_move}')

if player_move == rock:
    if computer_move == rock:
        print('Draw')
    elif computer_move == paper:
        print('Computer wins')
    else:
        print('Player wins')
elif player_move == paper:
    if computer_move == rock:
        print('Player wins')
    elif computer_move == paper:
        print('Draw')
    else:
        print('Computer wins')
else:
    if computer_move == rock:
        print('Computer wins')
    elif computer_move == paper:
        print('Player wins')
    else:
        print('Draw')
