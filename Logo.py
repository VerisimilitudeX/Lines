import pygame
pygame.init()
window = pygame.display.set_mode([400, 400])
window.fill((255, 255, 255))
black = (0, 0, 0)
top_left = (30, 30)
top_right = (370, 30)
bottom_left = (30, 370)
bottom_right = (370, 370)

pygame.draw.line(window, black, top_left, top_right, 2)
pygame.draw.line(window, black, top_left, bottom_left, 2)
pygame.draw.line(window, black, top_right, bottom_right, 2)
pygame.draw.line(window, black, top_right, bottom_right, 2)

pygame.display.flip()
input()
