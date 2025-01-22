from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw (self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        break1 = pygame.math.Vector2.rotate(self.velocity, angle)
        break2 = pygame.math.Vector2.rotate(self.velocity, -angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_ast_1.velocity = break1 * 1.2
        split_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_ast_2.velocity = break2 * 1.2
