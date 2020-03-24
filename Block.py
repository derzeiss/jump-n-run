import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, _type: int, rect: pygame.Rect, image: pygame.Surface):
        super().__init__()

        self.type = _type
        self.rect = rect
        self.image = image
