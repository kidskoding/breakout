import pygame

brick_width = 75
brick_height = 25

class Brick:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        
    def draw(self, screen):
        pygame.draw.rect(
            screen, 
            self.color, 
            (self.x, self.y, brick_width, brick_height)
        )