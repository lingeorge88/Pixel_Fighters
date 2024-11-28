import pygame
from settings import FPS, MAX_BULLETS, yellow_bullets, red_bullets, BULLET_VEL, WIDTH, RED_HIT, YELLOW_HIT, red_health, yellow_health
from helpers import draw_window, draw_winner, restart_prompt
from movement_logic import yellow_handle_movement, red_handle_movement
from game_objects import create_character_positions
from shooting_logic import handle_yellow_shooting, handle_red_shooting, handle_bullets
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

            if event.type == RED_HIT:
                red_health -= 1
                game_sounds.play_hit_sound()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                game_sounds.play_hit_sound()
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        if yellow_health <= 0:
            winner_text = "Red Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            if restart_prompt(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
                main()
            else:
                break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    pygame.quit()

if __name__ == "__main__":
    game_sounds.play_background_music()
    main()
