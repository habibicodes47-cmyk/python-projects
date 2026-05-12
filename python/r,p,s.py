import random

emojies={'r':'🪨','p':'📃','s':'✂️'}
choices={r,p,s}

while True:
   user_choices=input('rock,paper,scissor(r,p,s): ')
if user_choices not in choices:
        print('Invalid choice!!!')
        continue

        computer=random.choice(choices)

        print(f'you chose {choices}')
        print(f'computer choses {computer}')

if user_choices==computer:
    print('Tie!')
elif (user_choices=='r' and computer=='s') or (user_choices=='p' and computer=='r') or (user_choices=='s' and computer=='p'):
        print('you win')
else:
     print('You lose')

thought=input('continue(y/n):').lower()
if thought=='n':
    break

