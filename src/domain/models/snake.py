from typing import List

from adapters.gui import snake_gui
from ..interfaces import Drawable, Displayable, Position, GameKeys
from ..constants import *


DEFAULT_SPEED = 10
SLOW_START_SPEED = 1
FAST_SPEED = 20
LIVES = 5


class Snake(Drawable):
    def __init__(self, img_path: str):
        super().__init__()
        self.image_path = img_path
        self.body = self.start_body_coordinates()
        self.direction = [-1, 0]
        self.old_key = ""
        self.speed = SLOW_START_SPEED
        self.lives = LIVES

    def is_alive(self) -> bool:
        return self.lives > 0

    def speed_up(self):
        self.speed = FAST_SPEED

    def slow_down_default(self):
        self.speed = DEFAULT_SPEED

    def set_direction(self, key: GameKeys):  # change the direction of snake
        if self.old_key == key:
            self.speed_up()
        if key.value == GameKeys.UP.value:
            self.turn_up()
        elif key.value == GameKeys.LEFT.value:
            self.turn_left()
        elif key.value == GameKeys.RIGHT.value:
            self.turn_right()
        elif key.value == GameKeys.DOWN.value:
            self.turn_down()
        self.old_key = key

    def move_head(self):
        self.body.insert(0, [self.body[0][0] + self.direction[0],
                             self.body[0][1] + self.direction[1]])  # add a "cell" to the head according to direction
        self.body[0][0] = self.body[0][0] % COL_COUNT
        self.body[0][1] = self.body[0][1] % ROW_COUNT

    def remove_tail(self) -> None:
        if self.body:
            self.body.pop()

    @property
    def head_position(self) -> Position:
        head = self.body[0]
        return Position(
            coordinates=(head[0] * CELL_SIZE, head[1] * CELL_SIZE),
            dimensions=(CELL_SIZE, CELL_SIZE)
        )

    @property
    def drawable_objects_and_destinations(self):
        return Displayable(
            figures=[],
            images=[
                {
                    "source": self.image_path,
                    "destination": Position(
                        coordinates=(elem[0] * CELL_SIZE, elem[1] * CELL_SIZE),
                        dimensions=(CELL_SIZE, CELL_SIZE),
                    )
                }
                for elem in self.body
            ])

    @staticmethod
    def start_body_coordinates():
        # go to the start point
        # show up in the middle of the screen vertically
        return [
            [COL_COUNT // 2, ROW_COUNT // 2],
            [COL_COUNT // 2, ROW_COUNT // 2 + 1],
            [COL_COUNT // 2, ROW_COUNT // 2 + 2]
        ]

    def turn_up(self):
        if self.direction != [0, 1]:
            self.direction = [0, -1]

    def turn_down(self):
        if self.direction != [0, -1]:
            self.direction = [0, 1]

    def turn_left(self):
        if self.direction != [1, 0]:
            self.direction = [-1, 0]

    def turn_right(self):
        if self.direction != [-1, 0]:
            self.direction = [1, 0]

    def start_new_live(self):
        self.lives -= 1
        self.body = self.start_body_coordinates()
        self.turn_up()

    def hit_itself(self) -> bool:
        return self.body[0] in self.body[1:]

    def hit_walls(self, walls: List[Position]):
        return any(
            snake_gui.rectangles_collide(
                self.head_position, wall) for wall in walls
        )
