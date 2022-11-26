import pygame

from typing import List
from settings import Settings
from pygame import Surface, Rect

class Warrior:
    def __init__(self, settings : Settings, screen : Surface):
        
        self.steps = 0
        self.state = 0

        self.count_jump = 0
        
        self.screen : Surface = screen
        self.settings : Settings = settings
        self.screen_rect = screen.get_rect()

        self.run_images = [
            pygame.image.load("../images/run_1.bmp"),
            pygame.image.load("../images/run_2.bmp"),
            pygame.image.load("../images/run_3.bmp"),
            pygame.image.load("../images/run_4.bmp"),
            pygame.image.load("../images/run_5.bmp"),
            pygame.image.load("../images/run_6.bmp"),
        ]

        self.x = 200
        self.y = 560
        
        self.update_image()

    def update_image(self):
        if self.state == 1:
            self.image = pygame.image.load("../images/jump_up.bmp")
        elif self.state == 2:
            self.image = pygame.image.load("../images/jump_down.bmp")
        else:
            if self.steps > (len(self.run_images) * self.settings.warrior_animation_speed - 1): self.steps = 0
            self.image = self.run_images[self.steps // self.settings.warrior_animation_speed]
            self.steps += 1

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        if self.state == 1:
            if self.count_jump < self.settings.warrior_count_jump:
                self.y -= self.settings.warrior_speed
                self.count_jump += 1
            else: self.state = 2
        
        elif self.state == 2:
            if self.count_jump > 0:
                self.y += self.settings.warrior_speed
                self.count_jump -= 1
            else: self.state = 0

        self.update_image()        
    
    def bliting(self): self.screen.blit(self.image, self.rect)