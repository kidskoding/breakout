import pygame

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (175, 175, 175)
        self.radius = 10
        self.velocity = 5
        
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.radius
        )
        
    def update(self):
        self.y += self.velocity
        
    def check_collision_with_paddle(self, paddle):
        if (self.y + self.radius >= paddle.y and
            paddle.x <= self.x <= paddle.x + paddle.width):
            self.velocity = -self.velocity