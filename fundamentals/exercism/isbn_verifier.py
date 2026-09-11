"""Module for validating ISBN-10 numbers."""


def is_valid(isbn):
    """Check whether a given string is a valid ISBN-10 number."""
    isbn_numbers = []
    index_list = 0
    num = 10
    total = 0
    for char in isbn:
        if char.isdigit():
            isbn_numbers.append(int(char))
        elif char == "X" and len(isbn_numbers) == 9:
            isbn_numbers.append(10)
        elif char == "-":
            continue
        else:
            return False
    if len(isbn_numbers) != 10:
        return False
    while num != 0:
        total += isbn_numbers[index_list]*num
        index_list += 1
        num -= 1
    return total % 11 == 0
