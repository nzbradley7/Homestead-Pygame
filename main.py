import pygame, my, sprite, board, input, sys, logic

handler = logic.Handler()

while not my.GAME_EXIT:
    #Compute physics
    delta_time = my.CLOCK.tick(my.FPS)
    #Handle events
    handler.update()
    #Draw objects
    #screen.fill(colours['white'])
    pygame.display.update()
    my.CLOCK.tick(my.FPS)
    
pygame.quit()
sys.exit()
