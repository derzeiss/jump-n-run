import sys

import pygame

from ApplicationError import ApplicationError
from Camera import Camera
from Keys import Keys
from LevelManager import LevelManager
from Player import Player
from config import \
    COL_BG, \
    COL_PLAYER, \
    DEBUG, \
    PLAYER_WIDTH, \
    PLAYER_HEIGHT, \
    PLAYER1_KEY_LEFT, \
    PLAYER1_KEY_RIGHT, \
    PLAYER1_KEY_JUMP, \
    PLAYER1_KEY_RUN, \
    SCREEN


class Game:
    def __init__(self):
        self.__level = None

        # lists of game objects
        self.__player: Player = self.__get_player()
        self.__blocks = None
        self.__entities = None
        self.__camera = None

        # pygame props
        self.__running: bool = True
        self.__clock = pygame.time.Clock()
        self.__screen = SCREEN
        self.__bg = None

    def load_level(self, path) -> None:
        if self.__level:
            self.__screen.blit(self.__bg, (0, 0))

        self.__level = LevelManager.load_level(path)
        self.__blocks = self.__level.get_blocks()
        self.__entities = self.__get_entities_group()
        self.__camera = Camera(self.__player, self.__level)
        self.__bg = self.__get_bg()
        self.__player.set_spawn_point(self.__level.get_player_spawn())

        self.__player.respawn()

    def __get_entities_group(self) -> pygame.sprite.Group:
        g = self.__blocks.copy()
        g.add(self.__player)
        return g

    def __get_bg(self) -> pygame.Surface:
        s = pygame.Surface(self.__camera.get_size())
        s.fill(COL_BG)
        return s

    def mainloop(self) -> None:
        if not self.__level:
            raise ApplicationError('Please load a level before starting the mainloop')

        while self.__running:
            self.__clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.__running = False

            # update
            self.__entities.update()
            self.__camera.update()

            # render
            self.__entities.clear(self.__camera, self.__bg)
            if DEBUG:
                self.__camera.blit(self.__player.render_player_debug_info(), (self.__camera.get_pos_inverted()))
            self.__entities.draw(self.__camera)

            self.__screen.blit(self.__camera, self.__camera.get_pos())

            pygame.display.flip()

        pygame.display.quit()
        pygame.quit()
        sys.exit()

    def get_blocks(self) -> pygame.sprite.Group:
        return self.__blocks

    def __get_player(self) -> Player:
        player_image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        player_image.fill(COL_PLAYER)
        player_rect = pygame.Rect(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
        player_keys = Keys(PLAYER1_KEY_LEFT, PLAYER1_KEY_RIGHT, PLAYER1_KEY_JUMP, PLAYER1_KEY_RUN)
        player = Player(self, player_keys, player_rect, player_image)
        player.respawn()
        return player
