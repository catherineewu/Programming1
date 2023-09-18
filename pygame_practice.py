import pygame
import sys

"""SETUP: Main"""
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((500, 600))

"""SETUP: Details"""
small_font = pygame.font.SysFont("Courier", 15)
large_font = pygame.font.SysFont("Times New Roman", 30)

# Default Sudoku Board.
grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


rectangle = pygame.Rect(100, 100, 300, 400)

running = True

while running:

    color = (255, 255, 255)
    screen.fill(color)

    for event in pygame.event.get():
        # Quit game, called by user input
        if event.type == pygame.QUIT:
            running = False



    pygame.display.update()
