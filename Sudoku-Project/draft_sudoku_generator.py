import math, random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen  # FIXME: ??

        self.sketched_value = None
        self.initial_value = None
        self.initially_empty = False  # Keep track of whether cell has set value or one that user enters.

    def set_initial_value(self, value):
        self.initial_value = value

    def set_initially_empty(self, value):
        self.initially_empty = value

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):  # FIXME, VISUAL
        # Draws cell and value inside (displayed if != 0).
        # Cell outlined in red if currently selected.
        pass


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        if difficulty == 30:
            self.difficulty = 'easy'
        elif difficulty == 40:
            self.difficulty = 'medium'
        elif difficulty == 50:
            self.difficulty = 'hard'
        else:
            self.difficulty = 'custom'

        self.selected_cell = None

    def draw(self):  # VISUAL
        # Draws outline of Sudoku grid, with bold lines for 3x3's
        # Draws every cell on board
        pass

    def select(self, row, col):  # VISUAL
        self.selected_cell = row * 9 + col
        # Marks cell at (row, col) on board as selected.
        # Once selected, user can edit or sketch value.
        pass

    def click(self, x, y):  # VISUAL
        # If a tuple of (x, y) coordinates is within the displayed board,
        # this function returns a tuple of the (row, col) of the cell which was clicked.
            # self.select(row, col)
            # return (row, col)
        # Otherwise, this function returns None.
        pass

    def clear(self):  # VISUAL
        c = str(self.selected_cell)
        # Clears value cell.
        # User can only remove cell value and sketched value if filled in themselves
        if not self.screen[c].initially_empty:
            return
        else:
            self.screen[c].set_cell_value(0)
        pass

    def sketch(self, value):
        c = str(self.selected_cell)
        if not self.screen[c].initially_empty:
            return
        else:
            self.screen[c].set_sketched_value(value)
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed in the top left corner of the cell using the draw() function.

    def place_number(self, value):
        c = str(self.selected_cell)
        if not self.screen[c].initially_empty:
            return
        else:
            self.screen[c].set_cell_value(value)
        # Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key.

    def reset_to_original(self):
        # Reset all cells in the board to their original values
        # (0 if cleared, otherwise the corresponding digit).
        for cell in range(0, self.width ** 2):
            if self.screen[str(cell)].initially_empty:
                self.screen[str(cell)].set_value(0)
            else:
                self.screen[str(cell)].set_value(self.screen[str(cell)].initial_value)
        pass

    def is_full(self):
        # Returns a Boolean value indicating whether the board is full or not.
        for cell in range(0, self.width ** 2):
            if self.screen[str(cell)].value == 0:
                return False
        return True

    def update_board(self):
        for i in range(0, self.width ** 2):  # Update dictionary / screen values to current list
            current_value = sudoku.board[i // 9][i % 9]

            if self.screen[str(i)].value != current_value:
                self.screen[str(i)].set_cell_value(current_value)
                if self.screen[str(i)].initial_value is None:
                    self.screen[str(i)].set_initial_value(current_value)

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x, y).
        for i in range(0, self.width ** 2):
            if self.screen[str(i)].value == 0:
                return i // 9, i % 9
        return

    def check_board(self):
        # Check whether the Sudoku board is solved correctly.
        for i in range(0, self.row_length ** 2):
            if self.screen[str(i)].value != self.screen[str(i)].initial_value:
                return False
        return True


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.box_length = int(math.sqrt(row_length))
        self.removed_cells = removed_cells
        self.board = self.initiate_board_list()

        self.screen = {}
        for i in range(0, self.row_length ** 2):
            # FIXME: What is screen lol
            cell = Cell(0, i // 9, i % 9, self.screen)  # Cell: def __init__(self, value, row, col, screen)
            self.screen[str(i)] = cell

        # Generates 2D list square board, with 0 int value at each list index.
        self.class_board = Board(self.row_length, self.row_length, self.screen, self.removed_cells)

    def initiate_board_list(self):
        board = []
        for column in range(self.row_length):
            row_fill = []
            for row in range(self.row_length):
                row_fill.append(0)
            board.append(row_fill)
        return board

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
	
	FIXME: To add: 
    '''

    def get_board(self):  # Should work
        self.class_board.update_board()
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    def print_board(self):  # Should work
        for row in self.board:
            for num in row:
                print(num, end=' ')
            print()
        print()  # FIXME: Delete when done

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''

    def valid_in_row(self, row, num):  # FIXME: Need to check
        for r in self.board[row]:
            if r == num:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''

    def valid_in_col(self, col, num):  # FIXME: Need to check
        for row in self.board:
            if row[col] == num:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):  # FIXME: Need to check
        row_start = int(row_start - (row_start % 3))
        col_start = int(col_start - (col_start % 3))
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if num == self.board[row][col]:
                    return False
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        if not self.valid_in_row(row, num):
            return False
        elif not self.valid_in_col(col, num):
            return False
        elif not self.valid_in_box(row, col, num):
            return False
        else:
            return True

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):  # FIXME: Need to check
        row_start = int(row_start - (row_start % 3))
        col_start = int(col_start - (col_start % 3))
        single_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] == 0:
                    continue
                else:
                    single_digits.remove(self.board[row][col])
        random.shuffle(single_digits)
        index_digit = 0
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] != 0:
                    continue
                else:
                    self.board[row][col] = single_digits[index_digit]
                    index_digit += 1
        return None

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):  # FIXME: Need to check
        for i in [0, 3, 6]:
            self.fill_box(i, i)
        return None

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    def remove_cells(self):  # FIXME: Need to check
        to_remove = []
        while len(to_remove) < self.removed_cells:
            cell = random.randint(0, (self.row_length ** 2) - 1)
            if cell not in to_remove:
                to_remove.append(cell)
        for cell in to_remove:
            row = int(cell // self.row_length)
            col = int(cell % self.row_length)
            self.board[row][col] = 0
            self.screen[str(cell)].set_initially_empty(True)
        return None


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    # sudoku.print_board()
    sudoku.fill_values()
    # sudoku.print_board()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    # sudoku.print_board()
    return board


# TESTING AREA:
# s = SudokuGenerator(9, 10)
board_list = generate_sudoku(9, 20)
print(board_list)