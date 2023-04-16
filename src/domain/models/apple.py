import pygame
from random import randrange

from ..interfaces import Drawable, Displayable, Position

from ..constants import *


class Apple(Drawable):

    count = 0

    def __init__(self, size):
        self.x = randrange(1, COL_COUNT-1)  # random horizontal position
        self.y = randrange(1, ROW_COUNT-1)  # random vertical position
        self.size = size
        self.rect = pygame.Rect(self.x * CELL_SIZE, self.y * CELL_SIZE, self.size, self.size)

    def set_random_position(self):                    # change apple position
        self.x = randrange(1, COL_COUNT-1)
        self.y = randrange(1, ROW_COUNT-1)
        
        self.rect.x = self.x * CELL_SIZE
        self.rect.y = self.y * CELL_SIZE

        if Apple.count % 3 == 0:    # each 3d apple is going to be bigger
            self.size = CELL_SIZE + 6
            self.rect.x -= 3
            self.rect.y -= 3
        else:
            self.size = CELL_SIZE
        self.rect.width = self.size
        self.rect.height = self.size

    @property
    def position(self) -> Position:
        return Position(
            coordinates=(self.x * CELL_SIZE, self.y * CELL_SIZE),
            dimensions=(self.size, self.size)
        )

    @property
    def drawable_objects_and_destinations(self):
        return Displayable(
            figures=[{
                "color": RED,
                "destination": self.position,
            }],
            images=[]
        )
