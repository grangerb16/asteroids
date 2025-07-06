from constants import *
import circleshape
import pygame
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 
                           pygame.Color(255,255,255), 
                           self.position,
                           self.radius,
                            2)
    
    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20.0, 50.0)
        child_angle_a = self.velocity.rotate(angle)
        child_angle_b = self.velocity.rotate(-angle)

        child_a = Asteroid(self.position.x, self.position.x, self.radius - ASTEROID_MIN_RADIUS)
        child_a.velocity = child_angle_a * 1.2

        child_b = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        child_b.velocity = child_angle_b * 1.2
        
