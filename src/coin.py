import pygame

from pygame import Surface
from settings import Settings
from pygame.sprite import Sprite

class Coin(Sprite):
    def __init__(self, settings : Settings, screen : Surface):
        super().__init__()

        self.steps = 0

        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        self.coin_images = [
            pygame.image.load("../images/coin_1.bmp"),
            pygame.image.load("../images/coin_2.bmp"),
            pygame.image.load("../images/coin_3.bmp"),
            pygame.image.load("../images/coin_4.bmp"),
            pygame.image.load("../images/coin_5.bmp"),
            pygame.image.load("../images/coin_6.bmp"),
        ]

        self.y = 200
        self.x = self.screen_rect.right

        self.update_image()

    def update_image(self):
        if self.steps > (len(self.coin_images) * self.settings.coin_animation_speed - 1): self.steps = 0
        self.image = self.coin_images[self.steps // self.settings.coin_animation_speed]
        self.steps += 1

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self): 
        self.x -= float(self.settings.coin_speed)
        self.update_image()

    def bliting(self): self.screen.blit(self.image, self.rect)