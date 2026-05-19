"""Common circular sprite base class with collision support."""

import pygame


class CircleShape(pygame.sprite.Sprite):
    """Base class for circular game objects used in this project."""

    def __init__(self, x, y, radius):
        """Initialize common position, velocity, and radius properties."""
        # Subclasses can define `containers` to auto-join sprite groups.
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """Draw the shape to the screen; subclasses should override."""
        pass

    def update(self, dt):
        """Update state for a frame; subclasses should override."""
        pass

    def collides_with(self, other):
        """Return True when two circular hitboxes overlap or touch."""
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
