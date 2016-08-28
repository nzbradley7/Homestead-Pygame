import pygame
from pygame.locals import *

COLOURS = {'red1' : (178,27,9), 
           'red2' : (255,73,50),
           'red3' : (255,50,25),
           'green2' : (0,178,88),
           'green1' : (25,255,139),
           'white' : (255,255,255)}

KEYS = {'w' : pygame.locals.K_w,
        's' : pygame.locals.K_s,
        'a' : pygame.locals.K_a,
        'd' : pygame.locals.K_d
        }

SPRITES = []

WINDOWED_MODE = True
GAME_EXIT = False

CLOCK = pygame.time.Clock()
FPS = 60

CELL_SIZE = 50
MAP_CELLS_X = 100
MAP_CELLS_Y = 100
MAP_WIDTH = MAP_CELLS_X * CELL_SIZE
MAP_HEIGHT = MAP_CELLS_Y * CELL_SIZE

CAM_SPEED = 5

TERRAIN = ["grass", "tussock"]
TUSSOCK_FREQ = 75

pygame.init()

screen_info = pygame.display.Info()

if WINDOWED_MODE:
	WINDOW_WIDTH = screen_info.current_w  - 200
	WINDOW_HEIGHT = screen_info.current_h - 200
	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	
if not WINDOWED_MODE:
	WINDOW_WIDTH = screen_info.current_w
	WINDOW_HEIGHT = screen_info.current_h
	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
	
pygame.display.set_caption('RPG')