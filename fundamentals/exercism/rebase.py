"""Convert a sequence of digits from one base into a sequence of digits in another base."""


def rebase(input_base, digits, output_base):
    """Convert a sequence of digits from one base to another base.

    Parameters:
        input_base (int): The base the input digits are expressed in.
        digits (list): The digits of the number, most-significant digit first,
            expressed in input_base.
        output_base (int): The base to convert the number into.

    Returns:
        list: The digits of the same number, most-significant digit first,
            expressed in output_base.
    """
    if input_base < 2:
        raise ValueError('input base must be >= 2')
    if output_base < 2:
        raise ValueError('output base must be >= 2')

    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError('all digits must satisfy 0 <= d < input base')

    total = 0
    for index, digit in enumerate(reversed(digits)):
        total += int(digit) * (input_base ** index)

    if total == 0:
        return [0]

    output_digits = []
    while total > 0:
        output_digits.append(total % output_base)
        total //= output_base
    return output_digits[::-1]
