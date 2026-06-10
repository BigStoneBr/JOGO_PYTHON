from code.const import ENTITY_SPEED
from code.entity import Entity


class EnemyShot(Entity):
    def __init__(self, nome: str, position: tuple):
        super().__init__(nome, position)


    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]