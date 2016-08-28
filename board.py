import pygame, my, random
from pygame.locals import *

def loadTerrainImg(terrainNames):
    imgs = {}
    for name in terrainNames:
        imgs[name] = (pygame.image.load('assets/' + name + '.png').convert())
    return imgs    

class Board:
    '''Map data class'''
    IMG = loadTerrainImg(my.TERRAIN)
    
    def __init__(self):
        self.gen_base_map()
        
    def gen_base_map(self):
        self.tiles = []
        for x in range(0, my.MAP_CELLS_X):
            row = []
            for y in range(0, my.MAP_CELLS_Y):
                tile = "grass"
                if random.randint(0, my.TUSSOCK_FREQ) == 0:
                    tile = "tussock"
                row.append(tile)
            self.tiles.append(row)
    
    def gen_board(self):
        self.surf = pygame.Surface((my.MAP_WIDTH, my.MAP_HEIGHT)).convert()
        for x in range(0, my.MAP_CELLS_X):
            for y in range(0, my.MAP_CELLS_Y):
                self.surf.blit(Board.IMG[self.tiles[x][y]], (x * my.CELL_SIZE, y * my.CELL_SIZE))
                
class Camera:
    '''Camera class'''
    def __init__(self):
        self.view_area = pygame.Rect(0, 0, my.WINDOW_WIDTH, my.WINDOW_HEIGHT)
        self.focus = self.view_area.center
        
    def update(self):
        x, y = self.focus
        
        #controls
        if my.KEYS['w'] in my.input_handle.pressed_keys:
            y += my.CAM_SPEED
        if my.KEYS['s'] in my.input_handle.pressed_keys:
            y -= my.CAM_SPEED       
        if my.KEYS['a'] in my.input_handle.pressed_keys:
            x += my.CAM_SPEED
        if my.KEYS['d'] in my.input_handle.pressed_keys:
            x -= my.CAM_SPEED                
        
        self.focus = (x, y)
        self.view_area.center = self.focus