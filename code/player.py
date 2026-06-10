#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import name

import pygame

from code.PlayerShot import PlayerShot
from code.const import WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, \
    PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.entity import Entity


class Player(Entity):
    def __init__(self, nome: str, position: tuple):
        super().__init__(nome, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]


    def update(self):
        pass

    def move(self, ):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= 2.5
        if pressed_keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += 2.5
        if pressed_keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= 2.5
        if pressed_keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += 2.5
        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(nome=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))