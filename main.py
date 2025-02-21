import pygame
from paddle import Paddle, paddle_width
from ball import Ball
from brick_grid import BrickGrid

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout")

paddle = Paddle((width - paddle_width) // 2, height - 50)
ball = Ball(width // 2, height // 2)
brick_grid = BrickGrid()

running = True
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    paddle.draw(screen)
    ball.draw(screen)
    brick_grid.draw_grid(screen)
    
    pygame.display.flip()
    
pygame.quit()