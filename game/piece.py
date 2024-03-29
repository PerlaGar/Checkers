import pygame
from .constants import WIDTH, HEIGHT, BACKGROUND2, BACKGROUND1, ROWS, COLS, SQUARE_SIZE

class Piece:
    
    def __init__(self, color, row, col):
        self.color = color
        self.row= row
        self.col=col
        self.is_king = False
        self.x =0
        self.y=0

    def make_king(self):
        self.is_king= True

    def calculate_posicion(self):
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2
        return self.x, self.y

    def draw_piece(self, window):
        radius = SQUARE_SIZE // 2 - 10
        pygame.draw.circle(window, self.color, self.calculate_posicion(), radius)

