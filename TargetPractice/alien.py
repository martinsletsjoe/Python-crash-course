import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Initialize the alien and set its starting position.'''

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()


        # Start each new alien near the top right of the screen.
        screen_rect = self.screen.get_rect()
        self.rect.right = screen_rect.right - self.rect.width
        self.rect.top = 0 + self.rect.height

        self.destroyed = False
        self.alien_id = id(self)
        self.hit_count = 0  # Initialize the hit count for each alien to 0

        # Add a flag to control the aliens vertical movement direction.
        self.moving_down = True
        self.screen_rect = self.screen.get_rect()

    def alien_hit(self):
        self.hit_count += 1
        print(f"Alien hit! Alien ID: {self.alien_id}, Hits: {self.hit_count}")

        if self.hit_count >= 3:
            self.destroyed = True

    def check_edges(self):
        '''Return true if alien is at edge of screen.'''
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= screen_rect.top:
            return True

    def update(self):
        '''Move the alien to the right or left.'''
        # self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        # self.rect.y = self.y
        if self.moving_down:
            self.rect.y += self.settings.alien_speed
        else:
            self.rect.y -= self.settings.alien_speed

        # Check if the alien has reached the top or bottom of the screen.
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
            self.moving_down = not self.moving_down
