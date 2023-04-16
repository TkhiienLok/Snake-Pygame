import os

GAME_SCREEN_WIDTH = 480  # screen width
GAME_SCREEN_HEIGHT = 320  # screen height

CELL_SIZE = 10
COL_COUNT = GAME_SCREEN_WIDTH // CELL_SIZE  # column number - width in cells
ROW_COUNT = GAME_SCREEN_HEIGHT // CELL_SIZE  # column number - height in cells

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TILE_IMAGE = os.path.join(BASE_DIR, "images", "part.png")  # snake tile

# fonts
LARGE_FONT = ("Tahoma", 55)
NORM_FONT = ("Verdana", 10)
SCORE_FONT = ("Tahoma", 20)

# RGB colors
RED = (255, 50, 30)
BLUE = (50, 80, 255)
BLACK = (0, 0, 0)
TURQUOISE = (0, 230, 230)


FPS_LIMIT = 40
