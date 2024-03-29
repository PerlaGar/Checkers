import pygame
import sys
from game.constants import WIDTH, HEIGHT, WHITE
from game.board import Board
from game.piece import Piece
from game.event_handler import EventHandler

pygame.init()

WINDOWS = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Checkers')

board = Board()
board.initialize_pieces()
event_handler = EventHandler(board)
while True:
    for event in pygame.event.get():
        event_handler.handle_event(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    board.draw_squares(WINDOWS)  # draw the board with pieces
    pygame.display.flip()  # update the full display Surface to the screen
