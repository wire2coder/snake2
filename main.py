# python v3.10
# need to install 'pygame'
# https://www.youtube.com/watch?v=8dfePlONtls&list=WL&index=3&t=12s
# https://github.com/codebasics/python_projects/tree/main/1_snake_game

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import time
import os
import pygame
from pygame.locals import *

import logging
logging.basicConfig(level=logging.INFO)


MAX_SNAKE_SIZE = 40

class Snake:
    def __init__(self, game_window, snake_length):
        # 1. get 'game_window' from game 'class'
        self.game_window = game_window

        # 2. load the block.jpg
        self.block = pygame.image.load("resources/block.jpg")  # of an image file

        # 3. set 'starting position' for block.jpg
        # self.x_position = 100
        # self.y_position = 100
        self.snake_length = snake_length
        self.x_position = [MAX_SNAKE_SIZE] * snake_length # MAX_SNAKE_SIZE is 40
        self.y_position = [MAX_SNAKE_SIZE] * snake_length

        # start by moving to the right, 'by yourself'
        # every 1 second
        self.current_direction = 'right'

    def draw_block(self):
        self.game_window.fill((110, 110, 5))  # 'erase' previous 'block.jpg' by filling background color

        # 'draw stuff' in each 'location' inside the 'array'
        for index in range(self.snake_length):
            self.game_window.blit(self.block, (self.x_position[index], self.y_position[index]))  # 'draw' 'block.jpg' at new location

        pygame.display.flip()  # 'display the game window'

    def move_up(self):
        # decrease y-axis value by 10 (reversed y position)
        # self.y_position -= 10
        # draw the 'game window' and 'snake'
        # self.draw_block()
        self.current_direction = 'up'

    def move_down(self):
        self.current_direction = 'down'

    def move_left(self):
        self.current_direction = 'left'

    def move_right(self):
        self.current_direction = 'right'

    def auto_move(self): # the -1 at the 'end' means 'count backward'
        # import pdb
        # pdb.set_trace()
        asdf_snake_length = self.snake_length-1
        for index in range(self.snake_length-1, 0, -1):

            # put stuff in position 9 into position 8
            asdf1 = self.x_position[index - 1]
            asdf2 = self.x_position[index]
            # logging.info(f'x_pos now: {asdf2}')


            self.x_position[index] = self.x_position[index - 1]
            self.y_position[index] = self.y_position[index - 1]

        if self.current_direction == 'up':
            self.y_position[0] -= 40
        elif self.current_direction == 'down':
            self.y_position[0] += 40
        elif self.current_direction == 'left':
            self.x_position[0] -= 40
        elif self.current_direction == 'right':
            self.x_position[0] += 40 # add 40 to the 'first item' in the array, # this 40 is a different 40 from 'SIZE'

        self.draw_block()

class Game:
    def __init__(self):
        # 1. make game 'window'
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))

        # 2. fill background color for the 'window'
        self.surface.fill((110, 110, 5))

        # 3. make a 'snake'
        self.snake1 = Snake(self.surface, 6) # the second 'argument/input' is the 'starting length' of the 'snake'

        # 4. 'draw' the snake
        self.snake1.draw_block()

        self.run_game()

    def run_game(self):
        # infinite game loop
        running = True
        while running:
            event = pygame.event.get()

            for asdf in event:
                if asdf.type == KEYDOWN:  # when the key (on keyboard) bounce up

                    if asdf.key == K_ESCAPE:
                        running = False

                    elif asdf.key == K_UP:
                        # subtract y value by 10
                        self.snake1.move_up()  # decrease y-axis by 10

                    elif asdf.key == K_DOWN:
                        # increase y value by 10
                        self.snake1.move_down()

                    elif asdf.key == K_LEFT:
                        # subtract X value by 10, 'refactor' instructions into a function
                        self.snake1.move_left()

                    elif asdf.key == K_RIGHT:
                        # increase X value by 10
                        self.snake1.move_right()

                elif asdf.type == QUIT:
                    running = False

            # print(f"start debug here")
            self.snake1.auto_move()
            time.sleep(1)  # 0.4 second


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(f"start debug here")
    gameWindow1 = Game() # make a 'game window' and 'snake'
    gameWindow1.run_game() # run the 'infinite event loop'






