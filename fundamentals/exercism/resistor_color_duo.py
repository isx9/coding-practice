def value(colors):
    """Return the two-digit resistor value from a sequence of color bands,
    using only the first two colors and ignoring any additional bands.
    """
    ordered_colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    values = [str(ordered_colors.index(color)) for color in colors]
    return int(''.join(values[0:2]))
