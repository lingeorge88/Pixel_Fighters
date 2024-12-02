import pygame
from settings import FPS, player_one_bullets, player_two_bullets, player_two_health, player_one_health, WIN
from helpers import draw_window, render_projectiles
from movement_logic import player_one_handle_movement, player_two_handle_movement
from game_objects import create_character_positions
from shooting_logic import handle_player_one_shooting, handle_player_two_shooting, handle_bullets
from game_logic import handle_hits, check_winner
from game_sound import SoundManager
from title_screen import menu_options

game_sounds = SoundManager()

def main():
    # Initialize game sound runner
    global player_two_health, player_one_health  # Ensure global variables are reset
    player_two_health = 10
    player_one_health = 10
     # Reset bullets
    player_one_bullets.clear()
    player_two_bullets.clear()

    player_two, player_one = create_character_positions()
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
            handle_player_one_shooting(event, player_one, player_one_bullets)
            handle_player_two_shooting(event, player_two, player_two_bullets)
            player_two_health, player_one_health = handle_hits(event, player_two_health, player_one_health, game_sounds)
        
        # check for winner and display corresponding messages and restarts / quits the game based on input
        winner = check_winner(player_two_health, player_one_health, player_two, player_one, player_two_bullets, player_one_bullets)

        keys_pressed = pygame.key.get_pressed()
        player_one_handle_movement(keys_pressed, player_one)
        player_two_handle_movement(keys_pressed, player_two)
        handle_bullets(player_one_bullets, player_two_bullets, player_one, player_two)
        draw_window(player_two, player_one, player_two_bullets, player_one_bullets, player_two_health, player_one_health)
        render_projectiles(player_one_bullets, player_two_bullets, WIN)

        pygame.display.update()  # Update the display to reflect changes

        if winner == "RESTART":
            main()
            break

    pygame.quit()

if __name__ == "__main__":
    game_sounds.play_background_music()
    menu_options()
    main()
