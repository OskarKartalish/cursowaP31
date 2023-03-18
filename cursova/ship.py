import pygame

class Ship():
    def __init__(self, duel_game):
        self.screen = duel_game.screen
        self.screen_rect = duel_game.screen.get_rect()

        self.image = pygame.image.load('image/player2/player2__3_-removebg-preview.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center


    def blitme(self):
        self.screen.blit(self.image, self.rect)