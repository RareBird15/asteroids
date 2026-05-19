"""Projectile sprite fired by the player ship."""

import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    """Simple circular projectile that travels at constant velocity."""

    def __init__(self, x, y, velocity):
        """Create a shot at a position with a predefined velocity."""
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        """Draw the shot as a filled white circle."""
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        """Advance shot position each frame."""
        self.position += self.velocity * dt
