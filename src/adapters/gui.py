import abc
from typing import Union, List

import pygame

from domain.interfaces import (
    FontType, Position, RGB, Displayable, Color, GameKeys, GameEvent, GameEventTypes)
from domain.constants import GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT, NORM_FONT, FPS_LIMIT


class SnakeGUIInterface(abc.ABC):
    @abc.abstractmethod
    def render_text(self, txt: str, color, font=Union[FontType, None], textpos=None):
        raise NotImplementedError

    @abc.abstractmethod
    def draw_rectangle(self, rect_coords: Position):
        raise NotImplementedError


class SnakeGUI(SnakeGUIInterface):

    def __init__(self):
        self._screen = None
        self._clock = pygame.time.Clock()
        self._fps_limit = FPS_LIMIT

    def init_screen(self):
        pygame.init()
        self._screen = pygame.display.set_mode((GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))

    def render_text(self, txt: str, color: Color, font=None, textpos=None):
        font = pygame.font.SysFont(font[0], font[1]) if font else pygame.font.SysFont(*NORM_FONT)
        text = font.render(txt, True, color)
        if textpos is None:
            textpos = text.get_rect(centerx=GAME_SCREEN_WIDTH / 2, centery=GAME_SCREEN_HEIGHT / 2)
        self._screen.blit(text, textpos)

    def draw_rectangle(self, rect_coords: Position, *color: Color):
        pygame.draw.rect(
            self._screen,
            pygame.Color(*color),
            pygame.Rect(rect_coords.coordinates,
                        rect_coords.dimensions),
            0)

    def fill_with(self, color: RGB):
        self._screen.fill(color)

    def draw(self, displayable_items: Displayable):
        for item in displayable_items.images:
            self._screen.blit(
                pygame.transform.scale(pygame.image.load(item["source"]), item["destination"].dimensions),
                item["destination"].coordinates
            )
        for item in displayable_items.figures:
            self.draw_rectangle(item["destination"], item["color"])

    @staticmethod
    def update_display_to_screen():
        pygame.display.flip()

    @staticmethod
    def rectangles_collide(will_stay: Position, will_disappear: Position) -> bool:
        return pygame.Rect(*will_stay.coordinates, *will_stay.dimensions).colliderect(
            pygame.Rect(*will_disappear.coordinates, * will_disappear.dimensions)
        )

    @staticmethod
    def wait(milliseconds: int):
        pygame.time.wait(milliseconds)

    @staticmethod
    def get_events() -> List[GameEvent]:
        event_type_map = {
            pygame.QUIT: GameEventTypes.QUIT,
            pygame.KEYDOWN: GameEventTypes.KEYDOWN,
            pygame.KEYUP: GameEventTypes.KEYUP,
            pygame.WINDOWCLOSE: GameEventTypes.QUIT,
        }

        key_map = {
            pygame.K_LEFT: GameKeys.LEFT,
            pygame.K_RIGHT: GameKeys.RIGHT,
            pygame.K_UP: GameKeys.UP,
            pygame.K_DOWN: GameKeys.DOWN,
        }

        def is_key_event(event_type: int) -> bool:
            return event_type in [pygame.KEYDOWN, pygame.KEYUP]

        def can_handle_event(event_type: int) -> bool:
            return event_type in event_type_map.keys()

        def can_handle_key(key_kode: int) -> bool:
            return key_kode in key_map.keys()
        return [
            GameEvent(
                type=event_type_map[event.type],
                key=key_map[event.key] if is_key_event(event.type) else None
            )
            for event in pygame.event.get()
            if can_handle_event(event.type) and (
                    (
                            is_key_event(event.type) and can_handle_key(event.key)
                            or not is_key_event(event.type)
                    )
            )
        ]

    @staticmethod
    def set_caption(caption: str):
        pygame.display.set_caption(caption)

    def trigger_next_frame(self, limit: int):
        self._clock.tick(limit) if limit <= self._fps_limit else self._fps_limit

    @staticmethod
    def quit():
        pygame.quit()


snake_gui = SnakeGUI()

