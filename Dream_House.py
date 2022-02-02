"""
LESSON: 3.1 - Lines
EXERCISE: Dream House
"""

#### ---- SETUP ---- ####

# Import the PYGAME library
import pygame

# INITialize pygame
pygame.init()

# SET_MODE to be size [400, 400], and assign to
# a variable called window
window = pygame.display.set_mode([400, 400])

# FILL the window with (255, 255, 255)
window.fill = (255, 255, 255)

# Create a TUPLE with three values, (0, 0, 0) and
# assign it to the variable black
black = (0, 0, 0)


#### ---- DRAW LINES ---- ####

# DRAW LINES to make a house. Use the following as
# arguments: window, black, and the two points listed
# in the comments below.

# -- Body of the house (4 lines) --

# (50, 200), (50, 350)
# ---> TEST AFTER THIS LINE <--- #
pygame.draw.line(window, black, (50, 200), (50, 350))

# (50, 350), (350, 350)
pygame.draw.line(window, black, (50, 350), (350, 350))

# (350, 350), (350, 200)
pygame.draw.line(window, black, (350, 350), (350, 200))

# (350, 200), (50, 200)
# ---> TEST AFTER THIS LINE <--- #
pygame.draw.line(window, black, (350, 200), (50, 200))


# -- Window (4 Lines) --

# Assign the TUPLE (100, 230) to variable up_left
up_left = (100, 230)

# Assign the TUPLE (150, 230) to variable up_right
up_right = (150, 230)

# Assign the TUPLE (100, 280) to variable low_left
low_left = (100, 280)

# Assign the TUPLE (150, 280) to variable low_right
low_right = (150, 280)

# DRAW a LINE from up_left to up_right
# ---> TEST AFTER THIS LINE <--- #
pygame.draw.line(window, black, up_left, up_right)

# DRAW a LINE from up_left to low_left
pygame.draw.line(window, black, up_left, low_left)

# DRAW a LINE from low_left to low_right
pygame.draw.line(window, black, low_left, low_right)

# DRAW a LINE from low_right to up_right
# ---> TEST AFTER THIS LINE <--- #
pygame.draw.line(window, black, low_right, up_right)

# -- Roof (2 lines) --

# (50, 200), (200, 50)
pygame.draw.line(window, black, (50, 200), (200,50))

# (200, 50), (350, 200)
# ---> TEST AFTER THIS LINE <--- #
pygame.draw.line(window, black,(200, 50), (350, 200))


# -- Door (3 lines) --

# (200, 350), (200, 250)
pygame.draw.line(window, black, (200,350), (200,250))

# (250, 350), (250, 250)
pygame.draw.line(window, black, (250, 350), (250, 250))

# (200, 250), (250, 250)
# ---> TEST AFTER THIS LINE <--- #
pygame.draw.line(window, black, (200,250), (250, 250))


#### ---- FINISH ---- ####

# FLIP the display
pygame.display.flip()

# Get input to pause the program
# ---> TEST AFTER THIS LINE <--- #
input()




