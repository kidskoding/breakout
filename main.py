import pygame

from lose_screen import display_lose_screen
from paddle import Paddle, paddle_width
from ball import Ball
from brick_grid import BrickGrid
from win_screen import display_win_screen

pygame.init()

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

def reset_game():
    global paddle, ball, brick_grid, game_won, game_over, lives
    paddle = Paddle((screen_width - paddle_width) // 2, screen_height - 50)
    ball = Ball(screen_width // 2, screen_height // 2 - 30)
    brick_grid = BrickGrid()
    game_won = False
    game_over = False
    lives = 3

reset_game()

running = True
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and (game_won or game_over):
            mouse_pos = event.pos
            if play_again_rect.collidepoint(mouse_pos):
                reset_game()
            elif quit_rect.collidepoint(mouse_pos):
                running = False
    
    if not game_won and not game_over:
        paddle.draw(screen)
        ball.draw(screen)
        brick_grid.draw_grid(screen)
        
        keys = pygame.key.get_pressed()
        if paddle.x > 0 and (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            paddle.x -= paddle.velocity
        if (paddle.x < 640 - paddle.width
                and (keys[pygame.K_RIGHT] or keys[pygame.K_d])):
            paddle.x += paddle.velocity
        
        ball.update()
        ball.check_collision_with_paddle(paddle)
        ball.check_collision_with_walls(screen_width)
        ball.check_collision_with_bricks(brick_grid.bricks)
        if ball.y + ball.radius >= screen_height:
            lives -= 1
            if lives > 0:
                ball.reset_ball()
            else:
                game_over = True

        if not brick_grid.bricks:
            game_won = True

        for i in range(lives):
            pygame.draw.circle(
                screen,
                (175, 175, 175),
                (screen_width - (i + 1) * 30, screen_height - 30),
                10
            )
    else:
        if game_won:
            play_again_rect, quit_rect = display_win_screen(
                screen, screen_width, screen_height
            )
        if game_over:
            play_again_rect, quit_rect = display_lose_screen(
                screen, screen_width, screen_height
            )

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()