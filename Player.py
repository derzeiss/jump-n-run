from Keys import Keys
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, keys: Keys, rect: pygame.Rect, image: pygame.Surface):
        super().__init__()

        self.__game = game
        self.__keys = keys

        # must be public as these are pygame.sprite.Sprite props
        self.rect = rect
        self.image = image

        self.__spawn_point = (0, 0)

        self.__in_air: bool = False
        self.__vx: int = 0
        self.__vy: int = 0
        self.__ax: int = 0
        self.__ay: int = 0

    def update(self):
        self.__handle_input()
        self.__update()

    def __handle_input(self):
        keys_pressed = pygame.key.get_pressed()

        # left/right
        if keys_pressed[self.__keys.left]:
            self.__ax = -PLAYER_AX
        elif keys_pressed[self.__keys.right]:
            self.__ax = PLAYER_AX
        else:
            self.__ax = 0

        # jump
        if not self.__in_air and keys_pressed[self.__keys.jump]:
            self.__vy = -PLAYER_VY_MAX
            self.__in_air = True

    def __update(self):
        # gravity
        self.__ay = min(self.__ay + PLAYER_AY, PLAYER_AY)

        # calc vx
        self.__vx = round((self.__vx + self.__ax) * PLAYER_FRICTION, 2)
        if self.__ax == 0 and abs(self.__vx) < PLAYER_AX:
            self.__vx = 0
        elif self.__vx < -PLAYER_VX_MAX:
            self.__vx = -PLAYER_VX_MAX
        elif self.__vx > PLAYER_VX_MAX:
            self.__vx = PLAYER_VX_MAX

        # calc vy
        self.__vy = min(self.__vy + self.__ay, PLAYER_VY_MAX)
        if abs(self.__vy > PLAYER_AY): self.__in_air = True

        # set new provisional position
        self.rect = self.rect.move(self.__vx, self.__vy)

        # handle collisions
        self.__handle_collisions()

    def __handle_collisions(self):
        self.__assert_in_screen_boundaries()

        collided_blocks = pygame.sprite.spritecollide(self, self.__game.get_blocks(), False, pygame.sprite.collide_rect)
        for block in collided_blocks:
            if block.type == BLOCK_DEADLY:
                return self.respawn()

            self.rect.centery -= self.__vy
            collision_x = pygame.sprite.collide_rect(self, block)
            self.rect = self.rect.move(-self.__vx, self.__vy)
            collision_y = pygame.sprite.collide_rect(self, block)
            self.rect.centerx += self.__vx

            if collision_x:  # collision on x-axis
                should_handle = False
                if self.rect.centerx < block.rect.centerx:  # player left to block
                    if self.__vx > 0:
                        self.rect.right = block.rect.left
                        should_handle = True
                else:
                    if self.__vx < 0:
                        self.rect.left = block.rect.right
                        should_handle = True
                if should_handle:
                    self.__ax = 0
                    self.__vx = 0

            elif collision_y:  # collision on y-axis
                if self.rect.centery < block.rect.centery:  # player above block
                    if self.__ay > 0:  # only reset speed if player is falling
                        self.rect.bottom = block.rect.top
                        self.__ay = 0
                        self.__vy = 0
                        self.__in_air = False
                else:  # player beneath block
                    self.rect.top = block.rect.bottom
                    self.__ay = 0
                    self.__vy = 0

    def __assert_in_screen_boundaries(self):
        if self.rect.bottom > HEIGHT:
            self.respawn()

        if self.rect.left < 0:
            self.rect.left = 0
            self.__ax = 0
            self.__vx = 0

    def set_spawn_point(self, point: (int, int)):
        self.__spawn_point = point

    def respawn(self):
        self.rect.topleft = self.__spawn_point
        self.__ax = self.__ay = self.__vx = self.__vy = 0
        self.__in_air = True

    def render_player_debug_info(self):
        def write(text, y): surface.blit(FONT.render(text, True, COL_PLAYER), (0, y))

        surface = pygame.Surface((WIDTH, HEIGHT))

        write('ax: ' + str(self.__ax), 0)
        write('vx: ' + str(self.__vx), 15)
        write('x: ' + str(self.rect.centerx), 30)
        write('ay: ' + str(self.__ay), 45)
        write('vy: ' + str(self.__vy), 60)
        write('y: ' + str(self.rect.centery), 75)
        return surface
