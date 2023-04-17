import enum
from typing import List

from ..constants import *
from ..interfaces import Position


class WallsType(enum.Enum):
    EASY_PARALLEL = "EASY_PARALLEL"
    ROOM_FRAME = "ROOM_FRAME"


class Walls:

    def __init__(self, walls_type: WallsType):
        self.walls_type = walls_type
        self.color = BLUE

    def get_list(self, size) -> List[Position]:
        """Creates a list of wall coordinates"""
        horizontal_walls = [
                Position(coordinates=(0, 0), dimensions=(GAME_SCREEN_WIDTH, size)),
                Position(coordinates=(0, GAME_SCREEN_HEIGHT - size), dimensions=(GAME_SCREEN_WIDTH, size)),
            ]
        if self.walls_type == WallsType.EASY_PARALLEL:
            return horizontal_walls
        if self.walls_type == WallsType.ROOM_FRAME:
            return horizontal_walls + [
                Position(coordinates=(GAME_SCREEN_WIDTH - size, 0), dimensions=(size, GAME_SCREEN_HEIGHT)),  # right wall
                Position(coordinates=(0, 0), dimensions=(size, GAME_SCREEN_HEIGHT))  # left wall
            ]
        return []
