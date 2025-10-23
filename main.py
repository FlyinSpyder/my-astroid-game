#this allows us to use code from
#the open-source pygame library
#throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_limit = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    black = pygame.Color(0, 0, 0)
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #makes the X button work to close the program
                return
        screen.fill(black) 
        player1.update(dt)
        player1.draw(screen)

        pygame.display.flip()
        fps_limit.tick(60)
        dt = fps_limit.tick(60)/1000

if __name__ == "__main__":
    main()
