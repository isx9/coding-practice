"""Functions for classifying numbers as perfect, abundant or deficient."""

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    divisors = []
    for index in range(1, number):
        if number%index == 0:
            divisors.append(index)

    total = sum(divisors)
    if total == number:
        return "perfect"
    if total > number:
        return "abundant"
    return "deficient"
