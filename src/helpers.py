from settings import FPS, WIN, WHITE, BLACK, BORDER, RESIZE_YELLOW_SPACESHIP, RESIZE_RED_SPACESHIP, RED, YELLOW, red_bullets, yellow_bullets, BACKGROUND_IMAGE, red_health, yellow_health, HEALTH_FONT, WIDTH, WINNER_FONT, HEIGHT, MENU_FONT
import pygame
"""
This is a the file that handles various helper functions like building the game background, drawing characters images on the screen, etc
"""
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit((BACKGROUND_IMAGE), (0, 0))  # Setting up back ground color
    pygame.draw.rect(WIN, BLACK, BORDER)
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width()- 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(RESIZE_YELLOW_SPACESHIP, (yellow.x, yellow.y)) # position the image, using x,y coordinates
    WIN.blit(RESIZE_RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    pygame.display.update()

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def restart_prompt(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    """
    Helper function that displays a message asking if the player(s) would like to restart or quit the game after a game concludes
    """
    WIN = pygame.display.get_surface()
    restart_text = MENU_FONT.render("Press R to Restart or E to Exit the program", True, (255, 255, 255))
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart game
                    return True
                if event.key == pygame.K_e:  # Quit game
                    pygame.quit()
                    exit()
        clock.tick(FPS)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
        if pygame.time.get_ticks() % 3200 < 2800:  # Render text slower
            WIN.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 - restart_text.get_height() // 2))
        
        pygame.display.update()