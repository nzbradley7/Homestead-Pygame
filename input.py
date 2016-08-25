import pygame, my

class Input:
    """Handles keyboard input"""
    def __init__(self):
        self.pressed_keys = []
        
    def get(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                my.GAME_EXIT = True
            elif event.type == pygame.KEYDOWN:
                self.pressed_keys.append(event.key)
            elif event.type == pygame.KEYUP:
                for key in self.pressed_keys:
                    if event.key == key:
                        self.pressed_keys.remove(key)