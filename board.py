from sudoku_generator import *
from cell import Cell
import pygame


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen

        self.difficulty = difficulty
        self.rows = 9  # Default for Sudoku
        self.difficulties = {'easy': 30, 'medium': 40, 'hard': 50}

        self.selected_cell = None

        self.board = self.initialize_board()

    def initialize_board(self):
        """Initializes board by creating instance of SudokuGenerator class.
        Parameters are number of rows and cols (default always 9), and
        number of cells removed (depends on difficulty)."""
        return generate_sudoku(self.rows, self.difficulties[self.difficulty])

    def draw(self):  # VISUAL
        """Draws outline of Sudoku grid, with bold lines for 3x3's. Draws every cell on board."""

        pass

    def select(self, row, col):  # VISUAL
        """Marks cell at (row, col) on board as selected. Once selected, user can edit or sketch value."""

        self.selected_cell = row * 9 + col
        pass

    def click(self, x, y):  # VISUAL
        """
        If a tuple of (x, y) coordinates is within the displayed board,
        this function returns a tuple of the (row, col) of the cell which was clicked.
            self.select(row, col)
            return (row, col)
        Otherwise, this function returns None.
        """

        pass

    def clear(self):  # VISUAL
        """Clears value cell. User can only remove cell value and sketched value if filled in themselves."""

        c = str(self.selected_cell)
        if not self.screen[c].initially_empty:
            return
        else:
            self.screen[c].set_cell_value(0)
        pass

    def sketch(self, value):
        """Sets the sketched value of the current selected cell equal to user entered value.
        It will be displayed in the top left corner of the cell using the draw() function."""

        c = str(self.selected_cell)
        if not self.screen[c].initially_empty:
            return
        else:
            self.screen[c].set_sketched_value(value)

    def place_number(self, value):
        """Sets the value of the current selected cell equal to user entered value.
        Called when the user presses the Enter key."""

        c = str(self.selected_cell)
        if not self.screen[c].initially_empty:
            return
        else:
            self.screen[c].set_cell_value(value)

    def reset_to_original(self):
        """Reset all cells in the board to their original values
        (0 if cleared, otherwise the corresponding digit)."""

        for cell in range(0, self.width ** 2):
            if self.screen[str(cell)].initially_empty:
                self.screen[str(cell)].set_value(0)
            else:
                self.screen[str(cell)].set_value(self.screen[str(cell)].initial_value)
        pass

    def is_full(self):
        """Returns a Boolean value indicating whether the board is full or not."""

        for cell in range(0, self.width ** 2):
            if self.screen[str(cell)].value == 0:
                return False
        return True

"""
    def update_board(self):
        # Update dictionary / screen values to current list

        for i in range(0, self.width ** 2):
            current_value = sudoku.board[i // 9][i % 9]

            if self.screen[str(i)].value != current_value:
                self.screen[str(i)].set_cell_value(current_value)
                if self.screen[str(i)].initial_value is None:
                    self.screen[str(i)].set_initial_value(current_value)
"""
    def find_empty(self):
        """Finds an empty cell and returns its row and col as a tuple (x, y)."""

        for i in range(0, self.width ** 2):
            if self.screen[str(i)].value == 0:
                return i // 9, i % 9
        return

    def check_board(self):  # FIXME: Need to be able to check in function.
        """Check whether the Sudoku board is solved correctly."""

        for i in range(0, self.row_length ** 2):
            if self.screen[str(i)].value != self.screen[str(i)].initial_value:
                return False
        return True