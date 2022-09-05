'''
This will be a simple flowchart
dragons dugeon game
'''
import random
from time import sleep

def display_intro():
    print('-'*50)
    print('''You are in a land full of dragons. Infront of you,
          you see two caves. In one cave, the dragon is friendly
          and will share his treasure with you. The other dragon
          is greedy and hungry, and will eat you on sight''')
    print('-'*50)
    
def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? [1/2]\n')
        cave = input()
    return cave

def check_cave(choice):
    print('....')
    sleep(2)
    print("You aproach the cave...")
    sleep(2)
    print("It's dark and spooky...")
    sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and ....')
    print()
    sleep(2)
    cave_status = random.randint(1,2)
    if choice == str(cave_status):
        print("Gives you his treasure!!!")
        sleep(2)
        print('-'*50)
        print('You WIN!!!')
        print('-'*50)
    else:
        print("Eats you to your death.")
        sleep(2)
        print('-'*50)
        print('You LOSE!!!')
        print('-'*50)
        
def main():
    retry = 'yes'
    while retry in ['yes', 'YES', 'Yes', 'y', 'Y']:
        display_intro()
        cave_num = choose_cave()
        check_cave(cave_num)
        sleep(1)
        print('-'*50)
        print('Would you like to play again? [Y/N]\n')
        print('-'*50)
        retry = input()
        
if __name__ == '__main__':
    main()