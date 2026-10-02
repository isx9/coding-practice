"""Flatten a nested list of any depth into a single list."""


def flatten(iterable):
    """Return a flat list of all non-None values in a nested list.

    :param iterable: list - list that may contain nested lists and None values.
    :return: list - all values in their original order, with None removed.
    """
    result = []
    for item in iterable:
        if isinstance(item, list):
            result.extend(flatten(item))
        elif item is not None:
            result.append(item)
    return result
