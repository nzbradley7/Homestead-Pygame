import pygame, input, sprite, my
from pygame.locals import *

class Handler:
    '''Handles game logic'''
    def __init__(self):
        self.TEST_sprite = sprite.Sprite(10,10,"test.PNG")
        my.SPRITES.append(self.TEST_sprite)
    
    def update(self):
        my.input_handle.get()
        if pygame.locals.K_s in my.input_handle.pressed_keys:
            self.TEST_sprite.pos_y += 10
        if pygame.locals.K_w in my.input_handle.pressed_keys:
            self.TEST_sprite.pos_y -= 10        
        if pygame.locals.K_d in my.input_handle.pressed_keys:
            self.TEST_sprite.pos_x += 10
        if pygame.locals.K_a in my.input_handle.pressed_keys:
            self.TEST_sprite.pos_x -= 10        