import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(
            screen,
            white, 
            self.position,
            self.radius,
            width=2, 
            draw_top_right = False,
            draw_top_left = False,
            draw_bottom_left = False,
            draw_bottom_right = False,
        )

    def update(self, dt):
        self.position += self.velocity * dt
        