from typing import Tuple
from random import randrange

from ..interfaces import Drawable, Displayable, Position
from ..constants import *


class Apple(Drawable):

    count = 0

    def __init__(self, size):
        self.x, self.y = self.generate_random_coordinates()
        self.size = size

    @staticmethod
    def generate_random_coordinates() -> Tuple[int, int]:
        return randrange(1, COL_COUNT - 1), randrange(1, ROW_COUNT-1)

    def set_random_position(self):                    # change apple position
        self.x, self.y = self.generate_random_coordinates()

        if Apple.count % 3 == 0:    # each 3d apple is going to be bigger
            self.size = CELL_SIZE + 6
        else:
            self.size = CELL_SIZE

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
