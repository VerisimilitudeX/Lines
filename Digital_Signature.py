"""
LESSON: 3.1 - Lines
EXERCISE: Digital Signature
"""

#### ---- SETUP ---- ####

# Import the PYGAME library
import pygame

# INITialize pygame
pygame.init()

# SET_MODE to be size [500, 300], and assign the result
# to a variable called window
window = pygame.display.set_mode([500, 300])

# FILL the window with (255, 255, 255)
window.fill((255, 255, 255))

# Create a TUPLE with value (0, 0, 0) and assign it to
# the variable black
black = (0, 0, 0)


#### ---- DRAW LETTERS ---- ####

# DRAW your initials using LINES. For the arguments,
# use window, black, and coordinates that you determine.

# First Letter
# ---> TEST AFTER EACH LINE <--- #
top_left = (30, 0)
bottom_left = (30, 300)
middle_right = (150, 100)
middle_left = (30, 150)
pygame.draw.line(window, black, top_left, bottom_left, 2)
pygame.draw.line(window, black, top_left, middle_right, 2)
pygame.draw.line(window, black, middle_left, middle_right, 2)

# Second Letter
# ---> TEST AFTER EACH LINE <--- #
bottom_lefta = (250, 300)
top_middle = (300, 10)
bottom_right = (450, 300)
middle_middle1 = (270, 150)
middle_middle2 = (370, 150)
pygame.draw.line(window, black, bottom_lefta, top_middle, 2)
pygame.draw.line(window, black, top_middle, bottom_right, 2)
pygame.draw.line(window, black, middle_middle1, middle_middle2, 2)

#### ---- FINISH ---- ####

# FLIP the display
pygame.display.flip()

# Get input to pause the program
# ---> TEST AFTER THIS LINE <--- #
input()


# Turn in your Coding Exercise.

