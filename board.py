import pygame, my, random

def loadTerrainImg(terrainNames):
    imgs = {}
    for name in terrainNames:
        imgs[name] = (pygame.image.load('assets/' + name + '.png').convert())
    return imgs    

class Board:
    '''Map data class'''
    IMG = loadTerrainImg(my.TERRAIN)
    
    def __init__(self):
        self.genBaseMap()
        
    def genBaseMap(self):
        self.tiles = []
        for x in range(0, my.MAP_CELLS_X):
            row = []
            for y in range(0, my.MAP_CELLS_Y):
                tile = "grass"
                if random.randint(0, my.TUSSOCK_FREQ) == 0:
                    tile = "tussock"
                row.append(tile)
            self.tiles.append(row)
    
    def genBoard(self):
        for x in range(0, my.MAP_CELLS_X):
            for y in range(0, my.MAP_CELLS_Y):
                my.screen.blit(Board.IMG[self.tiles[x][y]], (x * my.CELL_SIZE, y * my.CELL_SIZE))