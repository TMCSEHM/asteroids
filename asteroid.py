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
        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        one = Asteroid(self.position.x, self.position.y, new_radius)
        two = Asteroid(self.position.x, self.position.y, new_radius)
        one.velocity = a * 1.2
        two.velocity = b * 1.2
        
