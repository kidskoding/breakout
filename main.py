import pygame
from brick_grid import BrickGrid

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout")

brick_grid = BrickGrid()

running = True
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    brick_grid.draw_grid(screen)
    
    pygame.display.flip()
    
pygame.quit()