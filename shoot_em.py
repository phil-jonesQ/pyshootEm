""" Version 1.00 - simple game
Phil Jones July 2019 - phil.jones.24.4@gmail.com
"""

import re
import pygame
import random
import os

# Global Variables
WindowWidth = 1400
WindowHeight = 700
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

ASTEROID_FRAMES = 16

# Load images
BG = pygame.transform.scale(pygame.image.load("game_assets/BG.jpg"), (WindowWidth, WindowHeight))
ship = pygame.transform.scale(pygame.image.load("game_assets/Ship1_new.png"), (100, 30))

# Load Asteroids
a_images = []
path = "game_assets/medium/a1"
for file_name in os.listdir(path):
    image = pygame.transform.scale(pygame.image.load(path + os.sep + file_name), (60, 60))
    a_images.append(image)

# Lives is a constant
lives = 3


# Version constant
version = "1.01"

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
            self.velocity += 0.4
            if self.velocity > 0.6:
                self.velocity += 0.8
            if self.velocity > 0.16:
                self.velocity += 3
            self.mover += self.velocity
            self.ship_pos = (self.ship_pos_x, self.ship_pos_y + self.mover)
            # Ship hits edge
            if self.ship_pos[1] > WindowHeight - SHIP_WIDTH:
                self.velocity = 0
                self.ship_pos = (0, WindowHeight - SHIP_WIDTH)
                self.mover = WindowHeight / 2 - SHIP_WIDTH
        if ship_dir == -1:
            self.velocity += 0.4
            if self.velocity > 0.6:
                self.velocity += 0.8
            if self.velocity > 0.16:
                self.velocity += 3
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
        self.images = a_images
        self.a_pos = pos
        self.scroll = 0
        # index value to get the image from the array
        # initially it is 0
        self.index = 0
        # now the image that we will display will be the index from the image array
        self.image = self.images[self.index]
        # creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite
        #self.rect = pygame.Rect(self.a_pos[0], self.a_pos[1], 40, 40)

    def animation(self):
        # when the update method is called, we will increment the index
        self.index += 1

        # if the index is larger than the total images
        if self.index >= len(self.images):
            # we will make the index to 0 again
            self.index = 0
        # finally we will update the image that will be displayed
        self.image = self.images[self.index]
    def updateSprite(self):
        self.scroll += -5
        updated_x = self.a_pos[0] + self.scroll
        # Constrain
        if updated_x < -30:
            self.scroll = 0
            updated_x = WindowWidth
        self.rect = pygame.Rect(updated_x, self.a_pos[1], 40, 40)
        #print (updated_x)


def rand_Coord():
    return random.randrange(300, WindowWidth), random.randrange(0, WindowHeight)


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

    # Generate a list of 19 Asteroid objects
    wave_list = [19 , 34, 45]
    wave = wave_list[2]
    asteroids = [Asteroid((rand_Coord())) for i in range(wave)]
    asteroids_group = [pygame.sprite.Group(asteroids) for i in range(wave)]

    # Start main game loop
    while loop:

        # Draw background image
        shoot_em_surface.blit(BG, [0, 0])

        # Draw our ship
        s.draw(shoot_em_surface)

        # Draw Asteroids
        #a.animation()
        #a_group.draw(shoot_em_surface)
        current_list_len = len(asteroids_group)
        #print(current_list_len)
        for i in asteroids:
            i.animation()
            i.updateSprite()
        for i in range(current_list_len):
            #asteroids_group[i].clear(shoot_em_surface,BG)
            asteroids_group[i].draw(shoot_em_surface)


        # Update the screen
        pygame.display.flip()


        # Control frame rate
        clock.tick(10)

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
        if keys[pygame.K_x]:
            asteroids_group.pop(0)
            asteroids.pop(0)

# Call main
if __name__ == "__main__":
    main()
