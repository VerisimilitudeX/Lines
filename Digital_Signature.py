import pygame

pygame.init()
window = pygame.display.set_mode([500, 300])
window.fill((255, 255, 255))
black = (0, 0, 0)

top_left = (30, 0)
bottom_left = (30, 300)
middle_right = (150, 100)
middle_left = (30, 150)
pygame.draw.line(window, black, top_left, bottom_left, 2)
pygame.draw.line(window, black, top_left, middle_right, 2)
pygame.draw.line(window, black, middle_left, middle_right, 2)

bottom_lefta = (250, 300)
top_middle = (300, 10)
bottom_right = (450, 300)
middle_middle1 = (270, 150)
middle_middle2 = (370, 150)
pygame.draw.line(window, black, bottom_lefta, top_middle, 2)
pygame.draw.line(window, black, top_middle, bottom_right, 2)
pygame.draw.line(window, black, middle_middle1, middle_middle2, 2)

pygame.display.flip()

input()
