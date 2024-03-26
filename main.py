import pygame
import sys
from game.constants import WIDTH, HEIGHT
from game.board import Board

board = Board()

pygame.init()

WINDOWS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    board.draw_squares(WINDOWS)
    pygame.display.flip()

