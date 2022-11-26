import pygame

from pygame import Surface
from settings import Settings
from pygame.sprite import Sprite

class Box(Sprite):
    def __init__(self, setings : Settings, screen : Surface):
        super().__init__()

        self.screen = screen
        self.settings = setings
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load("../images/box.bmp")
        self.rect = self.image.get_rect()
        
        self.rect.y = 650
        self.rect.x = self.screen_rect.right

    def update(self): self.rect.x -= float(self.settings.box_speed)

    def bliting(self): self.screen.blit(self.image, self.rect)