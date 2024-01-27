import pygame

class Ship:
    ''' A class to manage the ship.'''

    def __init__(self, ai_game):
        '''Initialize the ship and set its starting position.'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the left center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ships vertical position.
        self.y = float(self.rect.y)

        #movement flag
        self.moving_top = False
        self.moving_down = False

        self.hits = 0

    def ship_hit(self):
        '''check if the ship is hit, if so increment by 1.'''
        self.hits += 1
        print("Ship hit! Hits:", self.hits)

    def update(self, dt):
        '''Update the ships position based on the movement flag.'''
        if self.moving_top and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < 800:
            self.rect.y += self.settings.ship_speed

        # Update the rect object from self.y
        # self.rect.y = self.y

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)