import pygame

class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()


        # Start each new ship at the mid left of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value of the ships vertical position.
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_top = False
        self.moving_down = False

    def update(self, dt):
        '''Update the ships position based on the movement flag.'''
        if self.moving_top and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < 800:
            self.rect.y += self.settings.ship_speed

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)