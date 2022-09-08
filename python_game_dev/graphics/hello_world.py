import pygame, sys
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello World!')

# Set up the colors
BLK = (0, 0, 0)
WHT = (255, 255, 255)
RED = (255, 0, 0)
GRN = (0, 255, 0)
BLU = (0, 0, 255)

# Set up fonts
basicFont = pygame.font.SysFont(None, 48)

# Set up the text
text = basicFont.render('Hello World!', True, WHT, BLU)
textRect = text.get_rect()
textRect.centerx = window.get_rect().centerx
textRect.centery = window.get_rect().centery

# Draw the white background onto the surface
window.fill(WHT)

# DRaw a green polygon on to the surface
pygame.draw.polygon(window, GRN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Draw a some bllue lines on the surface
pygame.draw.line(window, BLU, (60, 60), (120, 60), 4)
pygame.draw.line(window, BLU, (120, 60), (60, 120))
pygame.draw.line(window, BLU, (60, 120), (120, 120), 4)

# Draw blue circle onto surface
pygame.draw.circle(window, BLU, (300, 50), 20, 0)

# Draw a red ellipse onto the surface
pygame.draw.ellipse(window, RED, (300, 250, 40, 80), 1)

# DRaw the tests background rectangle onto the surface
pygame.draw.rect(window, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# Get a pixel array of the surface
pixArray = pygame.PixelArray(window)
pixArray[480][380] = BLK
del pixArray

# Draw the test onto the surface
window.blit(text, textRect)

# Draw the window onto the screen
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == 'QUIT':
            pygame.quit()
            sys.exit()