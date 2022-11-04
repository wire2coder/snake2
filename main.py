# python v3.10
# need to install 'pygame'
# https://www.youtube.com/watch?v=8dfePlONtls&list=WL&index=3&t=12s
# https://github.com/codebasics/python_projects/tree/main/1_snake_game

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import time
import pygame
from pygame.locals import *
import os


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pygame.init()
    surface = pygame.display.set_mode((1000, 500)) # making a 'window'
    surface.fill((110, 110, 5)) # fill the window with background color

    block = pygame.image.load("resources/block.jpg") # of an image file
    x_position = 100
    y_position = 100
    surface.blit(block, (x_position, y_position))


    pygame.display.flip() # reverse the x and y axis

    # infinite game loop
    running = True
    while running:
        event = pygame.event.get()

        for asdf in event:
            if asdf.type == KEYUP: # when the key (on keyboard) bounce up
                if asdf.key == K_ESCAPE:
                    running = False
                if asdf.key == K_UP:
                    # subtract y value by 10
                    surface.fill((110, 110, 5)) # 'erase' previous 'block.jpg' by filling background color
                    y_position -= 10 # decrease y-axis by 10
                    surface.blit(block, (x_position, y_position)) # 'draw' 'block.jpg' at new location
                    pygame.display.flip() # 'display the game window'
                if asdf.key == K_DOWN:
                    # increase y value by 10
                    y_position += 10
                    surface.blit(block, (x_position, y_position))
                    pygame.display.flip()
                # if asdf.key == K_LEFT:
                #     # subtract X value by 10
                # if asdf.key == K_RIGHT:
                #     # increase X value by 10


            if asdf.type == QUIT:
                running = False
