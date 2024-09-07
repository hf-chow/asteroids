from types import new_class
import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            split_a_velocity = self.velocity.rotate(split_angle) 
            split_b_velocity = self.velocity.rotate(-split_angle) 
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split_a = Asteroid(self.position.x, self.position.y, new_radius)
            split_b = Asteroid(self.position.x, self.position.y, new_radius)
            split_a.velocity = split_a_velocity * 1.2
            split_b.velocity = split_b_velocity * 1.2
           
