'''
Simple Guess The Number Game
'''
import random
from time import sleep
import sys
def main():
    guesses_taken = 0
    print('-'*50)
    print('''Hello, and Welcome to
        Guess the Number!''')
    print('-'*50)
    print('What is your name: \n')

    my_name = input()

    num = random.randint(1, 20)
    print(f'Well, {my_name}, I am thinging of a number between 1 an 20.')

    for guesses_taken in range(6):
        print('-'*50)
        print('Take a guess.')
        print('-'*50)
        guess = input()
        guess = int(guess)
        
        if guess < num:
            print('Your guess is to low')
        if guess > num:
            print('Your guess is to high')
        if guess == num:
            break
    if guess == num:
        guesses_taken = str(guesses_taken + 1)
        print(f'Good job {my_name}! Your guessed the number in {guesses_taken} guesses!!')
        print('-'*50)
        print('YOU WIN!!!')
        print('-'*50)
        sleep(1)
        print("Would you like to play again? [Y/N]\n")
        retry = input()
        if retry in ['Y', 'y', 'YES', 'yes', 'Yes']:
            main()
        else:
            sys.exit()
    if guess != num:
        num = str(num)
        print(f'Nope. The number I was thinking of was {num}.')
        print('-'*50)
        print('YOU LOSE!! GAME OVER!!')
        print('-'*50)
        sleep(1)
        print("Would you like to try again? [Y/N]\n")
        retry = input()
        if retry in ['Y', 'y', 'YES', 'yes', 'Yes']:
            main()
        else:
            sys.exit()
            
if __name__ == '__main__':
    main()