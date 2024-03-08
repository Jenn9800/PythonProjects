import random
import requests

#function to get list of words from web source
def get_list_of_words():
    response = requests.get(
        'https://www.mit.edu/~ecprice/wordlist.10000',
        timeout=10
    )
    
    string_of_words = response.content.decode('utf-8')

    list_of_words = string_of_words.splitlines()

    return list_of_words

#print out the list of words for debugiing
words = get_list_of_words()
#print(words)

#choose a random word from the list and print it out
random_word = random.choice(words)
#print(random_word)


quit_input = 'Q'

correct_guess =['-'] * len(random_word)
wrong_guess = []

while True:
    user_input = input('guess a char/press Q to quit: ')
    
    if user_input == quit_input:
        print('the random word is: '+ random_word)
    
    for i, char in enumerate(random_word):
        if char in user_input:
            correct_guess[i] = char 
        else:
            if correct_guess[i] == '-':
                correct_guess[i] =='-'

    if user_input not in random_word:
        wrong_guess.append(user_input)
    
    word_display = ''.join(correct_guess)
    print('Correct guessed words: ' + word_display)
    
    wrong_display = ''.join(wrong_guess)
    print('Wrong guessed words: ' + wrong_display)
    
    if set(correct_guess) ==  set(random_word):
        print('you won!')
        break
    