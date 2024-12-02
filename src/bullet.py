import pygame

class Bullet:
    def __init__(self, x, y, width, height, velocity, image):
        """
        Initialize a bullet object.

        Parameters:
        - x, y: Starting position of the bullet.
        - width, height: Dimensions of the bullet.
        - color: Bullet color (tuple, e.g., (255, 255, 0)).
        - velocity: Bullet velocity (positive for right, negative for left).
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = velocity
        self.image = image

    def move(self):
        """update the bullet's position"""
        self.rect.x += self.velocity
    
    def is_off_screen(self, screen_width):
        """checks to see if the bullet is off the screen"""
        return self.rect.x < 0 or self.rect.x > screen_width

    def check_collision(self, target_rect):
        """check if the bullet has collided with the other player"""
        return self.rect.colliderect(target_rect)
    
    def draw(self, win):
        """render the bullet on the game window"""
        win.blit(self.image, (self.rect.x, self.rect.y))