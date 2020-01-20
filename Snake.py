import pygame
import math


class Dimensions:
    WIDTH = 500
    HEIGHT = 400
    TILE_SIZE = 10
    ENEMY_RADIUS = 12

    @staticmethod
    def d(x0, y0, x1, y1):
        center0_x = x0 / 2
        center0_y = y0 / 2
        center1_x = x1 / 2
        center1_y = y1 / 2
        return math.floor(math.sqrt((center0_x - center1_x) ** 2 + (center0_y - center1_y) ** 2))

    @staticmethod
    def circle_square_collision(square_x, square_y, circle_x, circle_y):
        point1 = (square_x, square_y)
        point2 = (square_x + Dimensions.WIDTH, square_y)
        point3 = (square_x, square_y + Dimensions.HEIGHT)
        point4 = (square_x + Dimensions.WIDTH, square_y + Dimensions.HEIGHT)

        if Dimensions.point_distance(circle_x, circle_y, point1[0],
                                     point1[1]) < Dimensions.ENEMY_RADIUS or Dimensions.point_distance(circle_x,
                                                                                                       circle_y,
                                                                                                       point2[0],
                                                                                                       point2[
                                                                                                           1]) < Dimensions.ENEMY_RADIUS or Dimensions.point_distance(
            circle_x, circle_y, point3[0], point3[1]) < Dimensions.ENEMY_RADIUS or Dimensions.point_distance(circle_x,
                                                                                                             circle_y,
                                                                                                             point4[0],
                                                                                                             point4[
                                                                                                                 1]) < Dimensions.ENEMY_RADIUS:
            return True
        return False

    @staticmethod
    def point_distance(x0, y0, x1, y1):
        return math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)


class Colors:
    RED = (239, 18, 18)
    TURQUOISE = (18, 231, 239)
    YELLOW = (224, 239, 18)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (30, 181, 25)


class Snake:
    def __init__(self, surface, head_x, head_y, tail_size=0):
        self.head_x = head_x
        self.head_y = head_y
        self.tail_size = tail_size
        self.surface = surface
        pygame.draw.rect(self.surface, Colors.WHITE,
                         (self.head_x, self.head_y, Dimensions.TILE_SIZE, Dimensions.TILE_SIZE))
        for i in range(self.tail_size):
            pygame.draw.rect(self.surface, Colors.WHITE,
                             (self.head_x - i * Dimensions.TILE_SIZE, self.head_y, Dimensions.TILE_SIZE, Dimensions.TILE_SIZE))



class Fruit:
    def __init__(self, surface, x, y):
        self.x = x
        self.y = y
        self.surface = surface
        pygame.draw.rect(self.surface, Colors.GREEN, (self.x, self.y, Dimensions.TILE_SIZE, Dimensions.TILE_SIZE))


class Enemy:
    def __init__(self, surface, x, y, r, g, b):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        pygame.draw.circle(surface, (self.r, self.g, self.b), (self.x, self.y), Dimensions.ENEMY_RADIUS)
