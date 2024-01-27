import sys
import pygame

class EmptyGame:
    def __init__(self):
        '''Initialize  the game, and create game resources'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('GangGang')

    def run_game(self):
        '''Start the main loop.'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if pygame.KEYDOWN:
                    print(event)
            pygame.display.flip()

if __name__ == '__main__':
    ai = EmptyGame()
    ai.run_game()