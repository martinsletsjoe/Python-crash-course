import sys
import pygame

from star import Star
from settings import Settings
from random import randint

class StarArray:
    '''Overall class to manage game assets and behaviour'''

    def __init__(self):
        '''Initialize the game.'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('StarGrid')

        self.star = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        '''Start the main loop for the program.'''
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        '''Respond to keypresses and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_fleet(self):
        '''Create a fleet of stars'''
        # self.star.empty()
        # min_x = 0
        # max_x = self.settings.screen_width
        # min_y = 0
        # max_y = self.settings.screen_height
        # number_of_stars = randint(0,11)
        # for i in range(number_of_stars):
        #     star = Star(self)
        #     star.rect.x = randint(min_x, max_x)
        #     star.rect.y = randint(min_y, max_y)
        #     self.star.add(star)
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_star_x = available_space_x // ( 2 * star_width)

        available_space_y = (self.settings.screen_height) - (3 * star_height)
        number_rows = available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_star_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        '''Create a star and place it in the row.'''
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star_height * row_number
        self.star.add(star)

    def _update_screen(self):
        '''Update images on the screen, and flup to the new screen.'''
        # Redraw the screen during each åass through the loop.
        self.screen.fill(self.settings.bg_colour)

        for star in self.star.sprites():
            star.y += self.settings.fleet_drop_speed
            star.rect.y = float(star.y)

            if star.rect.y >= self.settings.screen_height:
                self.star.remove(star)

        if not self.star:
            self._create_fleet()


        self.star.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    ai = StarArray()
    ai.run_game()