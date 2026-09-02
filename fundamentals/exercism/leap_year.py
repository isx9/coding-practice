def leap_year(year):
    """Determine whether a given year is a leap year.

    Parameters:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.

    Examples:
        >>> leap_year(2000)
        True

        >>> leap_year(1900)
        False
    """
    return year%4 == 0 and (year%100 != 0 or year%400 == 0)
