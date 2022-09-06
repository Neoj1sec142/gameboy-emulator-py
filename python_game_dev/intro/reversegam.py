import random as r
import sys
from time import sleep
WIDTH = 8
HEIGHT = 8

def draw_board(board):
    # print the board passed to this function
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print(f'{(y+1)}|', end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print(f' |{(y+1)}')
    print(' +-------+')
    print('  12345678')
    
def get_new_board():
    # create a new blank board data structure
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def is_valid_move(board, tile, xstart, ystart):
    # Return false if the player's move on space xstart, ystart is invalid
    # If it is a valid move, return a list of spaces that would become 
    #   The playe's if they made a move here
    if board[xstart][ystart] != ' ' or not is_on_board(xstart, ystart):
        return False
    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'
    tiles_to_flip = []
    for xdir, ydir in [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]:
        x, y = xstart, ystart
        x += xdir
        y += ydir
        while is_on_board(x,y) and board[x][y] == otherTile:
            x += xdir
            y += ydir
            if is_on_board(x,y) and board[x][y] == tile:
                while True:
                    x -= xdir
                    y -= ydir
                    if x == xstart and y == ystart:
                        break
                    tiles_to_flip.append([x,y])
    if len(tiles_to_flip) == 0:
        return False
    return tiles_to_flip

def is_on_board(x, y):
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT -1

def get_board_with_valid_moves(board, tile):
    # Return a new board w/ peroids marking the valid moves the player can make
    board_copy = get_board_copy(board)
    for x, y in get_valid_moves(board_copy, tile):
        board_copy[x][y] = '.'
    return board_copy

def get_valid_moves(board, tile):
    # Return a list for [x,y] lists of valid moves for the
    # given player on the given board
    valid_moves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if is_valid_move(board, tile, x, y) != False:
                valid_moves.append([x,y])
    return valid_moves

def get_score_of_board(board):
    # Determine the score by counting the tiles. 
    # Return a dictionary with keys 'X' and 'O'
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}

def enter_player_tile():
    '''Let the player enter which tile they want to be
    Return a list with the player's tile as the first
    item and the computer's tile as the second'''
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    
def who_goes_first():
    if r.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
    
def make_move(board, tile, xst, yst):
    '''Place the tile on the board at xst, yst and flip any
    of the opponent's pieces. Return false if this is an
    invalid move; True if it is valid'''
    tiles_to_flip = is_valid_move(board, tile, xst, yst)
    if tiles_to_flip == False:
        return False
    board[xst][yst] = tile
    for x,y in tiles_to_flip:
        board[x][y] = tile
    return True

def get_board_copy(board):
    # Make a duplicate of the board list and return it
    board_copy = get_new_board()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board_copy[x][y] = board[x][y]
    return board_copy

def is_on_corner(x, y):
    # Return true if the position is on one of the corners
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT -1)

def get_player_move(board, player_tile):
    '''Let the player enter their move
    Return the move as [x,y] or return 
    the strings hints or quit'''
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter your move, "quit" to end the game, or "hints" to toggle hints')
        move = input().lower()
        if move == 'quit' or move == 'hints':
            return move
        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if is_valid_move(board, player_tile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move. Enter the column (1-8) and then row (1-8)')
            print('For Example: 81 will move on the top right corner')
    return [x,y]

def get_computer_move(board, computer_tile):
    '''Given a board and the computer's tile, determine where
    to move and return that move as an [x,y] list.'''
    possible_moves = get_valid_moves(board, computer_tile)
    r.shuffle(possible_moves)
    for x,y in possible_moves:
        if is_on_corner(x,y):
            return [x,y]
    best_score = -1
    for x,y in possible_moves:
        board_copy = get_board_copy(board)
        make_move(board_copy, computer_tile, x, y)
        score = get_score_of_board(board_copy)[computer_tile]
        if score > best_score:
            best_move = [x,y]
            best_score = score
    return best_move

def print_score(board, player_tile, computer_tile):
    scores = get_score_of_board(board)
    print('-'*60)
    print(f'You: {scores[player_tile]} | Computer: {scores[computer_tile]}')
    print('-'*60)
    
def play_game(player_tile, computer_tile):
    show_hints = False
    turn = who_goes_first()
    print(f'The {turn} will go first.')
    # Clear the board and place starting pieces
    board = get_new_board()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'
    while True:
        player_valid_moves = get_valid_moves(board, player_tile)
        computer_valid_moves = get_valid_moves(board, computer_tile)
        if player_valid_moves == [] and computer_valid_moves == []:
            return board
        elif turn == 'player':
            if player_valid_moves != []:
                if show_hints:
                    valid_moves_board = get_board_with_valid_moves(board, player_tile)
                    draw_board(valid_moves_board)
                else:
                    draw_board(board)
                print_score(board, player_tile, computer_tile)
                move = get_player_move(board, player_tile)
                if move == 'quit':
                    print('Thanks for playing!')
                    sys.exit()
                elif move == 'hints':
                    show_hints = not show_hints
                    continue
                else:
                    make_move(board, player_tile, move[0], move[1])
            turn = 'computer'
        elif turn == 'computer':
            if computer_valid_moves != []:
                draw_board(board)
                print_score(board, player_tile, computer_tile)
                input('Press Enter to see the computer\'s moves')
                move = get_computer_move(board, computer_tile)
                make_move(board, computer_tile, move[0], move[1])
            turn = 'player'
            
def main():
    print('Welcome to Reversegam!')
    pl_tile, com_tile = enter_player_tile()
    while True:
        final_board = play_game(pl_tile, com_tile)
        draw_board(final_board)
        scores = get_score_of_board(final_board)
        print(f'X scored {scores["X"]} points. O scored {scores["O"]} points.')
        if scores[pl_tile] > scores[com_tile]:
            print(f'You beat the computer by {(scores[pl_tile] - scores[com_tile])} points! Congratulations!')
        elif scores[pl_tile] < scores[com_tile]:
            print(f'You lost. The computer beat you by {(scores[com_tile] - scores[pl_tile])} points')
        else:
            print('The game was a tie!')
        sleep(3)
        print('Do you want to play again? [Y/N]')
        if input().lower().startswith('y'):
            main()
        else:
            sys.exit()
            
if __name__ == '__main__':
    main()