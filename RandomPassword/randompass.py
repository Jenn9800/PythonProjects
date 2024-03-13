import random 
import string

while True:

    charlist = string.ascii_letters + string.digits + string.punctuation

    password = []
    
    user_input = input('Enter length of password (q to quit): ')
    if user_input == 'q':
        print('bye!')
        break
        
    int_user_input = int(user_input)
    for i in range(int_user_input):
        randomchar = random.choice(charlist)
        password.append(randomchar)
    print('the random password is ' + "".join(password))