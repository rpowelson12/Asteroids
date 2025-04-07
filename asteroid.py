from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        angle = random.uniform(20, 50)
        pos_angle = self.velocity.rotate(angle)
        neg_angle = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        pos_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        neg_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        pos_asteroid.velocity = pos_angle * 1.2
        neg_asteroid.velocity = neg_angle * 1.2
        

