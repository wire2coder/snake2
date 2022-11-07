# python v3.10
# need to install 'pygame'
# https://www.youtube.com/watch?v=8dfePlONtls&list=WL&index=3&t=12s
# https://github.com/codebasics/python_projects/tree/main/1_snake_game
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import time
import os
from datetime import datetime
import pygame
from pygame.locals import *

import logging
logging.basicConfig(level=logging.INFO)

# Constant Variable
GAME_WINDOW_WIDTH = 1000
GAME_WINDOW_HEIGHT = 800
MAX_SNAKE_SIZE = 40 # don't confuse this 40 with the 'image size' of 40 pixels for 'block.jpg'
STARTING_SNAKE_LENGTH = 1

class Apple:
    def __init__(self, game_window):
        # 1 get the 'game window'
        self.game_window = game_window

        # 2 load the image
        self.apple_img = pygame.image.load("./resources/apple.jpg")

        # 3 x_position and y position
        self.x_position = MAX_SNAKE_SIZE * 3 # why multiply by 3?
        self.y_position = MAX_SNAKE_SIZE * 3

    def draw_apple(self):
        self.game_window.blit(self.apple_img, (self.x_position, self.y_position))
        pygame.display.flip()

    def randomly_move_apple(self):
        # you have 1000 pixels (dots) in the x-axis
        # your 'block/snake head' is 40x40 pixels, so 1000 divide 40 = 25
        # so, inside that 1000 pixel, you have 25 'location' to place the 'apple' in the x-axis
        # same logic applies to the y-axis, 800 divide 40 = 20
        random_x_position = random.randint(0, 25-1) * MAX_SNAKE_SIZE # 25 * 40 = 1000, minus 1 to keep apple IN the screen
        random_y_position = random.randint(0, 20-1) * MAX_SNAKE_SIZE
        self.x_position = random_x_position
        self.y_position = random_y_position


class Snake:
    def __init__(self, game_window, snake_length=1):
        # 1. get 'game_window' from game 'class'
        self.game_window = game_window

        # 2. load the block.jpg
        self.block = pygame.image.load("resources/block.jpg")  # of an image file

        # 3. set 'starting position' for block.jpg
        # self.x_position = 100
        # self.y_position = 100
        self.snake_length = snake_length
        self.x_position = [MAX_SNAKE_SIZE] * snake_length # this is an array for (x,y) 'position'
        self.y_position = [MAX_SNAKE_SIZE] * snake_length # MAX_SNAKE_SIZE is 40

        # start by moving to the right, 'by yourself'
        # every 1 second
        self.current_direction = 'right'

    def draw_block_snake(self):
        self.game_window.fill((110, 110, 5))  # 'erase' previous 'block.jpg' by filling background color

        # 'draw stuff' in each 'location' inside the 'array'
        for index in range(self.snake_length):
            self.game_window.blit(self.block, (self.x_position[index], self.y_position[index]))  # 'draw' 'block.jpg' at new location

        pygame.display.flip()  # 'display the game window'

    def increase_snake_lenght(self):

        # adding 1 more 'block' to the 'snake
        self.snake_length += 1

        # increase x-position array by 1
        self.x_position.append(-1) # -1 means add to the 'tail'

        # increase y-position array by 1
        self.y_position.append(-1)


    def move_up(self):
        # decrease y-axis value by 10 (reversed y position)
        # self.y_position -= 10
        # draw the 'game window' and 'snake'
        # self.draw_block_snake()
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

        self.draw_block_snake()

class Game:
    def __init__(self):
        # 1. make game 'window'
        pygame.init()
        self.game_window = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))

        # 2. fill background color for the 'window'
        self.game_window.fill((110, 110, 5))

        # 3. make a 'snake'
        self.snake1 = Snake(self.game_window, STARTING_SNAKE_LENGTH) # the second 'argument/input' is the 'starting length' of the 'snake'

        # 4. 'draw' the snake
        self.snake1.draw_block_snake()

        # 5 make an Apple
        self.apple1 = Apple(self.game_window)

        # 6 draw the Apple
        self.apple1.draw_apple()

        self.run_game()

    def snake_apple_collision_not_use(self):
        # 'collision' (over lapping) is when you have the
        # x and y position of the sake (x, y) is THE SAME as the x and y (x, y) position of the apple
        if self.snake1.x_position[0] == self.apple1.x_position and self.snake1.y_position[0] == self.apple1.y_position:
            # logging.info(f'collided {datetime.now()}')
            return True
        return False

    def snake_snake_collision_not_use(self):
        # everything in snake x_position and y_position array
        # tell me why we started at 'index 3' ?
        # because we don't count the 'head' at index 0 and the body part 1 and 2
        # so, if the value in the 'head' ( x,y at index 0) DOES EXIST in the x_position array and y_position array

        # snake_head_x_y_value = self.snake1.x_position[0] and self.snake1.y_position[0]
        if self.snake1.x_position[0] in self.snake1.x_position[3 : : ]:
            if self.snake1.y_position[0] in self.snake1.y_position[3 : : ]:
                logging.info(f"SS collision x_pos {self.snake1.x_position[0]}, y_pos {self.snake1.y_position[0]}")

    def detect_collision(self, x1, y1, x2, y2): # look at the diagram for explanation for this 'logic'
        # don't confuse this 40 with the 'image size' of 40 pixels for 'block.jpg'
        if x1 >= x2 and x1 <= x2 + MAX_SNAKE_SIZE: # x2 is a number, (x2 + MAX_SNAKE_SIZE) is just another number
            if y1 >= y2 and y1 <= y2 + MAX_SNAKE_SIZE:
                # logging.info("2 things is collided")
                return True

    def display_score_snake_length(self):
        font1 = pygame.font.SysFont('arial', 30)
        score1 = font1.render(f"Current Score: {self.snake1.snake_length}", True, (255, 255, 255))
        current_apple_position = font1.render(f"Current Apple Location: {self.apple1.x_position}, {self.apple1.y_position}", True, (255,255,255))
        current_snake_head_pos = font1.render(f"Current Snake head pos: {self.snake1.x_position[0]} {self.snake1.y_position[0]}", True, (255, 255, 255))
        self.game_window.blit(score1, (600, 10))
        self.game_window.blit(current_apple_position, (600, 50))
        self.game_window.blit(current_snake_head_pos, (600, 100))
        pygame.display.flip()  # 'display the game window'


    def show_game_over_message(self):
        font1 = pygame.font.SysFont('arial', 30)
        line1 = font1.render(f"Game Over, your score is {self.snake1.snake_length}", True, (255, 255, 255))
        line2 = font1.render(f"Press Enter is Restart Game", True, (255, 255, 255))
        self.game_window.blit(line1, (GAME_WINDOW_WIDTH/2, GAME_WINDOW_HEIGHT/2))
        self.game_window.blit(line2, (GAME_WINDOW_WIDTH/2, (GAME_WINDOW_HEIGHT/2)+40))
        pygame.display.flip()

    def play_game_draw_all_objects(self):
        self.snake1.auto_move()
        self.apple1.draw_apple()
        self.display_score_snake_length()
        # pygame.display.flip()  # 'display the game window'

        # collision logic for 'snake' and 'apple'
        collided = self.detect_collision(self.snake1.x_position[0], self.snake1.y_position[0], self.apple1.x_position, self.apple1.y_position)
        if collided:
            # play the 'ding.mp3'
            ding1 = pygame.mixer.Sound("resources/ding.mp3")
            pygame.mixer.Sound.play(ding1)
            self.apple1.randomly_move_apple()
            self.snake1.increase_snake_lenght()

        # 'head of snake[0]' and 'snake body' collision logic
        # tell me why range() starts at index 3
        for index in range(3, self.snake1.snake_length):
            if self.detect_collision(self.snake1.x_position[0], self.snake1.y_position[0], self.snake1.x_position[index], self.snake1.y_position[index]):
                raise "Game over" # making an 'Exception'

    def reset_game(self):
        # reset the 'length of the snake to 1'
        # reset the x,y position array to 1
        # reset the 'score' to 1 (same as snake_length variable)
        # reset the 'moving direction' to 'right'
        # self.snake1.snake_length = 1
        # self.snake1.x_position = [MAX_SNAKE_SIZE] * self.snake1.snake_length
        # self.snake1.y_position = [MAX_SNAKE_SIZE] * self.snake1.snake_length
        # self.snake1.current_direction = 'right'

        # put 'apple' into a new 'random position'
        # self.apple1.randomly_move_apple()

        # just make a 'new object' with the same name?
        self.snake1 = Snake(self.game_window, STARTING_SNAKE_LENGTH)
        self.apple1 = Apple(self.game_window)

    def run_game(self):
        # infinite game loop
        running = True
        pause_game = False
        while running:
            event = pygame.event.get()

            for asdf in event:
                if asdf.type == KEYDOWN:  # when the key (on keyboard) bounce up

                    if asdf.key == K_RETURN and pause_game == True:
                        # self.reset_game() # for debugging
                        pause_game = False

                    if asdf.key == K_ESCAPE:
                        running = False

                    if not pause_game: # don't do stuff below if the game is 'pause'

                        if asdf.key == K_UP:
                            # subtract y value by 10
                            self.snake1.move_up()  # decrease y-axis by 10

                        if asdf.key == K_DOWN:
                            # increase y value by 10
                            self.snake1.move_down()

                        if asdf.key == K_LEFT:
                            # subtract X value by 10, 'refactor' instructions into a function
                            self.snake1.move_left()

                        if asdf.key == K_RIGHT:
                            # increase X value by 10
                            self.snake1.move_right()

                elif asdf.type == QUIT:
                    running = False

            # print(f"start debug here")
            try:
                if pause_game == False:
                    self.play_game_draw_all_objects()
            except Exception as e:
                pause_game = True
                self.show_game_over_message()
                self.reset_game()

            time.sleep(0.3)  # 0.4 second


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(f"start debug here")
    gameWindow1 = Game() # make a 'game window' and 'snake'
    gameWindow1.run_game() # run the 'infinite event loop'






