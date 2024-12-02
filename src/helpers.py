from settings import FPS, WIN, WHITE, BLACK, BORDER, BACKGROUND_IMAGE, HEALTH_FONT, WIDTH, WINNER_FONT, HEIGHT, RESIZE_PLAYER_ONE, RESIZE_PLAYER_TWO
import pygame
"""
This is a the file that handles various helper functions like building the game background, drawing characters images on the screen, etc
"""
def draw_window(player_two, player_one, player_two_bullets, player_one_bullets, player_two_health, player_one_health):
    WIN.blit((BACKGROUND_IMAGE), (0, 0))  # Setting up back ground color
    pygame.draw.rect(WIN, BLACK, BORDER)
    player_two_health_text = HEALTH_FONT.render("Health: " + str(player_two_health), 1, WHITE)
    player_one_health_text = HEALTH_FONT.render("Health: " + str(player_one_health), 1, WHITE)
    WIN.blit(player_two_health_text, (WIDTH - player_two_health_text.get_width()- 10, 10))
    WIN.blit(player_one_health_text, (10, 10))
    WIN.blit(RESIZE_PLAYER_ONE, (player_one.x, player_one.y)) # position the image, using x,y coordinates
    WIN.blit(RESIZE_PLAYER_TWO, (player_two.x, player_two.y))

    pygame.display.update()

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def render_projectiles(player_one_bullets, player_two_bullets, WIN):
    # Render bullets
        for bullet in player_one_bullets:
            bullet.draw(WIN)  # Use the Bullet class's draw method to render the image
        for bullet in player_two_bullets:
            bullet.draw(WIN)  # Use the Bullet class's draw method to render the image

def restart_prompt(player_two, player_one, player_two_bullets, player_one_bullets, player_two_health, player_one_health):
    """
    Helper function that displays a message asking if the player(s) would like to restart or quit the game after a game concludes
    """
    WIN = pygame.display.get_surface()
    restart_text = HEALTH_FONT.render("Press R to Restart or E to Exit the program", True, (255, 255, 255))
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
        draw_window(player_two, player_one, player_two_bullets, player_one_bullets, player_two_health, player_one_health)
        if pygame.time.get_ticks() % 3200 < 2800:  # Render text slower
            WIN.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 - restart_text.get_height() // 2))
        
        pygame.display.update()
