import sys
import pygame

from box import Box
from coin import Coin
from typing import List
from random import randint
from pygame import Surface
from warrior import Warrior
from settings import Settings
from pygame.sprite import Group
from background import Background

def check_events(warrior : Warrior):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_event(event, warrior)

def check_keydown_event(event, warrior : Warrior):
    if event.key == pygame.K_q: sys.exit()
    if event.key == pygame.K_SPACE:
        if warrior.state == 0: warrior.state = 1

def init_background(settings : Settings, screen : Surface) -> Group:
    backgrounds =  Group()
    backgrounds.add(Background(1, settings, screen))
    backgrounds.add(Background(2, settings, screen))
    backgrounds.sprites()[0].rect.x = 0
    settings.background_scene = 3
    return backgrounds

def update_screen(settings : Settings, screen : Surface, backgrounds : Group, warrior : Warrior, boxes : Group, coins : Group):
    for background in backgrounds:
        background.bliting()

    warrior.bliting()
    for coin in coins.sprites(): coin.bliting()
    for box in boxes.sprites(): box.bliting()

    pygame.display.flip()

def update_background(settings : Settings, screen : Surface, backgrounds : Group) -> None:
    backgrounds.update()
    backgrounds_list = backgrounds.sprites()

    if backgrounds_list[0].rect.right <= 0:
        backgrounds.remove(backgrounds_list[0])

    if backgrounds_list[-1].rect.right <= screen.get_rect().right:
        if settings.background_scene > 4: settings.background_scene = 1
        backgrounds.add(Background(settings.background_scene, settings, screen))
        settings.background_scene += 1
    
def update_warrior(warrior : Warrior): warrior.update()

def update_boxes(settings : Settings, screen : Surface, warrior : Warrior, boxes : Group):
    boxes.update()

    boxes_list = boxes.sprites()

    if boxes and boxes_list[0].rect.right <= 0: 
        boxes.remove(boxes_list[0])

    settings.box_wait_time -= 1
    
    if not settings.box_wait_time:
        boxes.add(Box(settings, screen))
        settings.box_wait_time = randint(150, 300)

    check_box_collisions(settings, warrior, boxes)

def check_box_collisions(settings : Settings, warrior : Warrior, boxes : Group):
    collision = pygame.sprite.spritecollideany(warrior, boxes)
    if collision: settings.game_active = False

def update_coins(settings : Settings, screen : Surface, warrior : Warrior, coins : Group):
    coins.update()

    coins_list = coins.sprites()

    if coins and coins_list[0].rect.right <= 0: 
        coins.remove(coins_list[0])

    settings.coin_wait_time -= 1
    
    if not settings.coin_wait_time:
        coins.add(Coin(settings, screen))
        settings.coin_wait_time = randint(100, 200)

    check_coins_collisions(settings, warrior, coins)

def check_coins_collisions(settings : Settings, warrior : Warrior, coins : Group):
    collision = pygame.sprite.spritecollideany(warrior, coins)
    if collision: coins.remove(collision)
