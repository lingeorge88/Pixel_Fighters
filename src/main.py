import pygame
from settings import FPS, yellow_bullets, red_bullets, RED_HIT, YELLOW_HIT, red_health, yellow_health, WIN
from helpers import draw_window, draw_winner, restart_prompt
from movement_logic import yellow_handle_movement, red_handle_movement
from game_objects import create_character_positions
from shooting_logic import handle_yellow_shooting, handle_red_shooting, handle_bullets
from game_logic import handle_hits, check_winner
from game_sound import SoundManager

game_sounds = SoundManager()

def main():
    # Initialize game sound runner
    global red_health, yellow_health  # Ensure global variables are reset
    red_health = 10
    yellow_health = 10
     # Reset bullets
    yellow_bullets.clear()
    red_bullets.clear()

    red, yellow = create_character_positions()
    clock = pygame.time.Clock()
    # Need to have the game running as long as we don't reach the win condition:
    # Use clock to cap how many times the while loop executes (60 times per second)
    run = True
    while run:
        
        clock.tick(FPS)
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
            ):  # if user closes the window, we terminate the game
                run = False
            handle_yellow_shooting(event, yellow, yellow_bullets)
            handle_red_shooting(event, red, red_bullets)
            red_health, yellow_health = handle_hits(event, red_health, yellow_health, game_sounds)
        
        # check for winner and display corresponding messages and restarts / quits the game based on input
        winner = check_winner(red_health, yellow_health, red, yellow, red_bullets, yellow_bullets)

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
        
        # Render bullets
        for bullet in yellow_bullets:
            bullet.draw(WIN)  # Use the Bullet class's draw method to render the image
        for bullet in red_bullets:
            bullet.draw(WIN)  # Use the Bullet class's draw method to render the image

        pygame.display.update()  # Update the display to reflect changes

        if winner == "RESTART":
            main()
            break

    pygame.quit()

if __name__ == "__main__":
    game_sounds.play_background_music()
    main()
