
"""
LESSON: 3.1 - Lines
EXERCISE: Shape Conspiracy
"""

#### ---- SETUP ---- ####

# Pygame
import pygame
pygame.init()

# Window
w = 500
h = 500
window = pygame.display.set_mode([w, h])
window.fill((255, 255, 255))
black = (0, 0, 0)


#### ---- DRAWING ---- ####

# Grid lines
size = 50
x = size
y = size

while x < w:
    pygame.draw.line(window, black, (x, 0), (x, h))
    x += size

while y < h:
    pygame.draw.line(window, black, (0, y), (w, y))
    y += size

# Triangle
pygame.draw.line(window, black, (0, 500), (250, 0), 15)
pygame.draw.line(window, black, (250, 0), (500, 500), 15)
pygame.draw.line(window, black, (0, 500), (500, 500), 15)

# Rectangle
pygame.draw.line(window, black, (150, 350), (350, 350), 15)
pygame.draw.line(window, black, (150, 450), (350, 450), 15)
pygame.draw.line(window, black, (150, 350), (150, 450), 15)
pygame.draw.line(window, black, (350, 350), (350, 450), 15)

# Diamond
pygame.draw.line(window, black, (250, 150), (200, 250), 15)
pygame.draw.line(window, black, (250, 150), (300, 250), 15)
pygame.draw.line(window, black, (300, 250), (250, 350), 15)
pygame.draw.line(window, black, (200, 250), (250, 350), 15)


#### ---- FINISH ---- ####
pygame.display.flip()
input("Press enter to close the window")


# Turn in your Coding Exercise.
