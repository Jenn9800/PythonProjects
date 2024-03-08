import random 
print('Winning Rules as follows: +\n Rock vs paper-> paper wins +\n Rock vs scissor-> Rock wins +\n paper vs scissor-> scissor wins. +\n')

print('Enter Choice: +\n 1. Rock +\n 2.Paper +\n 3.Scissor +\n')

user_input = int(input('User Turn: '))

if user_input == 1:
    print('User choice is: Rock')
elif user_input == 2:
    print('User choice is: Paper')
elif user_input == 3:
    print('User choice is: Scissor')
else: 
    print('Please enter a valid number')
    
print('Now its computer turn....')

comp_choice = random.randint(1, 3)

if comp_choice == 1:
    print('computer choice is: rock')
elif comp_choice == 2:
    print('computer choice is paper')
elif comp_choice == 3:
    print('computer choice is scissor')
    
if user_input == comp_choice:
    print('its a draw', end='')
elif (user_input==1 and comp_choice==2):
    print('user wins', end='')
elif (user_input==2 and comp_choice==1):
    print('comp wins', end='')
elif (user_input==1 and comp_choice==3):
    print('user wins', end='')
elif (user_input==3 and comp_choice==1):
    print('comp wins', end='')
elif (user_input==2 and comp_choice==3):
    print('user wins', end='')
elif (user_input==3 and comp_choice==2):
    print('comp wins', end='')
