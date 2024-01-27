class Settings:
    '''A class to store all the settings for Sideways shooter'''

    def __init__(self):
        '''Initialize the games settings.'''
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (20, 100, 200)

        # Ship settings
        self.ship_speed = 10

        self.bullet_speed = 10.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)

        # Alien settings
        self.alien_speed = 20 # 2.0
        self.fleet_drop_speed = 50
        # fleet_direction of 1 represents down; -1 represents up.
        self.fleet_direction = 1

        
