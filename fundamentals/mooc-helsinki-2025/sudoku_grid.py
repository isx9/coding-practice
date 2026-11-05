def has_no_duplicates(numbers: list):
    """Return True if the non-zero numbers in the list are all distinct."""
    seen = set()
    for number in numbers:
        if number == 0:
            continue
        if number in seen:
            return False
        seen.add(number)
    return True


def row_correct(sudoku: list, row_no: int):
    """Check that a row contains no repeated numbers."""
    return has_no_duplicates(sudoku[row_no])


def column_correct(sudoku: list, column_no: int):
    """Check that a column contains no repeated numbers."""
    return has_no_duplicates([row[column_no] for row in sudoku])


def block_correct(sudoku: list, row_no: int, column_no: int):
    """Check that the 3x3 block starting at (row_no, column_no) has no repeats."""
    block = [
        sudoku[row][column]
        for row in range(row_no, row_no + 3)
        for column in range(column_no, column_no + 3)
    ]
    return has_no_duplicates(block)


def sudoku_grid_correct(sudoku: list):
    """Check every row, column and 3x3 block of the grid."""
    for index in range(9):
        if not row_correct(sudoku, index):
            return False
        if not column_correct(sudoku, index):
            return False

    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            if not block_correct(sudoku, row, column):
                return False

    return True
