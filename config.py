import pygame

# GAME
DEBUG = False
WIDTH: int = 400
HEIGHT: int = 300

# COLORS
COL_BG = pygame.Color('black')
COL_PLAYER = pygame.Color('white')
COL_BLOCK = pygame.Color('grey')
COL_DEADLY = pygame.Color('red')

# PLAYER
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20

PLAYER1_KEY_LEFT = pygame.K_LEFT
PLAYER1_KEY_RIGHT = pygame.K_RIGHT
PLAYER1_KEY_JUMP = pygame.K_d
PLAYER1_KEY_RUN = pygame.K_s

PLAYER_AX = 1  # acc when pressing / dec when not pressing left/right
PLAYER_AX_RUNNING = 1
PLAYER_AY = 1  # gravity
PLAYER_AY_JUMPING = .6  # gravity when player holds jump key

PLAYER_VX_MAX = 3  # max walking-speed
PLAYER_VX_MAX_RUNNING = 5  # max-running-speed
PLAYER_VY_MAX = 9  # jump speed & max falling speed
PLAYER_VX_JUMP_MOD = .5  # factor for vx to add to initial jump speed

# BLOCKS
BLOCK_SIZE = PLAYER_WIDTH

BLOCK_AIR = 0
BLOCK_SOLID = 1
BLOCK_DEADLY = 2

# init pygame stuff
if DEBUG:
    print('Loading fonts.....')
    pygame.font.init()
    FONT = pygame.font.SysFont('monospace', 24)
    print('Fonts loaded.')
else:
    FONT = None

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
