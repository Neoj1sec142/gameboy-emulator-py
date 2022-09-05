'''
A Simple Hangman Game
'''
import random
from re import T
HANGMAN_PICS = ['''
                +---+
                    |
                    |
                    |
                   ===''','''
                +---+
                O   |
                    |
                    |
                   ===''', '''
                +---+
                O   |
                |   |
                    |
                   ===''', '''
                +---+
                O   |
               /|   |
                    |
                   ===''', '''
                +---+
                O   |
               /|\  |
                    |
                   ===''', '''
                +---+
                O   |
               /|\  |
               /    |
                   ===''', '''
                +---+
                O   |
               /|\  |
               /\   |
                   ===''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
def get_random_words(word_list):
    index = random.randint(0, len(word_list) - 1)
    return word_list[index]

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    
    print('Missed letters: ', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()
    
    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end=' ')
    print()
    
def get_guess(alreadyGuessed):
    while True:
        print('Guess a letter\n')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please use a LETTER')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def main():
    print('H A N G M A N')
    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_words(words)
    is_done = False
    while True:
        display_board(missed_letters, correct_letters, secret_word)
        guess = get_guess(missed_letters + correct_letters)
        if guess in secret_word:
            correct_letters += guess
            found_all_letters = T
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break
                if found_all_letters:
                    print(f'YES! The secret word in {secret_word}! YOU WIN!!!')
                    is_done = True
        else:
            missed_letters += guess
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_board(missed_letters, correct_letters, secret_word)
                print(f'You have run out of guesses!\n After {str(len(missed_letters))} missed guesses and {str(len(correct_letters))} correct guesses.')
                print(f'The secret word was: {secret_word}')
                is_done = True
                
        if is_done:
            if playAgain():
                missed_letters = ''
                correct_letters = ''
                is_done = False
                secret_word = get_random_words(words)
            else:
                break
            
if __name__ == '__main__':
    main()