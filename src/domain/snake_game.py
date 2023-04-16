import sys

from src.adapters.gui import snake_gui
from src.domain.interfaces import GameEventTypes, Result, Color
from src.domain.constants import (
    TILE_IMAGE,
    CELL_SIZE,
    SCORE_FONT,
    TURQUOISE,
    BLACK,
    LARGE_FONT,
    BLUE,
    RED,
)
from src.domain.models.apple import Apple
from src.domain.models.snake import Snake
from src.domain.models.user import GameUser
from src.domain.models.walls import Walls, WallsType
from src.adapters.repository import save_result


class SnakeGame:
    def __init__(self, player: GameUser):
        self.game_over = False
        snake_gui.init_screen()
        self.player = player
        self._snake = Snake(TILE_IMAGE)
        self._apple = Apple(CELL_SIZE)
        self._seconds_before_start = 3
        self._points = 0

        snake_gui.set_caption(f'Snake-{player.get_name()}')

        self.walls_list = Walls(WallsType.EASY_PARALLEL).get_list(CELL_SIZE)  # TODO: let the user choose what type of obstacles he wants

    @staticmethod
    def _print_text(text: str, color: Color, font=None, textpos=None):
        snake_gui.render_text(text, color, font, textpos)
        snake_gui.update_display_to_screen()

    def _show_status_text(self):
        text = "Apples:{} Points: {} Lives: {} ".format(self._apple.count, self._points, "-" * self._snake.lives)
        snake_gui.render_text(text, TURQUOISE, SCORE_FONT, (10, 10))

    def _draw_walls(self):
        for wall in self.walls_list:
            snake_gui.draw_rectangle(wall, BLUE)

    def _countdown(self):
        while self._seconds_before_start > 0:
            self._print_text("{}".format(self._seconds_before_start), BLUE, LARGE_FONT)
            snake_gui.wait(1000)
            snake_gui.fill_with(BLACK)
            self._seconds_before_start -= 1

    def _draw_game_objects(self):  # TODO: add images preloading
        snake_gui.fill_with(BLACK)
        self._show_status_text()
        self._draw_walls()
        objects = [self._snake, self._apple]
        for obj in objects:
            snake_gui.draw(obj.drawable_objects_and_destinations)
        snake_gui.update_display_to_screen()

    def _increase_points(self, points: int):
        self._points += points

    def quit(self):
        snake_gui.quit()
        sys.exit()

    def _handle_user_events(self):
        for event in snake_gui.get_events():
            if event.type.value == GameEventTypes.QUIT.value:
                self.quit()
            elif event.type.value == GameEventTypes.KEYDOWN.value:
                self._snake.set_direction(event.key)
            elif event.type.value == GameEventTypes.KEYUP.value:
                self._snake.slow_down_default()

    def _move_snake(self):
        self._snake.move_head()

        touched_apple = snake_gui.rectangles_collide(self._snake.head_position, self._apple.position)
        if touched_apple:
            self._increase_points(self._apple.size)
            self._apple.set_random_position()
            Apple.count += 1
        else:
            self._snake.remove_tail()

        if self._snake.hit_walls(self.walls_list) or self._snake.hit_itself():
            if self._snake.is_alive():
                self._snake.start_new_live()
                self._apple.set_random_position()
            else:
                self._print_text("GAME OVER", RED, LARGE_FONT)
                self.game_over = True

    def _handle_one_frame(self):
        self._handle_user_events()
        self._draw_game_objects()
        self._move_snake()
        snake_gui.trigger_next_frame(self._snake.speed)

    def start(self):
        self._countdown()
        while not self.game_over:
            self._handle_one_frame()

        save_result(Result(player_name=self.player.get_name(), apples=Apple.count, points=self._points))
        snake_gui.wait(2000)
