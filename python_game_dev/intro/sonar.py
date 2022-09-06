'''
Sonar Treasure Hunt
'''
import random as r
import sys
import math as m

def get_new_board():
    # Create a new 60x15 board data structure
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if r.randint(0,1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def draw_board(board):
    tens_digit_line = ' '
    for i in range(1,6):
        tens_digit_line += (' ' * 9) + str(i)
    print(tens_digit_line)
    print('  ' + ('0123456789' * 6))
    print()
    for row in range(15):
        if row < 10:
            extra_space = ' '
        else:
            extra_space = ''
        board_row = ''
        for column in range(60):
            board_row += board[column][row]
        print(f"{extra_space}{row} {board_row} {row}")
    print()
    print(' ' + ('0123456789' * 6))
    print(tens_digit_line)

def get_random_chests(numChests):
    chests = []
    while len(chests) < numChests:
        newChest = [r.randint(0,59), r.randint(0,14)]
        if newChest not in chests:
            chests.append(newChest)
    return chests

def is_on_board(x, y):
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def make_move(board, chests, x, y):
    # CHnage the board data structure with a sonar device character
    # remove chests if found. Return false if is inavalid move
    # Otherwise, return the string of the result of this move
    smallest_distance = 100
    for cx, cy in chests:
        distance = m.sqrt((cx - x) * (cx - x) + (cy - y) * (cy -y))
        if distance < smallest_distance:
            smallest_distance = distance
    smallest_distance = round(smallest_distance)
    if smallest_distance == 0:
        chests.remove([x,y])
        return 'You have found a sunken treasure chest!'
    else:
        if smallest_distance < 10:
            board[x][y] = str(smallest_distance)
            return f'Treasure detected as a distance of {smallest_distance} from sonar device'
        else:
            board[x][y] = 'X'
            return 'Sonar did not detect anything. All treasure out of range.'

def enter_player_move(prev_moves):
    # let player enter their move. return two item list of int xy coordinates
    print('Where do you want to drop the next sonar device (0-59 0-14) or type quit')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing')
            sys.exit()
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and is_on_board(int(move[0]), int(move[1])):
                if [int(move[0]), int(move[1])] in prev_moves:
                    print('You have already moveed there')
                    continue
                return [int(move[0]), int(move[1])]
        print('Enter a number from 0 to 59, a space, then a number from 0 to 14.')
        
def show_instructions():
    print('''Instructions:
          You are the captain fo the Simon, a treasure-hunting ship.
          Your current mission is to use sonar devices to find three
          sunken treasure chests at the bottom of the ocean. But
          You only have cheap sonar that finds distance, not direction
          Enter the cooridnates to drop a sonar device. The ocean map 
          will be marked with how far away the nearest chest is, or an 
          x if it is beyond the sonar device's range. For EX:
            - C marks where the cheats are
            - the sonar shows a 3 because the chest is 
                3 spaces away
                    1         2         3
            012345678901234567890123456789012

            0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
            1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
            2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
            3 ````````~~~`````~~~`~`````~`~``~` 3
            4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

            012345678901234567890123456789012
                        1         2         3
        (In the real game, the chests are not visible in the ocean.)
        -----------------------------------------------
        Press enter to continue....''')
    input()
    print('''When you drop a sonar device directly on a 
          chest, you retrieve it and the other sonar devices
          update to show how far away the next nearest chest 
          is. The chests are beyond the range of the sonar 
          device on the left, so it shows an X.
                         1         2         3
                012345678901234567890123456789012

                0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
                1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
                2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
                3 ````````~~~`````~~~`~`````~`~``~` 3
                4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

                012345678901234567890123456789012
                            1         2         3
            The treasure chests don't move around. 
            Sonar devices can detect treasure chests 
            up to a distance of 9 spaces. Try to collect
            all 3 chests before running out of sonar devices. 
            Good luck!
            ----------------------------------------------
            Press enter to continue....''')
    input()

def main():
    print('S O N A R')
    print()
    print('Would you like to view the instructions? [y/n]')
    if input().lower().startswith('y'):
        show_instructions()
    while True:
        # Game Setup
        sonar_devices = 20
        the_board = get_new_board()
        the_chests = get_random_chests(3)
        draw_board(the_board)
        prevMoves = []
        while sonar_devices > 0:
            # Show sonar device and chest statuses
            print(f'You have {sonar_devices} left. {len(the_chests)} remaining.')
            x, y = enter_player_move(prevMoves)
            prevMoves.append([x, y])
            move_res = make_move(the_board, the_chests, x, y)
            if move_res == False:
                continue
            else:
                if move_res == 'You have found a sunken treasure chest!':
                    for x, y in prevMoves:
                        make_move(the_board, the_chests, x,y)
                    draw_board(the_board)
                    print(move_res)
            if len(the_chests) == 0:
                print('You have found all the sunken treasure chests!')
                print('Congratulations and Good Game!')
                break
            sonar_devices -=1
        if sonar_devices == 0:
            print('''We\'ve run out of sonar devices!
                  Now we have to turn the ship around 
                  and head home with the treasure still
                  OUT THERE!!! GAME OVER!!!\n''')
            print('-'*50)
            print('The remaining chests were:\n')
            for x,y in the_chests:
                print(f'   {x}, {y}')
            print('Would you like to play again? [Y/N]')
            if input().lower().startswith('y'):
                main()
            else:
                sys.exit()

if __name__ == '__main__':
    main()