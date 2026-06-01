#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import WIN_WIDTH, ENTITY_SPEED
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.react.centerx -= ENTITY_SPEED[self.name]
        if self.react.right <= 0:
            self.react.left = WIN_WIDTH
        pass
