import pygame as pg
from maze import *

_ = False

mini_map = carve_maze(grid,size)
    

class Map:
    def __init__(self,game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])

        self.get_map()

    def get_map(self):
        for j,row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i,j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] *100 , pos[1] *100 ,100 ,100),2)
         for pos in self.world_map]
