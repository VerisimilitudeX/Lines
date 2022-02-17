import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((255, 255, 255))
black = (0, 0, 0)

top_left = (0, 0)
bottom_right = (400, 400)
top_right = (0, 400)
bottom_left = (400, 0)
pygame.draw.line(window, black, top_left, bottom_right, 2)
pygame.draw.line(window, black, top_right, bottom_left, 2)

pygame.display.flip()
input("Press enter to close window")
