import sys

import pygame
from rocketsettings import RocketSettings
from Rocketbmp import Rocket

class RapidRocket:
    '''Overall class to manage game assets and behaviour.'''

    def __init__(self):
        '''Initialize the game, and create game resources.'''
        pygame.init()

        self.rocketsettings = RocketSettings()
        self.screen = pygame.display.set_mode(
            (self.rocketsettings.screen_width, self.rocketsettings.screen_height))
        pygame.display.set_caption("Rapid Rocket")

        self.rocket = Rocket(self)

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()



    def _check_events(self):
        '''Respond to keypresses and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    self.rocket.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.rocket.moving_left = True
                elif event.key == pygame.K_UP:
                    self.rocket.moving_top = True
                elif event.key == pygame.K_DOWN:
                    self.rocket.moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.rocket.moving_left = False
                elif event.key == pygame.K_UP:
                    self.rocket.moving_top = False
                elif event.key == pygame.K_DOWN:
                    self.rocket.moving_down = False
    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen'''
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.rocketsettings.bg_colour)
        self.rocket.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    ai = RapidRocket()
    ai.run_game()