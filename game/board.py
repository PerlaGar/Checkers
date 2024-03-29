import pygame
from .constants import WIDTH, HEIGHT, BACKGROUND2, BACKGROUND1, ROWS, COLS, SQUARE_SIZE, BLACK, WHITE
from game.square import Square
from game.piece import Piece

class Board:
    def __init__(self):
        self.squares = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.selected_piece =None
        self.initialize_pieces()

    def initialize_pieces(self):
        '''Initializes the pieces in the initial positions.'''
        for row in range(3):
            for col in range(COLS):
                if (row + col) % 2 == 1:
                    self.squares[row][col] = Piece(BLACK, row, col)
                    
        for row in range(5, ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 1:
                    self.squares[row][col] = Piece(WHITE, row, col)

    def draw_squares(self, window)->None:
        '''Draws the squares of the checkers board on the provided window.'''
        window.fill(BACKGROUND2)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, BACKGROUND1, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        self.draw_pieces(window)

    def draw_pieces(self, window):
        '''Draws the initial pieces on the board'''
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.squares[row][col]
                if piece:
                    piece.draw_piece(window)    

    def move_piece(self, start_row, start_col, end_row, end_col):
        '''Moves a piece from start square to end square'''
        self.selected_piece = self.squares[start_row][start_col]  
        if self.selected_piece:
            self.squares[end_row][end_col] = self.selected_piece
            self.squares[start_row][start_col] = None
            self.selected_piece.row = end_row
            self.selected_piece.col=end_col


    def get_square_p(self,x, y):
        '''Get the row and col of the square at given pixel position'''
        row= y//SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    
