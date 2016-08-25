import pygame, my, sprite, board, input, sys, logic

pygame.init()

clock = pygame.time.Clock()
screen = my.screen
colours = my.COLOURS
my.input_handle = input.Input()
handler = logic.Handler()

while not my.GAME_EXIT:
    #Compute physics
    
    #Handle events
    handler.update()
    #Draw objects
    screen.fill(colours['white'])
    for sprite in my.SPRITES:
        sprite.draw(screen)
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
sys.exit()
