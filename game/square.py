import pygame
from .constants import WIDTH, HEIGHT, BACKGROUND2, BACKGROUND1, ROWS, COLS, SQUARE_SIZE

class Square:
    '''This class represents a square on the checkers board'''

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.piece = None  #square can contain a piece

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.row * SQUARE_SIZE, self.col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        if self.piece is not None:  #if there's a piece on this square
            self.piece.draw_piece(window)  #draw the piece
