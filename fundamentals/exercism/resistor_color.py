def color_code(color):
    """Return the numeric value associated with a given resistor color band.

    Raises a ValueError if the color is not a recognized band color.
    """
    return colors().index(color)


def colors():
    """Return the list of resistor band colors, ordered by their numeric value
    (black=0 through white=9).
    """
    return ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
