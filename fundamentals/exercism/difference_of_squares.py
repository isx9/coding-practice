def square_of_sum(number):
    """
    Return the square of the sum of the first N natural numbers.
    """
    return sum(range (1, number+1))**2


def sum_of_squares(number):
    """
    Return the sum of the squares of the first N natural numbers.
    """
    return sum(num**2 for num in range (1, number+1))


def difference_of_squares(number):
    """
    Return the difference between the square of the sum of the first N natural numbers and the sum of the squares of the first N natural numbers
    """
    return square_of_sum(number)-sum_of_squares(number)
