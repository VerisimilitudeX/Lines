"""
LESSON: 3.1 - Lines
WARMUP 4
"""
import pygame
pygame.init()
w = pygame.display.set_mode([400, 400])
w.fill((255, 255, 255))
black = (0, 0, 0)
pygame.draw.line(w, black, (0, 50), (250, 100), 2)
pygame.display.flip()
input()
