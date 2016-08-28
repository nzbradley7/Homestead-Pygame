import pygame, input, sprite, my, board
from pygame.locals import *

class Handler:
    '''Handles game logic'''
    def __init__(self):
        my.board = board.Board()
        my.board.gen_board()
        my.camera = board.Camera()
        my.input_handle = input.Input()
    
    def update(self):
        my.input_handle.get()
        my.camera.update()
        my.screen.fill(my.COLOURS['white'])
        my.screen.blit(my.board.surf, my.camera.view_area)