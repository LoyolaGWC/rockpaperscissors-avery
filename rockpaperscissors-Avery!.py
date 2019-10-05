#!/bin/python3

from random import randint
player=input('rock(r),paper(p),scissors,(s)')

print(player)

chosen=randint(1,3)
print(chosen)

if chosen==1:
   computer = 'r'

elif chosen ==2:
  computer = 'p'

else:
  computer = 's'

if player == computer:
  print('DRAW!')

elif player == 'r' and computer == 's':
  print('player wins!')

elif player == 'p' and computer == 'r':
  print('player wins!')