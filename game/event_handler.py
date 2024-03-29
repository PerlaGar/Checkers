import pygame
import sys
from pygame.locals import *
from .constants import WIDTH, HEIGHT, BACKGROUND2, BACKGROUND1, ROWS, COLS, SQUARE_SIZE, BLACK, WHITE
from game.board import Board


class EventHandler:
    def __init__(self, board):
        self.board = board

    def handle_quit(self):
        '''This class is for handle the QUIT event like quitting window or exiting the game'''
        pygame.quit()
        sys.exit()

    def handle_mouse_button_down(self, event):
        '''This class checks if a piece is selected and moves the piece.'''
        if event.button == 1:  #left mouse button
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row, col = self.board.get_square_p(mouse_x, mouse_y)
            selected_piece = self.board.squares[row][col]
            if self.board.selected_piece is not None:
                #check if the selected piece is not the same as the one already selected
                if self.board.selected_piece != selected_piece:
                    self.board.move_piece(self.board.selected_piece.row, self.board.selected_piece.col, row, col)
                    self.board.selected_piece = None
            elif selected_piece is not None:
                self.board.selected_piece = selected_piece


    def handle_event(self, event):
        events = {
            QUIT: self.handle_quit,
            MOUSEBUTTONDOWN: self.handle_mouse_button_down,
        }
        handler = events.get(event.type)
        if handler:
            handler(event)