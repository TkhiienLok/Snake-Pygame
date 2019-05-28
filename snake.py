import pygame
from constants import *


class Snake(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        # snake has three tiles initially
        # at the beginning it shows up in the middle of the screen vertically
        self.body = [[COL_COUNT // 2, ROW_COUNT // 2],
                     [COL_COUNT // 2, ROW_COUNT // 2 + 1],
                     [COL_COUNT // 2, ROW_COUNT // 2 + 2]]
        self.direction = [-1, 0]
        self.old_key = ""
        self.speed = 10
        self.lives = 5
        self.points = 0

    def set_direction(self, key):  # change the direction of snake
        if self.old_key == key:
            self.speed = 20
        # if snake's not moving down then turn up
        if key == pygame.K_UP and self.direction != [0, 1]:
            self.direction = [0, -1]
            self.old_key = key
        # if snake's not moving to the right then turn left
        elif key == pygame.K_LEFT and self.direction != [1, 0]:
            self.direction = [-1, 0]
            self.old_key = key
        # if snake's not moving right then turn left
        elif key == pygame.K_RIGHT and self.direction != [-1, 0]:
            self.direction = [1, 0]
            self.old_key = key
        # if snake's not moving up then turn down
        elif key == pygame.K_DOWN and self.direction != [0, -1]:
            self.direction = [0, 1]
            self.old_key = key

    def move(self):
        self.body.insert(0, [self.body[0][0] + self.direction[0],
                             self.body[0][1] + self.direction[1]])  # add a "cell" to the head according to direction
        self.body[0][0] = self.body[0][0] % COL_COUNT
        self.body[0][1] = self.body[0][1] % ROW_COUNT

    def draw(self, screen):
        for elem in self.body:
            screen.blit(self.image, (elem[0]*CELL_SIZE, elem[1]*CELL_SIZE,
                                     CELL_SIZE, CELL_SIZE))     # showing all snake's cells

    def after_hit(self):
        self.lives -= 1

        # go to the start point
        # show up in the middle of the screen vertically
        self.body = [[COL_COUNT // 2, ROW_COUNT // 2],
                     [COL_COUNT // 2, ROW_COUNT // 2 + 1],
                     [COL_COUNT // 2, ROW_COUNT // 2 + 2]]

        self.direction = [0, -1]

    def hit_walls(self, walls):
        hit = False

        for wall in walls:  # check hitting the walls
            head_rect = pygame.Rect(self.body[0][0] * CELL_SIZE, self.body[0][1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if wall.colliderect(head_rect):
                self.after_hit()
                hit = True

            if self.body[0] in self.body[1:]:  # check hitting itself
                self.after_hit()
                hit = True
        return hit
