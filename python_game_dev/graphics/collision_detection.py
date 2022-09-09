from curses import KEY_DOWN
from curses.ascii import SP
import sys, pygame as p
import random as r
from pygame.locals import *

# Set up the game
p.init()
mainClock = p.time.Clock()

# Set up the windows
HEIGHT = 400
WIDTH = 400

window = p.display.set_mode((WIDTH, HEIGHT), 0, 32)
p.display.set_caption('Collision Detection')

# Set up the colors
BLK = (0, 0, 0)
GRN = (0, 255, 0)
WHT = (255, 255, 255)

# Set up the player and food data structures
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = p.Rect(300, 100, 50, 50)
foods = []
for i in range(20):
    foods.append(p.Rect(r.randint(0, WIDTH - FOODSIZE), 
                        r.randint(0, HEIGHT - FOODSIZE), 
                        FOODSIZE, FOODSIZE))

# Set up movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

SPEED = 6

# Run the game loop
while True:
    for event in p.event.get():
        if event.type == QUIT:
            p.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Checnge th ekeyboard varaibles:
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                p.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = r.randint(0, HEIGHT = player.height)
                player.left = r.randint(0, WIDTH = player.height)
        if event.type == MOUSEBUTTONUP:
            foods.append(p.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))
    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # Add new food:
        foodCounter = 0
        foods.append(p.Rect(r.randint(0, WIDTH - FOODSIZE), r.randint(0, HEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
    window.fill(WHT)
    # MOve the player
    if moveDown and player.bottom < HEIGHT:
        player.top += SPEED
    if moveUp and player.top > 0:
        player.top -= SPEED
    if moveLeft and player.left > 0:
        player.left -= SPEED
    if moveRight and player.right < WIDTH:
        player.right += SPEED
    
    p.draw.rect(window, BLK, player)
    
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
    
    for i in range(len(foods)):
        p.draw.rect(window, GRN, foods[i])
        
    p.display.update()
    mainClock.tick(40)