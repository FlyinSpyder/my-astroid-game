#this allows us to use code from
#the open-source pygame library
#throughout this file
import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_limit = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #make groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #add Player to updateable and drawable groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable,drawable, shots)

    black = pygame.Color(0, 0, 0)
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #makes the X button work to close the program
                return
        screen.fill(black) 
        #change to use group player1.update(dt)
        #change to use group player1.draw(screen)
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(player1): # for if a player collides with an asteroid
                print("Game over!")
                return
        for astroid in asteroids:
            for shot in shots:
                if shot.collision(astroid):
                    astroid.kill()
                    shot.kill()

        pygame.display.flip()
        fps_limit.tick(60)
        dt = fps_limit.tick(60)/1000

if __name__ == "__main__":
    main()
