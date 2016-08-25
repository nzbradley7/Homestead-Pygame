import pygame

COLOURS = {'red1' : (178,27,9), 
           'red2' : (255,73,50),
           'red3' : (255,50,25),
           'green2' : (0,178,88),
           'green1' : (25,255,139),
           'white' : (255,255,255)}

SPRITES = []

WINDOWED_MODE = True
GAME_EXIT = False

pygame.init()

screenInfo = pygame.display.Info()

if WINDOWED_MODE:
	WINDOW_WIDTH = screenInfo.current_w  - 300#- 200
	WINDOW_HEIGHT = screenInfo.current_h - 300# - 200
	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	
if not WINDOWED_MODE:
	WINDOW_WIDTH = screenInfo.current_w
	WINDOW_HEIGHT = screenInfo.current_h
	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
	
pygame.display.set_caption('RPG')