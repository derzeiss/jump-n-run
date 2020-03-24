import pygame


class Level:
    def __init__(self, blocks: pygame.sprite.Group, length: int, player_spawn: (int, int)):
        self.__blocks = blocks
        self.__length = length
        self.__player_spawn = player_spawn

    def get_blocks(self) -> pygame.sprite.Group:
        return self.__blocks

    def get_length(self) -> int:
        return self.__length

    def get_player_spawn(self) -> (int, int):
        return self.__player_spawn
