def convert(number):
    """Convert a number to its corresponding raindrop sounds.

    Rules:
        - If the number is divisible by 3, add "Pling".
        - If the number is divisible by 5, add "Plang".
        - If the number is divisible by 7, add "Plong".
        - If the number is not divisible by 3, 5, or 7,
          return the number itself as a string.

    Args:
        number (int): The number to convert.

    Returns:
        str: The combined raindrop sounds, or the number as a
            string if none of the divisibility rules apply.

    Examples:
        >>> convert(28)
        'Plong'
        >>> convert(30)
        'PlingPlang'
        >>> convert(34)
        '34'
    """
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    return result if result else str(number)
