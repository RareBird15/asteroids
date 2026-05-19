"""Asteroid sprite behavior, including movement and splitting."""

import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    """A moving circular obstacle that can split into smaller asteroids."""

    def __init__(self, x, y, radius):
        """Create an asteroid at the given position with a radius."""
        super().__init__(x, y, radius)

    def draw(self, screen):
        """Draw the asteroid as an outlined white circle."""
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        """Advance asteroid position according to velocity and frame delta."""
        self.position += self.velocity * dt

    def split(self):
        """Destroy this asteroid and optionally spawn two smaller fragments."""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(random_angle)
        vector_two = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = vector_one * 1.2
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = vector_two * 1.2
