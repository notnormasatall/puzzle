'''Function'''


def convert_to_normal(board):
    '''
    The following function converts a board, so the rows areas become columns.
    '''
    new_board = []
    col = 0
    for row_i in reversed(range(5)):
        col_1 = ''
        col_2 = ''

        col_1 += board[row_i+3][col] + board[row_i+2][col] + \
            board[row_i+1][col] + board[row_i][col]
        col_2 += board[row_i+4][col] + board[row_i+4][col+1] + \
            board[row_i+4][col+2] + board[row_i+4][col+3] + \
            board[row_i+4][col+4]

        new_board.append(col_1[::-1]+col_2)

        col += 1
    return new_board


def check_areas(board):
    '''
    The following function checks, if there's no 1-9 matches on colored areas.
    '''
    for elem in board:
        elem = elem.replace(' ', '')
        elem = list(elem)

        if len(elem) != len(set(elem)):
            return False
    return True


def check_rows(board):
    '''
    The following function checks, if there's no 1-9 matches on rows.
    '''
    for elem in board:
        elem = elem.replace('*', '')
        elem = elem.replace(' ', '')
        elem = list(elem)

        if len(elem) != len(set(elem)):
            return False
    return True


def check_columns(board):
    '''
    The following function checks, if there's no 1-9 matches on columns.
    '''
    new_board = []
    for index in range(9):
        new_row = ''
        for elem in board:
            new_row += elem[index]
        new_board.append(new_row)

    result = check_rows(new_board)

    if not result:
        return False

    return True


def validate_board(board):
    '''
    The following function checks the board by all the criterias.
    >>> validate_board(["**** ****","***1 ****","**  3****",\
    "* 4 1****","     9 5 ", " 6  83  *","3   2  **","  8  2***","  2  ****"])
    True
    '''
    new_board = convert_to_normal(board)

    test1 = check_areas(new_board)
    test2 = check_rows(board)
    test3 = check_columns(board)

    if not test1 or not test2 or not test3:
        return False

    return True
