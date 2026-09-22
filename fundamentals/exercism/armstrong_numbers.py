def is_armstrong_number(number):
    """
    Determine whether a number is an Armstrong number.

    An Armstrong number (also called a narcissistic number) is a number that is
    equal to the sum of its own digits, each raised to the power of the number
    of digits.

    Examples:
        9   → 9 = 9^1
        10  → 10 != 1^2 + 0^2 = 1
        153 → 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27
        154 → 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190

    Parameters:
        number (int): The integer to evaluate.

    Returns:
        bool: True if `number` is an Armstrong number, False otherwise.
    """
    numbers = [int(num) for num in str(number)]
    total = sum(num**len(numbers) for num in numbers)
    return number == total
