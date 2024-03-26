import pygame
from .constants import WIDTH, HEIGHT, BACKGROUND2, BACKGROUND1, ROWS, COLS, SQUARE_SIZE

class Board: 
    '''This class represents the board for playing checkers.'''
    def __init__(self):
        self.squares =[]
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings =0    

    def draw_squares(self, window)->None:
        '''Draws the squares of the checkers board on the provided window.'''
        window.fill(BACKGROUND2)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, BACKGROUND1, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
