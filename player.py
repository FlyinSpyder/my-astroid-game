import pygame
from circleshape import CircleShape
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.lives = 3
        self.hits_to_next_life = 50

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        white = pygame.Color(255, 255, 255)
        pygame.draw.polygon(screen, white, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if self.position[0] >= SCREEN_WIDTH:
                self.position[0] = 0 + .5
        if self.position[0] <= 0:
                self.position[0] = SCREEN_WIDTH -.5
        if self.position[1] >= SCREEN_HEIGHT:
                self.position[1] = 0 + .5
        if self.position[1] <= 0:
                self.position[1] = SCREEN_HEIGHT -.5
        
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_e]:
            self.strafe(dt)
        if keys[pygame.K_q]:
            self.strafe(-dt)
        if self.timer > 0:
            self.timer -= dt
        #print(self.position)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def strafe(self, dt):
        right = pygame.Vector2(0, 1).rotate(self.rotation+90)
        self.position += right * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.timer > 0:
            pass
        else:
            x = self.position[0]
            y = self.position[1]
            velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            Shot(x, y, velocity)
            self.timer = PLAYER_SHOT_COOLDOWN
