from constants import *
import circleshape
import pygame

class Shot(circleshape.CircleShape):
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

    