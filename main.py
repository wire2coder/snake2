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

class Snake:
    # constructor
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load('./resources/block.jpg', 'just a block').convert()
        self.x = 0  # starting location for block.jpg
        self.y = 0  # starting location for block.jpg

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        self.parent_screen.blit(self.block, (self.x, self.y)) # 'draw' block.jpg on the screen
        pygame.display.flip()  # update the 'screen'

    def move_up(self): # y direction, reverse
        self.y = self.y - 10
        self.draw()
    def move_down(self):
        self.y = self.y + 10
        self.draw()
    def move_left(self): # x direction
        self.x = self.x - 10
        self.draw()
    def move_right(self):
        self.x = self.x + 10
        self.draw()

class Game:
    # constructor
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((110, 110, 5))  # fill background color

        # making an object variable
        self.snake1 = Snake(self.surface)
        self.snake1.draw()

    def run(self):

        running = True
        while running:
            asdf1 = pygame.event.get()
            for event in asdf1:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake1.move_up()
                    if event.key == K_DOWN:
                        self.snake1.move_down()
                    if event.key == K_RIGHT:
                        self.snake1.move_right()
                    if event.key == K_LEFT:
                        self.snake1.move_left()

                elif event.type == QUIT:  # this is when you click the 'x'
                    running = False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(f'start debug here')
    game1 = Game()
    game1.run()

    print('debug wait')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
