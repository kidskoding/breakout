import pygame

paddle_width = 100
paddle_height = 20

class Paddle:
    def __init__(self, x, y):
        self.color = (175, 175, 175)
        self.x = x
        self.y = y
        self.width = paddle_width
        self.height = paddle_height
        self.velocity = 0.3
        
    def draw(self, screen):
        pygame.draw.rect(
            screen, 
            self.color,
            (self.x, self.y, paddle_width, paddle_height)
        )