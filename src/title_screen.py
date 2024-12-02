import pygame
from settings import WIN, WIDTH, HEIGHT, BACKGROUND_IMAGE, HEALTH_FONT, CONTROL_FONT, TITLE_FONT

def menu_options():
    """
    Display the title screen with the game's name and options.
    """
    run = True
    while run:
        WIN.blit(BACKGROUND_IMAGE, (0,0))  # Black background
        title_text = TITLE_FONT.render("Pixel Fighter 1.0", True, (255, 255, 255))
        start_text = HEALTH_FONT.render("Start Game (Press S)", True, (255, 255, 255))
        controls_text = HEALTH_FONT.render("Controls (Press C)", True, (255, 255, 255))

        # Display the title and options
        WIN.blit(title_text, ((WIDTH - title_text.get_width()) // 2, HEIGHT // 4))
        WIN.blit(start_text, ((WIDTH - start_text.get_width()) // 2, HEIGHT // 2))
        WIN.blit(controls_text, ((WIDTH - controls_text.get_width()) // 2, HEIGHT // 2 + 50))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Start the game
                    return
                if event.key == pygame.K_c:  # Show controls
                    controls_screen()

def controls_screen():
    """
    Display the controls screen.
    """
    run = True
    line_spacing = 40  # Vertical space between lines
    margin = 50        # Left and right margin for text
    while run:
        WIN.blit(BACKGROUND_IMAGE, (0,0))   # Black background
        controls_title = CONTROL_FONT.render("Controls", True, (255, 255, 255))
        controls_text = [
            "Player 1: W - Move Up, S - Move Down, A - Move Left, D - Move Right, Q - Shoot",
            "Player 2: Arrow Keys to Move, M - Shoot",
            "Press ESC to return to the title screen",
        ]

        # Render controls text
        WIN.blit(controls_title, ((WIDTH - controls_title.get_width()) // 2, HEIGHT // 4))
        for i, line in enumerate(controls_text):
            controls_line = CONTROL_FONT.render(line, True, (255, 255, 255))
            WIN.blit(controls_line, (margin, HEIGHT // 2 + i * line_spacing))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Return to the title screen
                    return
