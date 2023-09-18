import math
import random
import sys
import pygame
import copy


class Cell:
    def __init__(self, initial_value, row, col):
        self.row = row
        self.col = col
        self.initial_value = initial_value

        self.sketched_value = None
        self.value = copy.deepcopy(initial_value)

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value


class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.box_length = int(math.sqrt(row_length))
        self.removed_cells = removed_cells

        self.board = self.initiate_board_list()
        self.fill_values()
        self.remove_cells()

    def initiate_board_list(self):
        board = []
        for column in range(self.row_length):
            row_fill = []
            for row in range(self.row_length):
                row_fill.append(0)
            board.append(row_fill)
        return board

    def get_board(self):  # Should work
        return self.board

    def print_board(self):  # Should work
        for row in self.board:
            for num in row:
                print(num, end=' ')
            print()

    def valid_in_row(self, row, num):
        for r in self.board[row]:
            if r == num:
                return False
        return True

    def valid_in_col(self, col, num):
        for row in self.board:
            if row[col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        row_start = int(row_start - (row_start % 3))
        col_start = int(col_start - (col_start % 3))
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if num == self.board[row][col]:
                    return False
        return True

    def is_valid(self, row, col, num):
        if not self.valid_in_row(row, num):
            return False
        elif not self.valid_in_col(col, num):
            return False
        elif not self.valid_in_box(row, col, num):
            return False
        else:
            return True

    def fill_box(self, row_start, col_start):
        # FIXME: Only called at start of game, indexing specifications irrelevant.
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

    def fill_diagonal(self):
        for i in [0, 3, 6]:
            self.fill_box(i, i)
        return None

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

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        to_remove = set()
        while len(to_remove) < self.removed_cells:
            cell_to_remove = random.randint(0, (self.row_length ** 2) - 1)
            to_remove.add(cell_to_remove)
        for cell_to_remove in to_remove:
            row = int(cell_to_remove // self.row_length)
            col = int(cell_to_remove % self.row_length)
            self.board[row][col] = 0
        return None


def initiate_cell_dictionary(board):
    cells = {}
    for i in range(0, 9 ** 2):
        row = i // 9
        col = i % 9
        next_cell = Cell(board[row][col], row, col)
        cells[str(i)] = next_cell
    return cells


def get_board_coords(pos, screen_width):
    # Parameters: pos is tuple of (x-coord, y-coord), Return: (x-grid-coord, y-grid-coord)
    square_size = screen_width // 9  # Width (630) / # squares (9) = 70
    x = pos[0] // square_size
    y = pos[1] // square_size
    return x, y


def update_board_list(board, cell_dict):
    for i in range(0, 81):
        if board[i // 9][i % 9] != cell_dict[str(i)].value:
            board[i // 9][i % 9] = cell_dict[str(i)].value
    return board


def reset_cell_dict(cell_dict):
    for i in range(0, 81):
        cell_dict[str(i)].value = cell_dict[str(i)].initial_value
        cell_dict[str(i)].sketched_value = None
    return cell_dict


def check_if_board_filled(board):
    for i in range(0, 81):
        if board[i // 9][i % 9] == 0:
            return False
    return True


def check_if_solution(board):
    # Check rows
    for row in range(0, 9):
        nums = set()
        for col in range(0, 9):
            nums.add(board[row][col])
        if len(nums) < 9:
            return False

    # Check cols
    for col in range(0, 9):
        nums = set()
        for row in range(0, 9):
            nums.add(board[row][col])
        if len(nums) < 9:
            return False

    # Check boxes
    i = [0, 3, 6]
    for row_box in i:
        for col_box in i:
            nums = set()
            for row in range(row_box, row_box + 3):
                for col in range(col_box, col_box + 3):
                    nums.add(board[row][col])
            if len(nums) < 9:
                return False
    return True


def main():

    selected_cell = None

    pygame.init()
    pygame.font.init()

    """INFORMATION:"""
    # FONTS (Do NOT move outside main function)
    tiny_font = pygame.font.SysFont("timesnewroman", 25)
    button_font = pygame.font.SysFont("timesnewroman", 30)
    small_font = pygame.font.SysFont("timesnewroman", 40)
    large_font = pygame.font.SysFont("timesnewroman", 60)

    # SCREEN DIMENSIONS
    screen_width = 630
    screen_height = 720

    # COLORS
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (150, 150, 150)
    red = (255, 0, 0)
    yellow = (255, 255, 120)

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Sudoku")

    state = 1  # Default/start screen
    sudoku_instance = None

    running = True
    while running:  # Run game
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # Registers user clicks
                pos = pygame.mouse.get_pos()

                if state == 1:  # Game start screen. Options: Easy, Medium, or Hard Difficulty
                    if easy_text_rect.collidepoint(pos):
                        sudoku_instance = SudokuGenerator(9, 30)  # Change to test
                    elif medium_text_rect.collidepoint(pos):
                        sudoku_instance = SudokuGenerator(9, 40)
                    elif hard_text_rect.collidepoint(pos):
                        sudoku_instance = SudokuGenerator(9, 50)
                    if sudoku_instance:
                        cell_dict = initiate_cell_dictionary(sudoku_instance.get_board())
                        board_list = sudoku_instance.get_board()
                        state = 2

                elif state == 2:  # Game running screen. Options: Select Cell, Sketch Value, Enter Value, Reset Game,
                    # Restart Game, Exit Game
                    if reset_text_rect.collidepoint(pos):
                        cell_dict = reset_cell_dict(cell_dict)
                        board_list = update_board_list(board_list, cell_dict)
                    elif restart_text_rect.collidepoint(pos):
                        state = 1
                    elif exit_text_rect.collidepoint(pos):
                        running = False

                    elif pos[1] < screen_width:  # If user click within game board
                        board_coord = get_board_coords(pos, screen_width)
                        selected_cell = board_coord[0] + board_coord[1] * 9  # Stores 0-80 number of selected cell

                elif state == 3:  # Game win screen. Options: Exit
                    if exit_button_text_rect.collidepoint(pos):
                        running = False

                elif state == 4:  # Game lose screen. Options: Restart
                    if restart_button_text_rect.collidepoint(pos):
                        state = 1

            if event.type == pygame.KEYDOWN:
                if state == 2:
                    if event.key == pygame.K_RETURN and selected_cell is not None:
                        for i in range(0, 81):
                            if cell_dict[str(selected_cell)].sketched_value is not None:
                                cell_dict[str(selected_cell)].set_cell_value(cell_dict[str(selected_cell)].sketched_value)
                                cell_dict[str(selected_cell)].set_sketched_value(None)

                    if selected_cell is not None and cell_dict[str(selected_cell)].initial_value == 0:
                        # aKeyboard user input numbers 1-9
                        if event.key == pygame.K_1:
                            cell_dict[str(selected_cell)].set_sketched_value(1)
                        elif event.key == pygame.K_2:
                            cell_dict[str(selected_cell)].set_sketched_value(2)
                        elif event.key == pygame.K_3:
                            cell_dict[str(selected_cell)].set_sketched_value(3)
                        elif event.key == pygame.K_4:
                            cell_dict[str(selected_cell)].set_sketched_value(4)
                        elif event.key == pygame.K_5:
                            cell_dict[str(selected_cell)].set_sketched_value(5)
                        elif event.key == pygame.K_6:
                            cell_dict[str(selected_cell)].set_sketched_value(6)
                        elif event.key == pygame.K_7:
                            cell_dict[str(selected_cell)].set_sketched_value(7)
                        elif event.key == pygame.K_8:
                            cell_dict[str(selected_cell)].set_sketched_value(8)
                        elif event.key == pygame.K_9:
                            cell_dict[str(selected_cell)].set_sketched_value(9)

                    board_list = update_board_list(board_list, cell_dict)
                    if check_if_board_filled(board_list):
                        if check_if_solution(board_list):
                            state = 3
                        else:
                            state = 4

        # STATE 1: Game Start Screen
        if state == 1:
            welcome_text = large_font.render("Welcome to Sudoku", True, black)
            welcome_text_rect = welcome_text.get_rect()
            welcome_text_rect.center = (screen_width // 2, screen_width // 4)
            screen.blit(welcome_text, welcome_text_rect)

            difficulty_text = small_font.render("Select Game Mode:", True, red)
            difficulty_text_rect = difficulty_text.get_rect()
            difficulty_text_rect.center = (screen_width // 2, screen_width // 2)
            screen.blit(difficulty_text, difficulty_text_rect)

            easy_text = button_font.render("EASY", True, black)
            easy_text_rect = easy_text.get_rect()
            easy_text_rect.center = (screen_width // 4, screen_width // 1.6)
            pygame.draw.rect(screen, yellow, easy_text_rect)
            screen.blit(easy_text, easy_text_rect)

            medium_text = button_font.render("MEDIUM", True, black)
            medium_text_rect = medium_text.get_rect()
            medium_text_rect.center = (screen_width // 2, screen_width // 1.6)
            pygame.draw.rect(screen, yellow, medium_text_rect)
            screen.blit(medium_text, medium_text_rect)

            hard_text = button_font.render("HARD", True, black)
            hard_text_rect = hard_text.get_rect()
            hard_text_rect.center = ((screen_width // 4) * 3, screen_width // 1.6)
            pygame.draw.rect(screen, yellow, hard_text_rect)
            screen.blit(hard_text, hard_text_rect)

        # STATE 2: Gameplay Screen
        if state == 2:
            # Draw in-game buttons: Reset, Restart, Exit
            reset_text = button_font.render("RESET", True, black)
            reset_text_rect = reset_text.get_rect()
            reset_text_rect.center = (screen_width // 4, screen_width + (screen_width // 18))
            pygame.draw.rect(screen, yellow, reset_text_rect)
            screen.blit(reset_text, reset_text_rect)

            restart_text = button_font.render("RESTART", True, black)
            restart_text_rect = restart_text.get_rect()
            restart_text_rect.center = (screen_width // 2, screen_width + (screen_width // 18))
            pygame.draw.rect(screen, yellow, restart_text_rect)
            screen.blit(restart_text, restart_text_rect)

            exit_text = button_font.render("EXIT", True, black)
            exit_text_rect = exit_text.get_rect()
            exit_text_rect.center = (3 * (screen_width // 4), screen_width + (screen_width // 18))
            pygame.draw.rect(screen, yellow, exit_text_rect)
            screen.blit(exit_text, exit_text_rect)

            # Draw thick lines
            thick_line_locations = [0, screen_width // 3, (screen_width // 3) * 2, screen_width - 4]
            for horizontal_line in thick_line_locations:
                pygame.draw.line(screen, black, (horizontal_line, 0), (horizontal_line, screen_width), width=8)
            for vertical_line in thick_line_locations:
                pygame.draw.line(screen, black, (0, vertical_line), (screen_width, vertical_line), width=8)

            # Draw thin lines
            thin_line_locations = []
            for i in range(0, 10):
                thin_line_locations.append((screen_width // 9) * i)
            for horizontal_line in thin_line_locations:
                pygame.draw.line(screen, black, (horizontal_line, 0), (horizontal_line, screen_width), width=3)
            for vertical_line in thin_line_locations:
                pygame.draw.line(screen, black, (0, vertical_line), (screen_width, vertical_line), width=3)

            # Display pre-set numbers (if), user-set numbers (elif #1), and sketched numbers (elif #2)
            for i in range(0, 81):
                row = i // 9
                col = i % 9
                num = board_list[row][col]
                num_pos = (((screen_width // 18) * ((col * 2) + 1)), ((screen_width // 18) * ((row * 2) + 1)))
                if cell_dict[str(i)].initial_value != 0:
                    num_text = small_font.render(str(num), True, black)
                    num_text_rect = num_text.get_rect()
                    num_text_rect.center = num_pos
                    screen.blit(num_text, num_text_rect)
                elif cell_dict[str(i)].initial_value == 0 and board_list[row][col] != 0:
                    num_text = small_font.render(str(num), True, red)
                    num_text_rect = num_text.get_rect()
                    num_text_rect.center = num_pos
                    screen.blit(num_text, num_text_rect)
                if cell_dict[str(i)].sketched_value is not None:
                    sketch_num_pos = ((num_pos[0] - (screen_width // 30)), (num_pos[1] - (screen_width // 30)))
                    num_text = tiny_font.render(str(cell_dict[str(i)].sketched_value), True, gray)
                    num_text_rect = num_text.get_rect()
                    num_text_rect.center = sketch_num_pos
                    screen.blit(num_text, num_text_rect)

            # Highlights Selected Cell in Red
            if selected_cell is not None:
                row = selected_cell // 9
                col = selected_cell % 9

                pygame.draw.line(screen, red, ((screen_width * col // 9), ((screen_width // 9) * row)),
                                 ((screen_width // 9) * col, ((screen_width // 9) * (row + 1))), width=8)
                pygame.draw.line(screen, red, ((screen_width // 9) * (col + 1), ((screen_width // 9) * row)),
                                 ((screen_width // 9) * (col + 1), ((screen_width // 9) * (row + 1))), width=8)
                pygame.draw.line(screen, red, ((screen_width // 9) * col, ((screen_width // 9) * row)),
                                 ((screen_width // 9) * (col + 1), ((screen_width // 9) * row)), width=8)
                pygame.draw.line(screen, red, ((screen_width // 9) * col, ((screen_width // 9) * (row + 1))),
                                 ((screen_width // 9) * (col + 1), ((screen_width // 9) * (row + 1))), width=8)

        # STATE 3: Winning Game End Screen
        if state == 3:
            win_text = large_font.render("Game Won!", True, black)
            win_text_rect = win_text.get_rect()
            win_text_rect.center = (screen_width // 2, screen_width // 3)
            screen.blit(win_text, win_text_rect)

            exit_button_text = button_font.render("EXIT", True, black)
            exit_button_text_rect = exit_button_text.get_rect()
            exit_button_text_rect.center = (screen_width // 2, screen_width // 2)
            pygame.draw.rect(screen, yellow, exit_button_text_rect)
            screen.blit(exit_button_text, exit_button_text_rect)

        # STATE 4: Losing Game End Screen
        if state == 4:
            lose_text = large_font.render("Game Over :(", True, black)
            lose_text_rect = lose_text.get_rect()
            lose_text_rect.center = (screen_width // 2, screen_width // 3)
            screen.blit(lose_text, lose_text_rect)

            restart_button_text = button_font.render("RESTART", True, black)
            restart_button_text_rect = restart_button_text.get_rect()
            restart_button_text_rect.center = (screen_width // 2, screen_width // 2)
            pygame.draw.rect(screen, yellow, restart_button_text_rect)
            screen.blit(restart_button_text, restart_button_text_rect)

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
