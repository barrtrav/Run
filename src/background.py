import pygame

from pygame import Surface
from settings import Settings
from pygame.sprite import Sprite

class Background(Sprite):
    def __init__(self, scene : int, settings : Settings, screen : Surface):
        super().__init__()

        self.screen = screen
        self.settings = settings
        
        screen_rect = screen.get_rect()

        self.image = pygame.image.load(f"../images/background_{scene}.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = screen_rect.right

    def bliting(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= self.settings.background_speed