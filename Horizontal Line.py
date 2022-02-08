"""
LESSON: 3.1 - Lines
WARMUP 3
"""

import pygame
pygame.init()

w = pygame.display.set_mode([400, 400])
w.fill((255, 255, 255))
black = (0, 0, 0)

# Draw lines here
pygame.draw.line(w, black, (200, 0), (200, 400), 2)
pygame.draw.line(w, black, (0, 200), (400, 200), 2)



pygame.display.flip()
input("Press enter to close window")

