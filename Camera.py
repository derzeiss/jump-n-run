import pygame

from Level import Level
from Player import Player
from config import WIDTH, HEIGHT

WIDTH_2 = WIDTH / 2


class Camera(pygame.Surface):
    def __init__(self, player: Player, level: Level):
        super().__init__((level.get_length(), HEIGHT))
        self.__x = 0
        self.__y = 0

        self.__player: Player = player
        self.__level: Level = level
        self.__max_x: int = 0
        self.set_level(level)  # to set max_x

    def get_pos(self):
        return self.__x, self.__y

    def get_pos_inverted(self):
        return self.__x * -1, self.__y

    def set_level(self, level: Level):
        self.__level = level
        self.__max_x = -self.__level.get_length() + WIDTH

    def update(self):
        self.__x = max(self.__max_x, min(0, WIDTH_2 - self.__player.rect.x))
