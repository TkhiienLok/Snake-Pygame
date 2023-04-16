import abc
import enum
from dataclasses import dataclass
from typing import NewType, Tuple, Union, List, TypedDict, Optional

Coordinates = Tuple[int, int]
Dimensions = Tuple[int, int]


@dataclass()
class Position:
    coordinates: Coordinates
    dimensions: Dimensions


FontName = NewType("FontName", str)
FontSize = NewType("FontName", int)
FontType = Tuple[FontName, FontSize]

RGB = Tuple[int, int, int]
Color = Union[str, RGB]


class GameKeys(enum.Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class GameEventTypes(enum.Enum):
    QUIT = "QUIT"
    KEYUP = "KEYUP"
    KEYDOWN = "KEYDOWN"


@dataclass
class GameEvent:
    type: GameEventTypes
    key: Optional[GameKeys]


class DisplayImage(TypedDict):
    source: str
    destination: Position


class DisplayFigure(TypedDict):
    color: Color
    destination: Position


@dataclass
class Displayable:
    images: List[DisplayImage]
    figures: List[DisplayFigure]


@abc.abstractmethod
class Drawable(abc.ABC):
    @property
    def drawable_objects_and_destinations(self) -> Displayable:
        raise NotImplementedError


@dataclass
class Result:
    player_name: str
    apples: int
    points: int
