import pygame

# GAME
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
PLAYER1_KEY_JUMP = pygame.K_UP

PLAYER_AX = .8  # acc when pressing left/right
PLAYER_FRICTION = .85  # damping when neither left nor right is pressed (1 => no friction; 0 => 100% friction)
PLAYER_AY = .5  # gravity

PLAYER_VX_MAX = 3  # max move-speed
PLAYER_VY_MAX = 10  # jump speed & max falling speed

# BLOCKS
BLOCK_SIZE = PLAYER_WIDTH

BLOCK_AIR = 0
BLOCK_SOLID = 1
BLOCK_DEADLY = 2

# init font
pygame.font.init()
FONT = pygame.font.SysFont('monospace', 24)

# init pygame surfaces
BG = pygame.Surface((WIDTH, HEIGHT))
BG.fill(COL_BG)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.blit(BG, (0, 0))
