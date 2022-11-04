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


class Snake:
    def __init__(self, game_window):
        # 1. get 'game_window' from game 'class'
        self.game_window = game_window

        # 2. load the block.jpg
        self.block = pygame.image.load("resources/block.jpg")  # of an image file

        # 3. set 'starting position' for block.jpg
        self.x_position = 100
        self.y_position = 100

    def draw_block(self):
        self.game_window.fill((110, 110, 5))  # 'erase' previous 'block.jpg' by filling background color
        self.game_window.blit(self.block, (self.x_position, self.y_position))  # 'draw' 'block.jpg' at new location

        pygame.display.flip()  # 'display the game window'


class Game:
    def __init__(self):
        # 1. make game 'window'
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))

        # 2. fill background color for the 'window'
        self.surface.fill((110, 110, 5))

        # 3. make a 'snake'
        self.snake1 = Snake(self.surface)

        # 4. 'draw' the snake
        self.snake1.draw_block()

        # infinite game loop
        running = True
        while running:
            event = pygame.event.get()

            for asdf in event:
                if asdf.type == KEYUP:  # when the key (on keyboard) bounce up
                    if asdf.key == K_ESCAPE:
                        running = False
                    if asdf.key == K_UP:
                        # subtract y value by 10
                        self.snake1.y_position -= 10  # decrease y-axis by 10
                        self.snake1.draw_block()
                    if asdf.key == K_DOWN:
                        # increase y value by 10
                        self.snake1.y_position += 10
                        self.snake1.draw_block()
                    if asdf.key == K_LEFT:
                        # subtract X value by 10
                        self.snake1.x_position -= 10
                        self.snake1.draw_block()
                    if asdf.key == K_RIGHT:
                        # increase X value by 10
                        self.snake1.x_position += 10
                        self.snake1.draw_block()

                if asdf.type == QUIT:
                    running = False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    gameWindow1 = Game()







