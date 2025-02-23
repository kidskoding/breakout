import pygame
from paddle import Paddle, paddle_width
from ball import Ball
from brick_grid import BrickGrid

pygame.init()

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

paddle = Paddle((screen_width - paddle_width) // 2, screen_height - 50)
ball = Ball(screen_width // 2, screen_height // 2)
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
    
    keys = pygame.key.get_pressed()
    if paddle.x > 0 and (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        paddle.x -= paddle.velocity
    if paddle.x < 640 - paddle.width and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        paddle.x += paddle.velocity
    
    ball.update()
    ball.check_collision_with_paddle(paddle)
    ball.check_collision_with_walls(screen_width)
    if ball.y + ball.radius >= screen_width:
        ball.reset_ball()
        pygame.time.delay(1000)

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()