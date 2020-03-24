import pygame


class Level:
    def __init__(self, blocks: pygame.sprite.Group, length: int):
        self.__blocks = blocks
        self.__length = length

    def get_blocks(self):
        return self.__blocks

    def get_length(self):
        return self.__length
