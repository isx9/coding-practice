def score(x, y):
    """Calculate the points scored for a dart landing at (x, y).

    Parameters:
        x (float): The x-coordinate of the dart's landing position.
        y (float): The y-coordinate of the dart's landing position.

    Returns:
        int: The points earned (0, 1, 5, or 10).
    """
    distance = x**2 + y**2
    if distance <= 1**2:
        return 10
    if distance <= 5**2:
        return 5
    if distance <= 10**2:
        return 1
    return 0
