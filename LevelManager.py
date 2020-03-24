from config import *
from Block import Block
from Level import Level

IMAGE_SOLID = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
IMAGE_SOLID.fill(COL_BLOCK)

IMAGE_DEADLY = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
IMAGE_DEADLY.fill(COL_DEADLY)


class LevelManager:
    def __init__(self):
        self.__level = None

    @staticmethod
    def load_level(path: str = './level/current.txt') -> Level:
        blocks = pygame.sprite.Group()
        length = 0
        y = -1
        with open(path) as f:
            for row in f:
                y += 1
                x = -1
                for block in row:
                    x += 1
                    rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    if block == '1':
                        image = IMAGE_SOLID
                    elif block == '2':
                        image = IMAGE_DEADLY
                    else:
                        continue
                    sprite = Block(int(block), rect, image)
                    blocks.add(sprite)

                if x > length:
                    length = x

            return Level(blocks, length * BLOCK_SIZE)
