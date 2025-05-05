# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

import sys

from constants import *

from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main(): 
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroidfield = AsteroidField()

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    

    while 1:
        #handle game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #draw screen
        screen.fill("black")

        #update objects
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collision_detection(asteroid):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collision_detection(asteroid):
                    shot.kill()
                    asteroid.split()

        

        #draw things
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        #cap framerate to 60hz
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
