from config import *
from LevelManager import LevelManager
from Keys import Keys
from Player import Player
from Level import Level
from Camera import Camera


class Game:
    def __init__(self):
        self.__level: Level = LevelManager.load_level()

        # lists of game objects
        self.__player: Player = self.__get_player()
        self.__blocks: pygame.sprite.Group = self.__level.get_blocks()
        self.__entities: pygame.sprite.Group = self.__blocks.copy()
        self.__entities.add(self.__player)

        self.__camera: Camera = Camera(self.__player, self.__level)

        # pygame props
        self.__running: bool = True
        self.__clock: pygame.time.Clock() = pygame.time.Clock()
        self.__screen: pygame.Surface = SCREEN
        self.__bg: pygame.Surface = pygame.Surface(self.__camera.get_size())

    def mainloop(self):
        while self.__running:
            self.__clock.tick()

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
            self.__camera.blit(self.__player.render_player_debug_info(), (self.__camera.get_pos_inverted()))
            self.__entities.draw(self.__camera)

            self.__screen.blit(self.__camera, self.__camera.get_pos())

            pygame.display.flip()

    def get_blocks(self) -> pygame.sprite.Group:
        return self.__blocks

    def __get_player(self) -> Player:
        player_image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        player_image.fill(COL_PLAYER)
        player_rect = pygame.Rect(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
        player_keys = Keys(PLAYER1_KEY_LEFT, PLAYER1_KEY_RIGHT, PLAYER1_KEY_JUMP)
        player = Player(self, player_keys, player_rect, player_image)
        player.respawn()
        return player
