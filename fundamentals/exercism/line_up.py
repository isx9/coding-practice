"""Announce a customer's position in line, with the correct ordinal suffix."""


def line_up(name, number):
    """Generate a message announcing a customer's position in line, with correct ordinal suffix.

    Parameters:
        name (str): The name of the customer.
        number (int): The customer's position in line.

    Returns:
        str: A message with the number formatted with its ordinal suffix (1st, 2nd, 3rd, 4th...).
    """
    last_digit = number % 10
    last_two_digits = number % 100

    if last_digit == 1 and last_two_digits != 11 and number != 11:
        term = 'st'
    elif last_digit == 2 and last_two_digits != 12 and number != 12:
        term = 'nd'
    elif last_digit == 3 and last_two_digits != 13 and number != 13:
        term = 'rd'
    else:
        term = 'th'

    return f"{name}, you are the {number}{term} customer we serve today. Thank you!"
