""" Version 1.00 - simple game
Phil Jones July 2019 - phil.jones.24.4@gmail.com
"""

import re
import pygame
import random

# Global Variables
WindowWidth = 1200
WindowHeight = 600
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
ship = pygame.transform.scale(pygame.image.load("game_assets/Ship1_new.png"), (200, 40))

# Lives is a constant
lives = 3


# Version constant
version = "1.00"

# Use the pygame clock so we can set the frame rate of the game
clock = pygame.time.Clock()


# Ship Class
class Ship(object):

    def __init__(self, start_pos):
        self.ship_pos = start_pos
        self.ship_pos_x = self.ship_pos[0]
        self.ship_pos_y = self.ship_pos[1]
        self.mover = 0
        self.velocity = 1

    def draw(self, surface):
        the_ship_pos = self.ship_pos
        #print(the_ship_pos)
        surface.blit(ship, the_ship_pos)

    def move(self, ship_dir):
        ship_velocity = self.velocity
        print(ship_velocity,self.mover)
        if ship_dir == 1:
            self.mover += ship_velocity
            ship_velocity += 10
        if ship_dir == -1:
            self.mover -= ship_velocity
        self.ship_pos = (self.ship_pos_x, self.ship_pos_y + self.mover)


class Asteroid(object):
    pass


def main():
    # Create the Window
    pygame.init()
    shoot_em_surface = pygame.display.set_mode((WindowWidth, WindowHeight))
    pygame.display.set_caption("Shoot Em " + str(version))
    pygame.key.set_repeat(1, 1)

    # Initialise fonts we will use
    font = pygame.font.SysFont('Arial', 50, False, False)

    # Game loop and control booleans / counters
    loop = True
    game_over = False

    # Initialise game objects
    s = Ship((0, (WindowHeight / 2)))

    # Start main game loop
    while loop:

        # Draw background image
        shoot_em_surface.blit(BG, [0, 0])

        # Draw our ship
        s.draw(shoot_em_surface)

        # Update the screen
        pygame.display.flip()


        # Control frame rate
        clock.tick(160)

        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            s.move(-1)
        if keys[pygame.K_DOWN]:
            s.move(1)
        if keys[pygame.K_SPACE]:
            print("FIRE")

# Call main
if __name__ == "__main__":
    main()
