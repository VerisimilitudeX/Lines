import pygame

pygame.init()

window = pygame.display.set_mode([400, 400])

window.fill = (255, 255, 255)

black = (0, 0, 0)

pygame.draw.line(window, black, (50, 200), (50, 350))

pygame.draw.line(window, black, (50, 350), (350, 350))

pygame.draw.line(window, black, (350, 350), (350, 200))

pygame.draw.line(window, black, (350, 200), (50, 200))

up_left = (100, 230)

up_right = (150, 230)

low_left = (100, 280)

low_right = (150, 280)

pygame.draw.line(window, black, up_left, up_right)

pygame.draw.line(window, black, up_left, low_left)

pygame.draw.line(window, black, low_left, low_right)

pygame.draw.line(window, black, low_right, up_right)

pygame.draw.line(window, black, (50, 200), (200,50))

pygame.draw.line(window, black,(200, 50), (350, 200))

pygame.draw.line(window, black, (200,350), (200,250))

pygame.draw.line(window, black, (250, 350), (250, 250))

pygame.draw.line(window, black, (200,250), (250, 250))

pygame.display.flip()

input()
