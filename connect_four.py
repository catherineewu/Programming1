# LAB 05: CONNECT FOUR


def print_board(board_string):
    for row in range((len(board_string) - 1), -1, -1):
        print(' '.join(board_string[row]), end='')
        print()
    print()


def initialize_board(rows, cols):
    board = []
    for row in range(rows):
        board.append([])
        for col in range(cols):
            board[row].append('-')
    return board


def insert_chip(board_string, col, chip_type):
    for row in range(len(board_string)):
        if board_string[row][col] == '-':
            board_string[row][col] = chip_type
            break
    return board_string


def check_if_winner(board, col, row, chip_type):
    # check for 4 in a row vertically and horizontally of current player chip type
    win = False
    # HORIZONTAL CHECK
    for check_row in range(row):
        tokens_in_row = 0
        for check_col in range(col):
            if board[check_row][check_col] == chip_type:
                tokens_in_row += 1
            else:
                tokens_in_row = 0
            if tokens_in_row == 4:
                win = True
                break
        if win:
            break
    # VERTICAL CHECK
    if not win:
        for check_col in range(col):
            tokens_in_col = 0
            for check_row in range(row):
                if board[check_row][check_col] == chip_type:
                    tokens_in_col += 1
                else:
                    tokens_in_col = 0
                if tokens_in_col == 4:
                    win = True
                    break
            if win:
                break

    # return winner False or winner True
    return win


def check_if_board_full(board, col, row):
    full = True
    for check_row in range(row):
        for check_col in range(col):
            if board[check_row][check_col] == '-':
                full = False
                break
        if not full:
            break
    return full


def main():
    num_rows = int(input('What would you like the height of the board to be? '))
    num_cols = int(input('What would you like the length of the board to be? '))
    board = initialize_board(num_rows, num_cols)

    print_board(board)
    print('Player 1: x\nPlayer 2: o\n')
    token1 = 'x'
    token2 = 'o'

    turn = 0
    winner = False
    board_full = False
    while not winner and not board_full:
        turn += 1
        if turn % 2 == 1:
            token = token1
            place_col = int(input('Player 1: Which column would you like to choose? '))
            board = insert_chip(board, place_col, token)
        else:
            token = token2
            place_col = int(input('Player 2: Which column would you like to choose? '))
            board = insert_chip(board, place_col, token)
        print_board(board)
        winner = check_if_winner(board, num_cols, num_rows, token)
        board_full = check_if_board_full(board, num_cols, num_rows)

    if winner:
        if turn % 2 == 1:
            print('Player 1 won the game!')
        else:
            print('Player 2 won the game!')
    else:
        print('Draw. Nobody wins.')


if __name__ == '__main__':
    main()