import pygame

brick_width = 75
brick_height = 25

class Brick:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.width = brick_width
        self.height = brick_height
        
    def draw(self, screen):
        pygame.draw.rect(
            screen, 
            self.color, 
            (self.x, self.y, self.width, self.height)
        )