# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    ast_field = AsteroidField()

    print ("Starting asteroids!")
    print ("Screen width: 1280") 
    print ("Screen height: 720")

   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))

        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                sys.exit("Game Over!")
            for shot in shots:
                if shot.collision_check(asteroid) == True:
                    shot.kill()
                    asteroid.kill()
        for thing in drawable:
            thing.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()