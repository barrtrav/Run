import pygame
import functions as fn

from warrior import Warrior
from settings import Settings
from pygame.sprite import Group

def run_game():
    pygame.init()
    settings = Settings()
    pygame.display.set_caption(settings.screen_caption)
    screen = pygame.display.set_mode(settings.screen_size)

    backgrounds : Group = fn.init_background(settings, screen)
    warrior = Warrior(settings, screen)
    
    boxes = Group()
    coins = Group()

    while True:
        fn.check_events(warrior)
        
        if settings.game_active:
            fn.update_background(settings, screen, backgrounds)
            fn.update_boxes(settings, screen, warrior, boxes)
            fn.update_coins(settings, screen, warrior, coins)
            fn.update_warrior(warrior)
        
        fn.update_screen(settings, screen, backgrounds, warrior, boxes, coins)

if __name__ == "__main__":
    run_game()