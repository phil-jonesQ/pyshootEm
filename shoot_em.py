""" Version 1.00 - simple game
Phil Jones July 2019 - phil.jones.24.4@gmail.com
"""

import re
import pygame
import random

# Global Variables
WindowWidth = 900
WindowHeight = 400
x_POS = WindowWidth / 2
y_POS = WindowHeight / 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (101, 152, 101)
GREY = (128, 128, 128)

# Load images
BG = pygame.transform.scale(pygame.image.load("game_assets/BG.jpg"), (WindowWidth, WindowHeight))
#gallows_base = pygame.transform.scale(pygame.image.load("Assets/Gallows_base.png"), (200, 30))
#gallows_post = pygame.transform.scale(pygame.image.load("Assets/Gallows_post.png"), (30, 300))
#gallows_top = pygame.transform.scale(pygame.image.load("Assets/Gallows_top.png"), (200, 30))
#gallows_skew = pygame.transform.scale(pygame.image.load("Assets/Gallows_skew.png"), (30, 30))

# Lives is a constant
lives = 11


# Version constant
version = "1.00"

# Use the pygame clock so we can set the frame rate of the game
clock = pygame.time.Clock()


def main():
    pygame.init()
    # Create the Window
    shoot_em_surface = pygame.display.set_mode((WindowWidth, WindowHeight))
    pygame.display.set_caption("Shoot Em " + str(version))

    # Create an empty list so we can track guessed letters
    guessed_letters = []

    # Game loop and control booleans / counters
    loop = True
    game_over = False

    # Initialise fonts we will use
    font = pygame.font.SysFont('Arial', 50, False, False)

    # Start main game loop
    while loop:

        # Draw background image
        shoot_em_surface.blit(BG, [0, 0])

        # Update the screen
        pygame.display.flip()

        # Keep frame rate at 60 - clearly not needed for this type of game
        clock.tick(60)
        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()

            # Don't react to letter keys if the game is over
            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_a and a:
                    guessed_letters.append("A")

# Call main
if __name__ == "__main__":
    main()
