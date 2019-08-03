""" Version 1.00 - simple game
Phil Jones July 2019 - phil.jones.24.4@gmail.com
"""

import re
import pygame
import random
import os
import time

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
laser = pygame.transform.scale(pygame.image.load("game_assets/laser.png"), (100, 3))

# Load Asteroids
a_images = []
path = "game_assets/medium/a1"
for file_name in os.listdir(path):
    image = pygame.transform.scale(pygame.image.load(path + os.sep + file_name), (60, 60))
    #image = pygame.image.load(path + os.sep + file_name)
    a_images.append(image)

# Load Explosions
e_images = []
path = "game_assets/explosion"
for file_name in os.listdir(path):
    image = pygame.transform.scale(pygame.image.load(path + os.sep + file_name), (57, 57))
    e_images.append(image)

# Lives is a constant
lives = 3


# Version constant
version = "1.01"

# Use the pygame clock so we can set the frame rate of the game
clock = pygame.time.Clock()


# Ship Class
class Ship(pygame.sprite.Sprite):

    def __init__(self, start_pos):
        super(Ship, self).__init__()
        self.ship_pos = start_pos
        self.ship_pos_x = self.ship_pos[0]
        self.ship_pos_y = self.ship_pos[1]
        self.mover = 0
        self.velocity = 0
        self.direction = 0
        self.damage = 0
        self.damage_threshold = 50
        self.rect2 = ship.get_rect()
        self.radius = 35


    def draw(self, surface):
        the_ship_pos = self.ship_pos
        surface.blit(ship, the_ship_pos)
        self.rect = pygame.Rect(the_ship_pos[0], the_ship_pos[1], 50, 30)
        #pygame.draw.circle(ship, RED, self.rect2.center, self.radius)
        #surface.blit(self.rect, the_ship_pos)
        #pygame.draw.rect(surface, [255, 0, 0], [the_ship_pos[0], the_ship_pos[1], 50, 30], 1)

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
        if ship_dir == 2:
            self.velocity += 0.4
            if self.velocity > 0.6:
                self.velocity += 0.8
            if self.velocity > 0.16:
                self.velocity += 3
            self.mover += self.velocity
            self.ship_pos = (self.ship_pos_x + self.mover, self.ship_pos_y)
            # Ship hits edge
            if self.ship_pos[1] < 0:
                self.velocity = 0
                self.ship_pos = (0, 0)
                self.mover = -WindowHeight / 2

    def reset_velocity(self):
        self.velocity = 0

    def is_ship_destroyed(self):
        if self.damage > self.damage_threshold:
            return True


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
        self.rect = self.images[self.index]
        self.rect = pygame.rect.Rect(self.a_pos[0], self.a_pos[1], 60, 60)
        self.damage = 0
        self.damage_threshold = 40

    def animation(self):
        # when the update method is called, we will increment the index
        self.index += 1
        # if the index is larger than the total images
        if self.index >= len(self.images):
            # we will make the index to 0 again
            self.index = 0
        # finally we will update the image that will be displayed
        self.image = self.images[self.index]

    def update_sprite(self, surface):
        self.scroll += -5
        updated_x = self.a_pos[0] + self.scroll
        # Constrain
        if updated_x < -100:
            self.scroll = 0
            self.a_pos = (WindowWidth, self.a_pos[1])
        self.rect = pygame.Rect(updated_x, self.a_pos[1], 60, 60)
        updated_y = self.a_pos[1]
        return updated_x, updated_y

    def is_colliding(self, ship, explode, e_group, surface):
        s = ship
        e = explode
        shoot_em_surface = surface
        if self.rect.colliderect(s.rect):
            #print("collided with ship and the damage is " + str(s.damage))
            #print("*****")
            s.damage += 1
            e.update_sprite(s.ship_pos)
            e.animation()
            e_group.draw(shoot_em_surface)
            if s.is_ship_destroyed():
                print("BOOM! Life is lost!!")


class Explosion(pygame.sprite.Sprite):

    def __init__(self):
        super(Explosion, self).__init__()
        self.images = e_images
        self.e_pos = (0, 0)
        self.index = 0
        # now the image that we will display will be the index from the image array
        self.image = self.images[self.index]
        self.noi = 10
        self.current_image = 0

        self.time = 0

    def animation(self):
        # when the update method is called, we will increment the index
        self.time += 1
        self.index += 1
        # if the index is larger than the total images
        if self.index >= len(self.images):
            # we will make the index to 0 again
            self.index = 0
        # finally we will update the image that will be displayed
        self.image = self.images[self.index]
        self.time = 0

    def update_sprite(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 57, 57)


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Laser, self).__init__()
        self.image = laser
        self.laser_pos = pos
        self.propogate = 0
        self.propogate_stop = 100
        self.mask = pygame.mask.from_surface(self.image)
        self.charged = True

    def draw(self, surface, ship, asteroids, a_group, explosion, e_group):
        the_laser_pos = (ship.ship_pos[0] + 50, ship.ship_pos[1] + 20)
        i = 0
        while i < 1000:
            i += 1
            self.charged = False
            self.propogate += 5
            the_laser_pos = (the_laser_pos[0] + self.propogate, the_laser_pos[1])
            #print (self.propogate)
            surface.blit(laser, the_laser_pos)
            self.rect = pygame.Rect(the_laser_pos[0], the_laser_pos[1], 10, 3)
            #pygame.draw.rect(surface, [255, 0, 0], [the_laser_pos[0], the_laser_pos[1], 100, 3], 1)
            if self.is_colliding(asteroids, a_group, surface, explosion, e_group):
                break
        self.propogate = 0

    def is_colliding(self, asteroids, a_group, surface, explosion, e_group):
        e = explosion
        e_g = e_group
        e1 = Explosion()
        e1_g = pygame.sprite.Group(e1)
        for i in asteroids:
            if self.rect.colliderect(i.rect):
                i.damage += 1
                #print (i.damage)
                #asteroid_pos = i.update_sprite(surface)
                #e.update_sprite(asteroid_pos)
                #e_g.draw(surface)
                if i.damage > i.damage_threshold:
                    i.kill()
                    #for repeat in range(15):
                    asteroid_pos = i.update_sprite(surface)
                    e.update_sprite(asteroid_pos)
                    e.animation()
                    e_g.draw(surface)
                    e1.update_sprite(asteroid_pos + (10, -10))
                    e1.animation()
                    e1_g.draw(surface)
                    i.kill()


                    asteroids.remove(i)

def rand_coord():
    return random.randrange(200, WindowWidth), random.randrange(30, WindowHeight - 50)


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

    e = Explosion()
    e_group = pygame.sprite.Group(e)

    weapon_1 = Laser((300, (WindowHeight / 2)))


    # Generate a list of "wave_list" Asteroid objects
    wave_list = [16, 32, 64, 128]
    wave = wave_list[1]
    asteroids = [Asteroid((rand_coord())) for i in range(wave)]
    #asteroids_group = [pygame.sprite.Group(asteroids) for i in range(wave)]
    asteroids_group = [pygame.sprite.Group(asteroids)]

    # Start main game loop
    while loop:

        # Draw background image
        shoot_em_surface.blit(BG, [0, 0])

        # Draw our ship
        s.draw(shoot_em_surface)
        #s_group.draw(shoot_em_surface)

        # Animate and scroll the Asteroids
        for i in asteroids:
            i.animation()
            i.update_sprite(shoot_em_surface)
            i.is_colliding(s, e, e_group, shoot_em_surface)

        # Draw the asteroid sprite group
        asteroids_group[0].draw(shoot_em_surface)


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
        if keys[pygame.K_RIGHT]:
            s.move(2)
        print (weapon_1.charged)
        if keys[pygame.K_SPACE]:
            weapon_1.draw(shoot_em_surface, s, asteroids, asteroids_group, e, e_group)
            pygame.display.flip()
        if keys[pygame.K_x]:
            #asteroids.pop(0)
            asteroids.pop(0)
            #e.update_sprite((10, 10))
            #e_group.draw(shoot_em_surface)
            #l.update_sprite(shoot_em_surface)


# Call main
if __name__ == "__main__":
    main()
