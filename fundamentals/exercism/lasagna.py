"""Functions used in preparing Guido's gorgeous lasagna.

Exercism exercise: practices defining functions with default/required
parameters, basic arithmetic operations, and writing clear docstrings.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(lasagna_layers):
    """Calculate the preparation time in minutes.

    Parameters:
        lasagna_layers (int): The number of layers for that lasagna.

    Returns:
        int: The amount of time (in minutes) needed to prepare the lasagna,
        based on how many layers are needed and PREPARATION_TIME.
    """
    return lasagna_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, baked_time):
    """Calculate the elapsed time of the preparation in minutes.

    Parameters:
        number_of_layers (int): The number of layers already prepared for that lasagna.
        baked_time (int): Time spent so far for baking in minutes.

    Returns:
        int: The amount of time (in minutes) spent so far to prepare and bake the lasagna.
    """
    return baked_time + number_of_layers * PREPARATION_TIME
