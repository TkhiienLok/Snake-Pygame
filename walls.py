import pygame
from constants import *


class Walls(object):
    def createList(self, size):
        ''' Creates a list of wall Rect objects.'''
        walls = []
        #walls.append(pygame.Rect((x, y), (width, height)))
        #walls.append(pygame.Rect((100, 70), (280, size)))
        #walls.append(pygame.Rect((100, 200), (280, size)))

        walls.append(pygame.Rect((0, 0), (W, size)))  # top wall
        # walls.append(pygame.Rect((W - size, 0), (size, H)))  # right wall
        walls.append(pygame.Rect((0, H - size), (W, size)))  # bottom wall
        # walls.append(pygame.Rect((0, 0), (size, H)))  # left wall
        return walls
