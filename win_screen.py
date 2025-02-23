import pygame

def display_win_screen(screen, screen_width, screen_height):
    font = pygame.font.Font(None, 74)
    win_text = font.render("You Win!", True, (255, 255, 255))
    screen.blit(
        win_text, 
        (screen_width // 2 - win_text.get_width() // 2, screen_height // 2 - win_text.get_height() // 2 - 100)
    )
    
    button_font = pygame.font.Font(None, 36)

    play_again_text = button_font.render("Play Again", True, (0, 0, 0))
    play_again_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2, 200, 50)
    pygame.draw.rect(screen, (255, 255, 255), play_again_rect)
    screen.blit(play_again_text, (play_again_rect.x + 40, play_again_rect.y + 10))

    quit_text = button_font.render("Quit", True, (0, 0, 0))
    quit_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 60, 200, 50)
    pygame.draw.rect(screen, (255, 255, 255), quit_rect)
    screen.blit(quit_text, (quit_rect.x + 75, quit_rect.y + 10))

    pygame.display.flip()
    
    return play_again_rect, quit_rect