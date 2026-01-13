import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import (
        LINE_WIDTH,
        ASTEROID_MIN_RADIUS,
)

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_split_vector = self.velocity.rotate(angle)
        second_split_vector = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        one = Asteroid(self.position.x, self.position.y, new_radius)
        two = Asteroid(self.position.x, self.position.y, new_radius)
        one.velocity = first_split_vector * 1.2
        two.velocity = second_split_vector * 1.2
        
