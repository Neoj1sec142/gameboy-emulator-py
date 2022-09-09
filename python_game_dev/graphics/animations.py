import sys, time, pygame as p
from pygame.locals import *

p.init()

# Set up the window
WIDTH = 400
HEIGHT = 400

window = p.display.set_mode((WIDTH, HEIGHT), 0, 32)
p.display.set_caption('Animation')

# Set up direction variables
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

SPEED = 4

# Set up the colors
WHT = (255, 255, 255)
RED = (255, 0, 0)
GRN = (0, 255, 0)
BLU = (0, 0, 255)

# Set up the game loop
b1 = {'rect':p.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':p.Rect(200, 200, 20, 20), 'color':GRN, 'dir':UPLEFT}
b3 = {'rect':p.Rect(100, 150, 60, 60), 'color':BLU, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]
# run the game loop
while True:
    # Chekc for the quit event
    for event in p.event.get():
        if event.type == QUIT:
            p.quit()
            sys.exit()
    window.fill(WHT)
    for b in boxes:
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= SPEED
            b['rect'].top += SPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += SPEED
            b['rect'].top += SPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= SPEED
            b['rect'].top -= SPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += SPEED
            b['rect'].top -= SPEED
            
        # Check weather the box has moved out of the window
        if b['rect'].top < 0:
            # The box has moved past the bottom
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
                
        if b['rect'].bottom > HEIGHT:
            # The box has moved past the bottom
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            # The box has moved past the left side
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WIDTH:
            # The box has moved past the left side
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT
                
        p.draw.rect(window, b['color'], b['rect'])
    p.display.update()
    time.sleep(0.02)
