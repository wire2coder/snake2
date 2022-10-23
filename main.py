# python v3.10
# need to install 'pygame'
# https://www.youtube.com/watch?v=8dfePlONtls&list=WL&index=3&t=12s
# https://github.com/codebasics/python_projects/tree/main/1_snake_game


# This is a sample Python script.
import time
import pygame
from pygame.locals import *
import os

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def draw_block():
    surface.fill((110, 110, 5))
    surface.blit(block, (block_x, block_y)) # what's a 'blit'?
    pygame.display.flip() # update the 'screen'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((500,500))
    surface.fill((110,110,5))
    block = pygame.image.load('./resources/block.jpg', 'just a block').convert()

    block_x = 0
    block_y = 0
    surface.blit(block, (block_x, block_y))

    pygame.display.flip() # Update the full display Surface to the screen

    running = True

    while running:
        asdf1 = pygame.event.get()
        for event in asdf1:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    block_y = block_y - 10 # reverse y-direction
                    draw_block()
                if event.key == K_DOWN:
                    block_y = block_y + 10 # reverse y-direction
                    draw_block()
                if event.key == K_RIGHT:
                    block_x = block_x + 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x = block_x - 10
                    draw_block()

            elif event.type == QUIT: # this is when you click the 'x'
                running = False

    print('debug wait')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
