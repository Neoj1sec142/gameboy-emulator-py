import random
import sys
def main():
    print('I will flip a coin 1000 time. Guess how many times it will come up heads\n')
    choice = input()
    flips = 0
    heads = 0
    while flips < 1000:
        if random.randint(0,1) == 1:
            heads += 1
        flips += 1
        if flips == 900:
            print(f'900 flips and there have been {heads} heads')
        if flips == 100:
            print(f"At 100 flips heads has come up {heads} times")
        if flips == 500:
            print(f'Halfway done, and heads has come up {heads} times')
    print()
    print(f'Out of 1,000 coin tosses, heads came up {heads} times!')
    print(f'You chose {choice}\n')
    if int(choice) == int(heads):
        print('YOU WERE RIGHT!!!!\n')
    retry = input("Would you like to play again? [Y/N]: ")
    if retry in ['Y', 'y', 'yes', 'Yes', 'YES']:
        main()
    else:
        sys.exit()
        
if __name__ == '__main__':
    main()
