import pygame

class Sprite:
    '''Class containing sprite data'''
    def __init__(self, pos_x, pos_y, sprite_name):
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.sprite = pygame.image.load(sprite_name).convert()
            
    def draw(self, screen):
            screen.blit(self.sprite, (self.pos_x, self.pos_y))    