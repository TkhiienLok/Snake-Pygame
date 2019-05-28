from constants import *
from random import randrange
import pygame


class Apple:

    count = 0

    def __init__(self, size):
        self.x = randrange(1, COL_COUNT-1)  # random horizontal position
        self.y = randrange(1, ROW_COUNT-1)  # random vertical position
        self.size = size
        self.rect = pygame.Rect(self.x * CELL_SIZE, self.y * CELL_SIZE, self.size, self.size)
        
    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)  # drawing red square apple

    def set_random_xy(self):                    # change apple position
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


