import pygame

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (175, 175, 175)
        self.radius = 10
        
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.radius
        )