def steps(number):
    """Return the number of steps to reach 1 following the Collatz Conjecture rules."""
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        steps += 1
    return steps
