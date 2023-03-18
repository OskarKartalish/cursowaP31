import pygame

class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 675
        self.bg_image = pygame.image.load('image/bg_fon.jpg')
        self.basic_font = pygame.font.Font('fonts/basic_fonts.ttf', 40)  # Шрифт
        self.settings_font = self.basic_font.render("Duel", False, "Blue")  # Характеристика шрифта

