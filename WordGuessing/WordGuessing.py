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

# Initialize with dashes for all characters
correct_guess = ['-'] * len(random_word)  

#special char to quit the game
input_quit = 'Q'
while True:
    #get user input
    input_guess = input('Guess a char/type Q to quit: ')
    
    if input_guess == input_quit:
        print('the word is: ' + random_word)
    
    #iterate through each char in the random word
    for i, char in enumerate(random_word):
        #if guessed char is correct, put it into the list
        if char in input_guess:
            correct_guess[i] = char
        else: #otherwise, preseve the dash for chars that has not been guessed
            if correct_guess[i] == '-':
                correct_guess[i] = '-'            
    #display the correct state of word by joining the correct gussed words 
    display_word = ''.join(correct_guess)
    print(display_word)
    
    # Check if the user has guessed all the characters
    if set(correct_guess) == set(random_word):
        print('You won!')
        break

