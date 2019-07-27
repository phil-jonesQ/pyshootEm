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

MAX_VELOCITY = 20
SHIP_WIDTH = 40

# Load images
BG = pygame.transform.scale(pygame.image.load("game_assets/BG.jpg"), (WindowWidth, WindowHeight))
ship = pygame.transform.scale(pygame.image.load("game_assets/Ship1_new.png"), (200, 40))
asteroid = pygame.transform.scale(pygame.image.load("game_assets/medium/a10000.png"), (60, 60))
asteroid1 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10001.png"), (60, 60))
asteroid2 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10002.png"), (60, 60))
asteroid3 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10003.png"), (60, 60))
asteroid4 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10004.png"), (60, 60))
asteroid5 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10005.png"), (60, 60))
asteroid6 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10006.png"), (60, 60))
asteroid7 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10007.png"), (60, 60))
asteroid8 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10008.png"), (60, 60))
asteroid9 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10009.png"), (60, 60))
asteroid10 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10010.png"), (60, 60))
asteroid11 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10011.png"), (60, 60))
asteroid12 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10012.png"), (60, 60))
asteroid13 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10013.png"), (60, 60))
asteroid14 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10014.png"), (60, 60))
asteroid15 = pygame.transform.scale(pygame.image.load("game_assets/medium/a10015.png"), (60, 60))
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
        self.velocity = 0
        self.direction = 0

    def draw(self, surface):
        the_ship_pos = self.ship_pos
        surface.blit(ship, the_ship_pos)

    def move(self, ship_dir):
        #print(self.velocity, self.ship_pos, ship_dir, self.mover)
        if ship_dir == 1:
            self.velocity += 4
            if self.velocity > 2:
                self.velocity += 8
            if self.velocity > 5:
                self.velocity += 12
            self.mover += self.velocity
            self.ship_pos = (self.ship_pos_x, self.ship_pos_y + self.mover)
            # Ship hits edge
            if self.ship_pos[1] > WindowHeight - SHIP_WIDTH:
                self.velocity = 0
                self.ship_pos = (0, WindowHeight - SHIP_WIDTH)
                self.mover = WindowHeight / 2 - SHIP_WIDTH
        if ship_dir == -1:
            self.velocity += 4
            if self.velocity > 2:
                self.velocity += 8
            if self.velocity > 5:
                self.velocity += 12
            self.mover -= self.velocity
            self.ship_pos = (self.ship_pos_x, self.ship_pos_y + self.mover)
            # Ship hits edge
            if self.ship_pos[1] < 0:
                self.velocity = 0
                self.ship_pos = (0, 0)
                self.mover = -WindowHeight / 2

    def reset_velocity(self):
        self.velocity = 0


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Asteroid, self).__init__()
        self.images = []
        self.images.append(asteroid)
        self.images.append(asteroid1)
        self.images.append(asteroid2)
        self.images.append(asteroid3)
        self.images.append(asteroid4)
        self.images.append(asteroid5)
        self.images.append(asteroid6)
        self.images.append(asteroid7)
        self.images.append(asteroid8)
        self.images.append(asteroid9)
        self.images.append(asteroid10)
        self.images.append(asteroid11)
        self.images.append(asteroid12)
        self.images.append(asteroid13)
        self.images.append(asteroid14)
        self.images.append(asteroid15)
        self.a_pos = pos
        self.scroll = 0

        # index value to get the image from the array
        # initially it is 0
        self.index = 0

        # now the image that we will display will be the index from the image array
        self.image = self.images[self.index]

        # creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite
        self.rect = pygame.Rect(self.a_pos[0], self.a_pos[1], 40, 40)

    def animation(self):
        # when the update method is called, we will increment the index
        self.index += 1

        # if the index is larger than the total images
        if self.index >= len(self.images):
            # we will make the index to 0 again
            self.index = 0

        # finally we will update the image that will be displayed
        self.image = self.images[self.index]

    def move(self):
        self.scroll += -1
        self.a_pos = (self.a_pos[0] + self.scroll, self.a_pos[1])
        print(self.a_pos)


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
    a = Asteroid((500, 500))
    a_group = pygame.sprite.Group(a)
    a1 = Asteroid((600, 600))
    a1_group = pygame.sprite.Group(a1)

    # Start main game loop
    while loop:

        # Draw background image
        shoot_em_surface.blit(BG, [0, 0])

        # Draw our ship
        s.draw(shoot_em_surface)

        # Draw Asteroids
        a_group.update()
        a.animation()
        a_group.draw(shoot_em_surface)
        a1_group.update()
        a1.animation()
        a1_group.draw(shoot_em_surface)

        # Move Asteroids
        a.move()
        a1.move()

        # Update the screen
        pygame.display.flip()


        # Control frame rate
        clock.tick(16)

        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
            if event.type == pygame.KEYUP:
                s.reset_velocity()

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
