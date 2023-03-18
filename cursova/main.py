import pygame
import sys
from ship import Ship
from settings import Settings


class Duel:
    def __init__(self):

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Duel")
        self.ship = Ship(self.ship.screen)


    def run_game(self):
        while True:
            self.screen.blit(self.settings.bg_image, (0, 0))
            self.screen.blit(self.settings.settings_font, (560, 100))
            platform = pygame.draw.rect(self.screen, 'White', (200, 500, 800, 10), (100))  # Позиція об'єкта
            self.ship.blitme()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()

if __name__ == '__main__':
    run_game = Duel()
    run_game.run_game()