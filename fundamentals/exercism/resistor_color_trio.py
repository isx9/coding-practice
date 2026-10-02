COLORS = ['black', 'brown', 'red', 'orange', 'yellow',
          'green', 'blue', 'violet', 'grey', 'white']


def label(colors):
    """Return the resistance label for the first three color bands.

    :param colors: list - color names of the resistor bands.
    :return: str - resistance value with the appropriate metric prefix.
    """
    first = COLORS.index(colors[0])
    second = COLORS.index(colors[1])
    third = COLORS.index(colors[2])

    ohms = (first * 10 + second) * 10 ** third

    if ohms and ohms % 1_000_000_000 == 0:
        return f'{ohms // 1_000_000_000} gigaohms'
    if ohms and ohms % 1_000_000 == 0:
        return f'{ohms // 1_000_000} megaohms'
    if ohms and ohms % 1_000 == 0:
        return f'{ohms // 1_000} kiloohms'
    return f'{ohms} ohms'
