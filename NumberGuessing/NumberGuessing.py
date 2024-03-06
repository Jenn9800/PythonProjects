import random
import math 

min = 0 
max = 100
guess_number = random.randint(0, 100)
max_attempt = 10
attempt = 0

while attempt<=max_attempt:
    user_input = int(input('Input Number: '))
    attempt += 1
    if user_input > guess_number:
        print('guess a smaller number')
    elif user_input < guess_number:
        print('guess a bigger number')
    elif user_input ==  guess_number:
        print("you won!")
        break
if attempt > max_attempt:
    print('sorry, reached max attempt :(')
    
