"""Module for calculating grains of wheat on a chessboard."""


def square(number):
    """Return the number of grains on a given chessboard square (1-64)."""
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    """Return the total number of grains on the entire chessboard."""
    total_grains = 0
    for index in range(1, 65):
        total_grains += square(index)
    return total_grains
