import sys
import pygame
from ship import Ship
from shooterbullets import Bullet
from alien import Alien

from settings import Settings

class SidewaysShooter:
    '''Overall class to manage game assets and behaviour'''

    def __init__(self):
        '''initialize the game'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Sideways Shooter')

        self.alien_hit_count = {}
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        clock = pygame.time.Clock()
        while True:
            dt = clock.tick(60) / 1000.0
            self._check_events()
            self.ship.update(dt)
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()


            pygame.display.flip()


    def _check_events(self):
        '''Respond to keypresses and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        '''Respond to keypresses'''
        if event.key == pygame.K_UP:
            # move ship upwards
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        '''Respond to key releases'''
        if event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group.'''
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''Update positions of bullets and get rid of old bullets.'''
        self.bullets.update()
        screen_rect = self.screen.get_rect()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= screen_rect.right:
                self.bullets.remove(bullet)
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, False)
        for bullet, hit_aliens in collisions.items():
            for alien in hit_aliens:
                self.alien_hit(alien)

        self.aliens = pygame.sprite.Group([alien for alien in self.aliens if not alien.destroyed])

        # Remove aliens from hit count dictionary if they are no longer in the game
        self.alien_hit_count = {alien: hits for alien, hits in self.alien_hit_count.items() if alien in self.aliens}

        if not self.aliens:
            # Destroy existing bullets and create a new fleet.
            self.bullets.empty()
            self._create_fleet()

    def alien_hit(self, alien):
        if alien not in self.alien_hit_count:
            self.alien_hit_count[alien] = 1
        else:
            self.alien_hit_count[alien] += 1

        print(f"Alien hit! Alien ID: {id(alien)}, Hits: {self.alien_hit_count[alien]}")

        if self.alien_hit_count[alien] >= 3:
            self.alien_hit_count.pop(alien)
            alien.destroyed = True

    def ship_hit(self):
        self.ship_hits += 1
        print(f"Ship hit! Hits: {self.ship_hits}")


    def _update_aliens(self):
        '''Check if the fleet is at an edge, then update the positions of all aliens in the fleet'''
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship.ship_hit()

    def _create_fleet(self):
        '''Create the fleet of aliens.'''
        # Make an alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_y = self.settings.screen_height - (2 * alien_height)
        number_aliens_y = available_space_y // (2 * alien_height)

        # Determine the number of rows of aliens that fit on the screen.
        ship_width = self.ship.rect.width
        available_space_x = (self.settings.screen_width - (2 * alien_width) - ship_width)
        number_rows = available_space_x // (3 * alien_width)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        '''Create an alien and place it in the row.'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.y = alien_height + 2 * alien_height * alien_number
        alien.rect.y = alien.y

        # Set the aliens initial x position to the right side of the screen
        alien.rect.x = self.settings.screen_width - alien.rect.width
        # old: alien.rect.x = alien.rect.width + 2 * alien.rect.width * row_number

        # adjust the x position based on the row number
        alien.rect.x -= 2 * alien.rect.width * row_number

        self.aliens.add(alien)

    def _check_fleet_edges(self):
        '''Respond appropriately if any aliens have reached an edge.'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''Move the entire fleet and change the fleet's direction.'''
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen'''
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

if __name__ == '__main__':
    ai = SidewaysShooter()
    ai.run_game()